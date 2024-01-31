from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from ..ui.updatewindow.ui_updatewindow import Ui_UpdateWindow
import os, requests, webbrowser as wb

class UpdateWindow(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self._parent = parent
        self.ui: Ui_UpdateWindow = Ui_UpdateWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Procurando por atualizações...')

        self._disableDownload()
        # Signals
        self.ui.quit_btn.clicked.connect(self.close)
        self.ui.download_btn.clicked.connect(self._download)
        self._startChecking()

    def closeEvent(self, event) -> None:
        # self._parent.setWindowFlags(Qt.WindowFlags())
        self._parent.show()
        event.accept()

    def _startChecking(self) -> None:
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
            self._addMessage('Nenhuma atualização disponível')
            self.close()

    def _addMessage(self, message: str) -> None:
        self.ui.messages_list.addItem(message)

    def _enableDownload(self) -> None:
        self.ui.download_btn.setEnabled(True)

    def _disableDownload(self) -> None:
        self.ui.download_btn.setEnabled(False)

    def _download(self) -> None:
        pass
