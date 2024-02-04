import sys
from PySide6.QtWidgets import QApplication
from updatewindow.updatewindow import UpdateWindow

if __name__ == "__main__":
    pid = sys.argv[1]
    freeze: bool = True if (sys.argv[2] == '--freeze') else False
    app: QApplication = QApplication(sys.argv)
    window: UpdateWindow = UpdateWindow(pid=pid, freeze=freeze)
    # window.show()
    app.exec()
