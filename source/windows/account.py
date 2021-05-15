from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class AccountScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        self.title = QLabel("Mi Cuenta", self)
        self.title.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.name = QLabel("Nombre:", self)
        self.name.setAlignment(Qt.AlignLeft)
        self.name_contents = QLabel("Nombre Apellido", self)
        self.name_contents.setAlignment(Qt.AlignJustify)

        self.address = QLabel("Dirección:", self)
        self.address.setAlignment(Qt.AlignLeft)
        self.address_contents = QLabel("Calle Número", self)
        self.address_contents.setAlignment(Qt.AlignJustify)

        self.payment = QLabel("Método de pago:", self)
        self.payment.setAlignment(Qt.AlignLeft)
        self.payment_info = QLabel("Tarjeta de crédito", self)
        self.payment_info.setAlignment(Qt.AlignJustify)

        hbox_name = QHBoxLayout()
        hbox_name.addWidget(self.name)
        hbox_name.addWidget(self.name_contents)

        hbox_address = QHBoxLayout()
        hbox_address.addWidget(self.address)
        hbox_address.addWidget(self.address_contents)

        hbox_payment = QHBoxLayout()
        hbox_payment.addWidget(self.payment)
        hbox_payment.addWidget(self.payment_info)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addLayout(hbox_name)
        vbox.addLayout(hbox_address)
        vbox.addLayout(hbox_payment)

        self.setLayout(vbox)
