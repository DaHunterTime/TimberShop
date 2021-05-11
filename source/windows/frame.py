from PyQt5.QtWidgets import QMainWindow, QScrollArea, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

from .start import StartScreen
from .main_menu import MainMenu
from .info import InfoScreen


class AppFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("TimberShop App Prototype")
        self.setFixedSize(440, 620)

        # Screens & Menus
        self.start_screen = StartScreen(self)
        self.main_menu = Wrapper(MainMenu, self)
        self.info_screen = Wrapper(InfoScreen, self)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.start_screen)

        self.setCentralWidget(self.scroll_area)

        # Connecting signals
        # Navigation buttons
        self.main_menu.navigation.connect_buttons_signal.connect(self.connect_navigation)
        self.info_screen.navigation.connect_buttons_signal.connect(self.connect_navigation)

        # Sign in/up
        self.start_screen.sign_in_signal.connect(self.sign_in)
        self.start_screen.sign_up_signal.connect(self.sign_up)

        # Connect navigation buttons
        self.main_menu.navigation.connect_buttons()
        self.info_screen.navigation.connect_buttons()

        self.show()

    def sign_in(self):
        # temporary
        self.start_screen = self.scroll_area.takeWidget()
        self.scroll_area.setWidget(self.main_menu)

    def sign_up(self):
        pass

    def connect_navigation(self, buttons):
        buttons["home"].clicked.connect(self.go_home)
        buttons["cart"].clicked.connect(self.go_cart)
        buttons["account"].clicked.connect(self.go_account)
        buttons["settings"].clicked.connect(self.go_settings)
        buttons["info"].clicked.connect(self.go_info)

    def go_home(self):
        widget = self.scroll_area.takeWidget()

        if type(widget.class_) == InfoScreen:
            self.info_screen = widget

        self.scroll_area.setWidget(self.main_menu)

    def go_cart(self):
        pass

    def go_account(self):
        pass

    def go_settings(self):
        pass

    def go_info(self):
        widget = self.scroll_area.takeWidget()

        if type(widget.class_) == MainMenu:
            self.main_menu = widget

        self.scroll_area.setWidget(self.info_screen)


class NavigationDock(QWidget):
    connect_buttons_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        # Change button names to icons
        self.home_button = QPushButton("Inicio", self)

        self.cart_button = QPushButton("carrito", self)

        self.account_button = QPushButton("Mi Cuenta", self)

        self.settings_button = QPushButton("Ajustes", self)

        self.info_button = QPushButton("Info", self)

        self.buttons = {"home": self.home_button, "cart": self.cart_button,
                        "account": self.account_button, "settings": self.settings_button,
                        "info": self.info_button}

        hbox = QHBoxLayout()
        hbox.addWidget(self.home_button)
        hbox.addWidget(self.cart_button)
        hbox.addWidget(self.account_button)
        hbox.addWidget(self.settings_button)
        hbox.addWidget(self.info_button)

        self.setLayout(hbox)

    def connect_buttons(self):
        self.connect_buttons_signal.emit(self.buttons)


class Wrapper(QWidget):
    def __init__(self, class_, parent=None):
        super().__init__(parent=parent)
        self.class_ = class_(parent)
        self.navigation = NavigationDock(parent)

        vbox = QVBoxLayout()
        vbox.addWidget(self.class_)
        vbox.addWidget(self.navigation)

        self.setLayout(vbox)
