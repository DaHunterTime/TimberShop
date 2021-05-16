from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QScrollArea

from .product import ProductOverview


class MainMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Buscar tiendas o productos")

        # Change button name with icon
        self.search_button = QPushButton("Buscar", self)

        hbox_search = QHBoxLayout()
        hbox_search.addWidget(self.search_bar)
        hbox_search.addWidget(self.search_button)

        self.products = ProductsManager(self)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.products)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_search)
        vbox.addWidget(self.scroll_area)

        self.setLayout(vbox)


class ProductsManager(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.items = []
        self.init_UI()

    def init_UI(self):
        vbox = QVBoxLayout()

        with open("products/data.txt", "r") as file:
            for line in file:
                line = line.strip()
                product = ProductOverview(line)
                self.items.append(product)
                vbox.addWidget(product)

        self.setLayout(vbox)
