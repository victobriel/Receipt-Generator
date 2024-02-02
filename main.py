import sys
from PySide6.QtWidgets import QApplication
from src.mainwindow.mainwindow import MainWindow as Application

if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    main: Application = Application()
    main.show()
    app.exec()
