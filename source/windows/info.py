from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt


class InfoScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        self.title = QLabel("Información", self)
        self.title.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.description = QLabel("Descripción del proyecto:", self)
        self.description.setAlignment(Qt.AlignLeft)
        self.description_contents = QLabel("Información relevante", self)
        self.description_contents.setAlignment(Qt.AlignJustify)
        self.description_contents.setWordWrap(True)

        # Temporary
        self.business = QLabel("Información de 'Empresa':", self)
        self.business.setAlignment(Qt.AlignLeft)
        self.business_contents = QLabel("Información relevante", self)
        self.business_contents.setAlignment(Qt.AlignJustify)
        self.business_contents.setWordWrap(True)

        hbox_description = QHBoxLayout()
        hbox_description.addWidget(self.description)
        hbox_description.addWidget(self.description_contents)

        # Temporary
        hbox_business = QHBoxLayout()
        hbox_business.addWidget(self.business)
        hbox_business.addWidget(self.business_contents)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addLayout(hbox_description)
        vbox.addLayout(hbox_business)

        self.setLayout(vbox)
