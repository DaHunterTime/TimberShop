from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class SettingsScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        self.title = QLabel("Ajustes", self)
        self.title.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title)

        self.setLayout(vbox)
