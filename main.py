import sys
from src.mainwindow.mainwindow import MainWindow as Application
from PySide6 import QtWidgets

if __name__ == "__main__":
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    main: Application = Application()
    main.show()
    app.exec()
