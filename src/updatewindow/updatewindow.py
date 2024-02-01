from PySide6.QtWidgets import QDialog
from ..ui.updatewindow.ui_updatewindow import Ui_UpdateWindow
import os,requests,webbrowser as wb

class UpdateWindow(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self._parent = parent
        self.ui: Ui_UpdateWindow = Ui_UpdateWindow()
        self.ui.setupUi(self)

        self._disableDownload()
        # Signals
        self.ui.quit_btn.clicked.connect(self.close)
        self.ui.download_btn.clicked.connect(self._download)

    def closeEvent(self, event) -> None:
        # self._parent.setWindowFlags(Qt.WindowFlags())
        self._parent.show()
        event.accept()

    def _checkForUpdate(self) -> None:
        self.setWindowTitle('Procurando por atualizações...')
        self._clearMessages()
        self._addMessage("Procurando por atualizações...")

        version: str = os.getenv('VERSION')
        self._addMessage(f'Versão atual: {version}')
        githubData: dict = requests.get('https://api.github.com/repos/victobriel/receipt-generator/releases/latest').json()
        githubVersion: str = githubData['tag_name'].replace('v', '')
        self._addMessage(f'Versão mais recente: {githubVersion}')
        if version != githubVersion:
            self.setWindowTitle('Atualização disponível')
            _m: str = 'Baixe a versão mais recente do aplicativo'
            self._addMessage(_m)
            self._enableDownload()
        else:
            self._parent.statusBar().showMessage('Nenhuma atualização disponível', 5000)
            self.close()

    def _addMessage(self, message: str) -> None:
        self.ui.messages_list.addItem(message)

    def _enableDownload(self) -> None:
        self.ui.download_btn.setEnabled(True)

    def _disableDownload(self) -> None:
        self.ui.download_btn.setEnabled(False)

    def _download(self) -> None:
        pass

    def _clearMessages(self) -> None:
        self.ui.messages_list.clear()
