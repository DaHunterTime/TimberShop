from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout


class MainMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Buscar tiendas o productos")

        # Change button name with icon
        self.search_button = QPushButton("Buscar", self)

        vbox = QHBoxLayout()
        vbox.addWidget(self.search_bar)
        vbox.addWidget(self.search_button)

        self.setLayout(vbox)
