import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont

from windows import AppFrame
from logic import UserManager, user


def main():
    app = QApplication([])
    app.setWindowIcon(QIcon("img/logo.png"))
    app.setFont(QFont("Corsiva Hebrew"))

    window = AppFrame()
    users = UserManager("data/users.csv")

    # Connecting signals
    window.start_screen.sign_in_signal.connect(users.login)
    window.start_screen.sign_up_signal.connect(users.register)
    users.signal_success_login.connect(window.sign_in)
    users.signal_failed_login.connect(window.start_screen.display_error)
    users.signal_failed_register.connect(window.start_screen.display_error)
    users.signal_success_register.connect(window.start_screen.display_error)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
