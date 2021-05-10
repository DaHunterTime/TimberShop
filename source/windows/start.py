from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout


class StartScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        self.setStyleSheet("background-color: rgb(86, 255, 0);")

        self.sign_in_button = QPushButton("Iniciar Sesión", self)
        self.sign_in_button.setStyleSheet("background-color: none;")

        self.sign_up_button = QPushButton("Registrarse", self)
        self.sign_up_button.setStyleSheet("background-color: none;")

        vbox = QVBoxLayout()
        vbox.addWidget(self.sign_in_button)
        vbox.addWidget(self.sign_up_button)

        self.setLayout(vbox)
