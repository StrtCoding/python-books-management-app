from PySide2.QtWidgets import QApplication
from controllers.main_window import ListBookWindow


if __name__ == "__main__":
    app = QApplication()
    window = ListBookWindow()
    window.show()

    app.exec_()