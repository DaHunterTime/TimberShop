import json

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal


class ProductScreen(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent=parent)
        self.init_UI(data)

    def init_UI(self, info):
        self.back_button = QPushButton("< Atrás", self)

        self.name = QLabel(f"{info['name']}", self)
        self.name.setAlignment(Qt.AlignCenter)
        self.description = QLabel(f"{info['description']}", self)
        self.description.setAlignment(Qt.AlignJustify)
        self.price = QLabel(f"Precio: ${info['price']}")

        self.buy_button = QPushButton("Agregar al carrito", self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.back_button, alignment=Qt.AlignTop | Qt.AlignLeft)
        vbox.addWidget(self.name)
        vbox.addWidget(self.description)
        vbox.addWidget(self.price)
        vbox.addWidget(self.buy_button, alignment=Qt.AlignBottom | Qt.AlignCenter)

        self.setLayout(vbox)


class ProductOverview(QPushButton):
    set_screen_signal = pyqtSignal(ProductScreen)

    def __init__(self, path, parent=None):
        super().__init__(parent=parent)

        with open(path, "rb") as file:
            info = json.load(file)

        self.init_UI(info)

        self.screen = ProductScreen(info, parent)

    def init_UI(self, info):
        self.setText(f"{info['name']} ${info['price']}")
        self.clicked.connect(self.show_screen)

    def show_screen(self):
        self.set_screen_signal.emit(self.screen)
