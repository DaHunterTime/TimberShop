import sys

from PyQt5.QtWidgets import QApplication

from windows import AppFrame


def main():
    app = QApplication([])

    window = AppFrame()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
