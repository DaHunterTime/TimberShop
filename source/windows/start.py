from hashlib import sha256

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt


class StartScreen(QWidget):
    sign_in_signal = pyqtSignal(dict)
    sign_up_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        self.setStyleSheet("background-color: black;")

        pixels = QPixmap("img/logo.png")
        pixels = pixels.scaled(220, 220, Qt.KeepAspectRatio)
        self.logo = QLabel(self)
        self.logo.setPixmap(pixels)
        self.logo.setAlignment(Qt.AlignCenter)

        self.sign_in_button = QPushButton("Iniciar Sesión", self)
        self.sign_in_button.setStyleSheet("background-color: none;")
        self.sign_in_button.clicked.connect(self.sign_in)
        self.sign_in_button.setMaximumWidth(200)
        self.sign_in_button.setMinimumSize(150, 30)

        self.sign_up_button = QPushButton("Registrarse", self)
        self.sign_up_button.setStyleSheet("background-color: none;")
        self.sign_up_button.clicked.connect(self.sign_up)
        self.sign_up_button.setMaximumWidth(200)
        self.sign_up_button.setMinimumSize(150, 30)

        self.prototype_version = QLabel("V1.0.0", self)
        self.prototype_version.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        self.prototype_version.setStyleSheet("color: white; font: 8px;")

        self.user = QLineEdit(self)
        self.user.setPlaceholderText("Nombre de usuario")
        self.user.setStyleSheet("background-color: None;")
        self.user.setMaximumWidth(200)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Contraseña")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("background-color: None;")
        self.password.setMaximumWidth(200)

        self.error = QLabel(self)
        self.error.setAlignment(Qt.AlignCenter)
        self.error.setStyleSheet("color: white;")
        self.error.hide()

        vbox = QVBoxLayout()
        vbox.addWidget(self.logo)
        vbox.addWidget(self.user, alignment=Qt.AlignCenter)
        vbox.addWidget(self.password, alignment=Qt.AlignCenter)
        vbox.addWidget(self.error)
        vbox.addWidget(self.sign_in_button, alignment=Qt.AlignCenter)
        vbox.addWidget(self.sign_up_button, alignment=Qt.AlignCenter)
        vbox.addWidget(self.prototype_version)

        self.setLayout(vbox)

    def sign_in(self):
        data = {"user": self.user.text(),
                "hash": sha256(self.password.text().encode("utf-8")).hexdigest()}
        self.sign_in_signal.emit(data)

    def sign_up(self):
        data = {"user": self.user.text(),
                "hash": sha256(self.password.text().encode("utf-8")).hexdigest()}
        self.sign_up_signal.emit(data)

    def display_error(self, error):
        self.error.setText(error)
        self.error.show()
