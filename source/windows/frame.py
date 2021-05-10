from PyQt5.QtWidgets import QMainWindow, QScrollArea

from .start import StartScreen


class AppFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("TimberShop App Prototype")
        self.setFixedSize(375, 612)

        # Screens & Menus
        self.start_screen = StartScreen(self)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.start_screen)

        self.setCentralWidget(self.scroll_area)

        self.show()
