from PyQt5.QtWidgets import QMainWindow, QScrollArea, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

from .start import StartScreen
from .main_menu import MainMenu
from .cart import CartScreen
from .account import AccountScreen
from .settings import SettingsScreen
from .info import InfoScreen
from .tips import Tips


class AppFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("TimberShop App Prototype")
        self.setFixedSize(440, 620)

        # Environmental tips
        self.tips = Tips()

        # Screens & Menus
        self.start_screen = StartScreen(self)
        self.main_menu = Wrapper(MainMenu, self, self.tips)
        self.cart_menu = Wrapper(CartScreen, self, self.tips)
        self.account_menu = Wrapper(AccountScreen, self)
        self.settings_menu = Wrapper(SettingsScreen, self)
        self.info_screen = Wrapper(InfoScreen, self)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.start_screen)

        self.setCentralWidget(self.scroll_area)

        # Connecting signals
        # Navigation buttons
        self.main_menu.navigation.connect_buttons_signal.connect(self.connect_navigation)
        self.cart_menu.navigation.connect_buttons_signal.connect(self.connect_navigation)
        self.account_menu.navigation.connect_buttons_signal.connect(self.connect_navigation)
        self.settings_menu.navigation.connect_buttons_signal.connect(self.connect_navigation)
        self.info_screen.navigation.connect_buttons_signal.connect(self.connect_navigation)

        # Sign in/up
        self.start_screen.sign_in_signal.connect(self.sign_in)
        self.start_screen.sign_up_signal.connect(self.sign_up)

        # Connect navigation buttons
        self.main_menu.navigation.connect_buttons()
        self.cart_menu.navigation.connect_buttons()
        self.account_menu.navigation.connect_buttons()
        self.settings_menu.navigation.connect_buttons()
        self.info_screen.navigation.connect_buttons()

        # Connect products buttons
        for product in self.main_menu.class_.products.items:
            product.screen.back_button.clicked.connect(self.go_back)
            product.set_screen_signal.connect(self.go_product)
            product.screen.add_product_signal.connect(self.cart_menu.class_.add_product)

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

    def go_back(self):
        widget = self.scroll_area.takeWidget()

        for index, product in enumerate(self.main_menu.class_.products.items):
            if product.screen == widget:
                self.main_menu.class_.products.items[index] = widget
                break

        self.scroll_area.setWidget(self.main_menu)

    def go_product(self, screen):
        self.main_menu = self.scroll_area.takeWidget()
        screen.change_tip()
        self.scroll_area.setWidget(screen)

    def go_home(self):
        widget = self.scroll_area.takeWidget()

        if type(widget.class_) == CartScreen:
            self.cart_menu = widget
        elif type(widget.class_) == AccountScreen:
            self.account_menu = widget
        elif type(widget.class_) == SettingsScreen:
            self.settings_menu = widget
        elif type(widget.class_) == InfoScreen:
            self.info_screen = widget

        self.scroll_area.setWidget(self.main_menu)

    def go_cart(self):
        widget = self.scroll_area.takeWidget()

        if type(widget.class_) == MainMenu:
            self.main_menu = widget
        elif type(widget.class_) == AccountScreen:
            self.account_menu = widget
        elif type(widget.class_) == SettingsScreen:
            self.settings_menu = widget
        elif type(widget.class_) == InfoScreen:
            self.info_screen = widget

        self.cart_menu.class_.change_tip()
        self.scroll_area.setWidget(self.cart_menu)

    def go_account(self):
        widget = self.scroll_area.takeWidget()

        if type(widget.class_) == MainMenu:
            self.main_menu = widget
        elif type(widget.class_) == CartScreen:
            self.cart_menu = widget
        elif type(widget.class_) == SettingsScreen:
            self.settings_menu = widget
        elif type(widget.class_) == InfoScreen:
            self.info_screen = widget

        self.scroll_area.setWidget(self.account_menu)

    def go_settings(self):
        widget = self.scroll_area.takeWidget()

        if type(widget.class_) == MainMenu:
            self.main_menu = widget
        elif type(widget.class_) == CartScreen:
            self.cart_menu = widget
        elif type(widget.class_) == AccountScreen:
            self.account_menu = widget
        elif type(widget.class_) == InfoScreen:
            self.info_screen = widget

        self.scroll_area.setWidget(self.settings_menu)

    def go_info(self):
        widget = self.scroll_area.takeWidget()

        if type(widget.class_) == MainMenu:
            self.main_menu = widget
        elif type(widget.class_) == CartScreen:
            self.cart_menu = widget
        elif type(widget.class_) == AccountScreen:
            self.account_menu = widget
        elif type(widget.class_) == SettingsScreen:
            self.settings_menu = widget

        self.scroll_area.setWidget(self.info_screen)


class NavigationDock(QWidget):
    connect_buttons_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_UI()

    def init_UI(self):
        # Change button names to icons
        self.home_button = QPushButton("Inicio", self)

        self.cart_button = QPushButton("Carrito", self)

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
    def __init__(self, class_, parent=None, *args):
        super().__init__(parent=parent)
        self.class_ = class_(*args, parent)
        self.navigation = NavigationDock(parent)

        vbox = QVBoxLayout()
        vbox.addWidget(self.class_)
        vbox.addWidget(self.navigation)

        self.setLayout(vbox)
