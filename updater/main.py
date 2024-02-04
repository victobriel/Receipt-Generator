import sys
from PySide6.QtWidgets import QApplication
from updatewindow.updatewindow import UpdateWindow

if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: UpdateWindow = UpdateWindow(
        pid = sys.argv[1] if len(sys.argv) > 1 else None,
        freeze = False if (len(sys.argv) > 2 and sys.argv[2] == '--not-freeze') else True)
    app.exec()
