from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon

from .product import ProductOverview


class MainMenu(QWidget):
    def __init__(self, tips, parent=None):
        super().__init__(parent=parent)
        self.init_UI(tips)

    def init_UI(self, tips):
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Buscar tiendas o productos")

        self.search_button = QPushButton(self)
        self.search_button.setIcon(QIcon("img/search.png"))
        self.search_button.setToolTip("Buscar")
        self.search_button.setStyleSheet("background-color: rgb(146, 237, 108);")

        hbox_search = QHBoxLayout()
        hbox_search.addWidget(self.search_bar)
        hbox_search.addWidget(self.search_button)

        self.products = ProductsManager(tips, self)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.products)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_search)
        vbox.addWidget(self.scroll_area)

        self.setLayout(vbox)


class ProductsManager(QWidget):
    def __init__(self, tips, parent=None):
        super().__init__(parent=parent)
        self.items = []
        self.init_UI(tips)

    def init_UI(self, tips):
        vbox = QVBoxLayout()

        with open("products/data.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                product = ProductOverview(line, tips, self)
                self.items.append(product)
                vbox.addWidget(product)

        self.setLayout(vbox)
