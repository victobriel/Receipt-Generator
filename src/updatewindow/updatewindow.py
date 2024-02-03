from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from ..ui.updatewindow.ui_updatewindow import Ui_UpdateWindow
from ..updater.updater import Updater

class UpdateWindow(QDialog):

    appDownloaded = Signal(str)

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self._parent = parent
        self.ui: Ui_UpdateWindow = Ui_UpdateWindow()
        self.ui.setupUi(self)
        self._updater = Updater(self)
        self._disableDownload()
        self.resetProgressBar()
        # Signals
        self.ui.quit_btn.clicked.connect(self.close)
        self.ui.download_btn.clicked.connect(self._download)
        self._updater.setTotalProgress.connect(self.setProgressBarMax)
        self._updater.setCurrentProgress.connect(self.setProgressBar)
        self._updater.addMessage.connect(self.addMessage)

    def checkForUpdate(self, freeze: bool) -> None:
        self._clearMessages()
        self.setWindowTitle('Procurando por atualizações...')
        update: bool = self._updater.check()
        if update:
            self.show()
            self.resize(360, 320)
            self.setWindowTitle('Atualização disponível')
            _m: str = 'Baixe a versão mais recente do aplicativo'
            self.addMessage(_m)
            self._enableDownload()
        else:
            if not freeze:
                self.close()
            else:
                self.show()
                self.resize(360, 320)
                self.setWindowTitle('Você está atualizado')
                _m: str = 'Você já está utilizando a versão mais recente do aplicativo'
                self.addMessage(_m)

    def _download(self) -> None:
        self.setWindowTitle('Baixando atualização...')
        download: bool = self._updater.download()
        if download:
            self.setWindowTitle('Atualização baixada')
            self.addMessage('Atualização baixada com sucesso')
            self._disableDownload()
            self.appDownloaded.emit(self._updater._file)
        else:
            self.setWindowTitle('Erro ao baixar atualização')

    def addMessage(self, message: str) -> None:
        self.ui.messages_list.addItem(message)

    def _enableDownload(self) -> None:
        self.ui.download_btn.setEnabled(True)

    def _disableDownload(self) -> None:
        self.ui.download_btn.setEnabled(False)

    def _clearMessages(self) -> None:
        self.ui.messages_list.clear()

    def getProgressBar(self) -> int:
        return self.ui.updateProgressBar.value()

    def setProgressBar(self, value: int, max=False) -> None:
        if max:
            self.ui.updateProgressBar.setValue(self.ui.updateProgressBar.maximum())
        else:
            self.ui.updateProgressBar.setValue(value)

    def setProgressBarMax(self, value: int) -> None:
        self.ui.updateProgressBar.setMaximum(value)

    def resetProgressBar(self) -> None:
        self.ui.updateProgressBar.setValue(0)
