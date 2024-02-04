from PySide6.QtWidgets import QMainWindow
from ui.updatewindow.ui_updatewindow import Ui_UpdateWindow
from updater.updater import Updater
import sys,psutil

class UpdateWindow(QMainWindow):
    def __init__(self, pid: str, freeze: bool, parent=None) -> None:
        super().__init__(parent)
        self._freeze: bool = freeze
        self._pid: str = pid
        # UI
        self.ui: Ui_UpdateWindow = Ui_UpdateWindow()
        self.ui.setupUi(self)
        # Updater
        self._updater = Updater(self)
        # Signals
        self.ui.quit_btn.clicked.connect(self.close)
        self.ui.download_btn.clicked.connect(self._download)
        self._updater.setTotalProgress.connect(self.setProgressBarMax)
        self._updater.setCurrentProgress.connect(self.setProgressBar)
        self._updater.addMessage.connect(self.addMessage)
        # Start
        self._disableDownload()
        self.resetProgressBar()
        self._checkForUpdate()

    def _checkForUpdate(self) -> None:
        self._clearMessages()
        self.setWindowTitle('Procurando por atualizações...')
        update: bool = self._updater.check()
        if not update:
            if not self._freeze:
                return sys.exit()
            self.show()
            self.resize(360, 320)
            self.setWindowTitle('Nenhuma atualização disponível')
            _m: str = 'Você está atualizado.'
            self.addMessage(_m)
            self._updater.runApp()
        else:
            self.show()
            self.resize(360, 320)
            self.setWindowTitle('Atualização disponível')
            _m: str = 'Baixe a versão mais recente do aplicativo'
            self.addMessage(_m)
            self._enableDownload()

    def _download(self) -> None:
        self.setWindowTitle('Baixando atualização...')
        download: bool = self._updater.download()
        self.addMessage('Baixando atualização...')
        if download:
            self.setWindowTitle('Atualização baixada')
            self.addMessage('Atualização baixada com sucesso')
            self._disableDownload()
            self.addMessage('Fechando Receipt Generator...')
            while self._checkPID():
                pass
            self._install()
        else:
            self.setWindowTitle('Erro ao baixar atualização')
            self.addMessage('Erro ao baixar atualização')

    def _checkPID(self) -> bool:
        if not psutil.pid_exists(int(self._pid)):
            return False
        else:
            p = psutil.Process(int(self._pid))
            p.terminate()
        return True

    def _install(self) -> None:
        self.setWindowTitle('Instalando atualização...')
        install: bool = self._updater.install()
        if install:
            self.setWindowTitle('Atualização instalada')
            self.addMessage('Atualização instalada com sucesso')
            self._updater.runApp()
        else:
            self.setWindowTitle('Erro ao instalar atualização')

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
