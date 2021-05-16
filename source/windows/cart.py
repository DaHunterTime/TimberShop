from uuid import uuid4

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox, \
                            QScrollArea
from PyQt5.QtCore import Qt, pyqtSignal


class CartScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.total_price = 0
        self.init_UI()

    def init_UI(self):
        self.title = QLabel("Carrito", self)
        self.title.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.products_container = ProductContainer(self)
        self.products_scroll = QScrollArea(self)
        self.products_scroll.setWidgetResizable(True)
        self.products_scroll.setWidget(self.products_container)

        self.final_price = QLabel(f"Precio total: ${self.total_price}", self)

        self.buy_button = QPushButton("Comprar", self)
        self.buy_button.clicked.connect(self.buy_products)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addWidget(self.products_scroll)
        vbox.addWidget(self.final_price)
        vbox.addWidget(self.buy_button)

        self.setLayout(vbox)

    def add_product(self, info):
        product = ProductSummary(info, self.products_container)
        self.products_container.add_product(product)
        price = product.unit_price * product.amount
        self.update_price(price)
        product.delete_signal.connect(self.products_container.delete_by_uuid)
        product.delete_price_signal.connect(self.update_price)
        product.update_price_signal.connect(self.update_price)

    def buy_products(self):
        # Incomplete
        for product in self.products_container.products[::]:
            self.products_container.delete_product(product)

        self.set_price(0)

    def update_price(self, price):
        self.total_price += price
        self.final_price.setText(f"Precio total: ${self.total_price}")

    def set_price(self, price):
        self.total_price = price
        self.final_price.setText(f"Precio total: ${self.total_price}")


class ProductSummary(QWidget):
    delete_signal = pyqtSignal(str)
    delete_price_signal = pyqtSignal(int)
    update_price_signal = pyqtSignal(int)

    def __init__(self, info, parent=None):
        super().__init__(parent=parent)
        self.unit_price = info["price"]
        self.amount = info["quantity"]
        self.uuid = uuid4().hex
        self.init_UI(info)

    def init_UI(self, info):
        self.name = QLabel(f"{info['name']}", self)

        self.price = QLabel(f"${info['price']}", self)

        self.quantity = QSpinBox(self)
        self.quantity.setRange(1, 2147483647)
        self.quantity.setValue(info["quantity"])
        self.quantity.valueChanged.connect(self.change_price)

        self.delete_button = QPushButton("x", self)
        self.delete_button.clicked.connect(self.delete)

        hbox = QHBoxLayout()
        hbox.addWidget(self.name)
        hbox.addWidget(self.price)
        hbox.addWidget(self.quantity)
        hbox.addWidget(self.delete_button)

        self.setLayout(hbox)

    def change_price(self):
        take = self.unit_price * self.amount
        self.amount = self.quantity.value()
        add = self.unit_price * self.amount
        self.update_price_signal.emit(add - take)

    def delete(self):
        self.delete_signal.emit(self.uuid)
        take = (self.unit_price * self.amount) * -1
        self.delete_price_signal.emit(take)


class ProductContainer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.products = []
        self.init_UI()

    def init_UI(self):
        self.vbox = QVBoxLayout(self)
        self.setLayout(self.vbox)

    def add_product(self, product):
        self.vbox.addWidget(product)
        self.products.append(product)

    def delete_product(self, product):
        self.vbox.removeWidget(product)
        self.products.remove(product)

    def delete_by_uuid(self, uuid):
        for product in self.products:
            if product.uuid == uuid:
                break

        self.delete_product(product)
