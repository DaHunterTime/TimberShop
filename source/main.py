import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont

from windows import AppFrame


def main():
    app = QApplication([])
    app.setWindowIcon(QIcon("img/logo.png"))
    app.setFont(QFont("Corsiva Hebrew"))

    window = AppFrame()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
