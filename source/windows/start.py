from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt


class StartScreen(QWidget):
    sign_in_signal = pyqtSignal()
    sign_up_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        self.setStyleSheet("background-color: rgb(86, 255, 0);")

        pixels = QPixmap("img/logo.png")
        pixels = pixels.scaled(220, 220, Qt.KeepAspectRatio)
        self.logo = QLabel(self)
        self.logo.setPixmap(pixels)
        self.logo.setAlignment(Qt.AlignCenter)

        self.sign_in_button = QPushButton("Iniciar Sesión", self)
        self.sign_in_button.setStyleSheet("background-color: none;")
        self.sign_in_button.clicked.connect(self.sign_in)

        self.sign_up_button = QPushButton("Registrarse", self)
        self.sign_up_button.setStyleSheet("background-color: none;")
        self.sign_up_button.clicked.connect(self.sign_up)

        self.prototype_version = QLabel("V0.7.2", self)
        self.prototype_version.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        vbox = QVBoxLayout()
        vbox.addWidget(self.logo)
        vbox.addWidget(self.sign_in_button)
        vbox.addWidget(self.sign_up_button)
        vbox.addWidget(self.prototype_version)

        self.setLayout(vbox)

    def sign_in(self):
        self.sign_in_signal.emit()

    def sign_up(self):
        self.sign_up_signal.emit()
