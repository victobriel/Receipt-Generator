from PySide6.QtWidgets import QMainWindow,QMessageBox
from PySide6.QtCore import Slot
from ui.updatewindow.ui_updatewindow import Ui_UpdateWindow
from updater.updater import Updater
import sys,psutil

class UpdateWindow(QMainWindow):
    def __init__(self, pid: str, freeze: bool, parent=None) -> None:
        super().__init__(parent)
        self._pid: str = pid
        self._freeze: bool = freeze
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
                sys.exit()
            else:
                self.show()
                self.resize(360, 320)
                self.setWindowTitle('Nenhuma atualização disponível')
                _m: str = 'Você está atualizado.'
                self.addMessage(_m)
        else:
            self.show()
            self.resize(360, 320)
            self.setWindowTitle('Atualização disponível')
            _m: str = 'Baixe a versão mais recente do aplicativo'
            self.addMessage(_m)
            self._enableDownload()

    @Slot()
    def _download(self) -> None:
        self.setWindowTitle('Baixando atualização...')
        download: bool = self._updater.download()
        self.addMessage('Baixando atualização...')
        if download:
            self.setWindowTitle('Atualização baixada')
            self.addMessage('Atualização baixada com sucesso')
            self._disableDownload()
            if self._pid != None:
                if self._checkPID():
                    self._b = QMessageBox()
                    self._b.setIcon(QMessageBox.Information)
                    self._b.setWindowTitle("Atualização")
                    self._b.setText("A atualização foi baixada e detectamos que o Receipt Generator está aberto.")
                    self._b.setInformativeText("Clique em OK para fechá-lo e instalar a atualização")
                    self._b.setStandardButtons(QMessageBox.Ok)
                    self._b.exec_()
                    if self._b.clickedButton() == self._b.button(QMessageBox.Ok):
                        p = psutil.Process(int(self._pid))
                        p.terminate()
            self._install()
        else:
            self.setWindowTitle('Erro ao baixar atualização')
            self.addMessage('Erro ao baixar atualização')

    def _checkPID(self) -> bool:
        if psutil.pid_exists(int(self._pid)):
            return True
        return False

    def _install(self) -> None:
        self.setWindowTitle('Instalando atualização...')
        install: bool = self._updater.install()
        if install:
            self.setWindowTitle('Atualização instalada')
            self.addMessage('Atualização instalada com sucesso')
            self._updater.runApp()
        else:
            self.setWindowTitle('Erro ao instalar atualização')

    @Slot(str)
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

    @Slot(int, bool)
    def setProgressBar(self, value: int, max=False) -> None:
        if max:
            self.ui.updateProgressBar.setValue(self.ui.updateProgressBar.maximum())
        else:
            self.ui.updateProgressBar.setValue(value)

    @Slot(int)
    def setProgressBarMax(self, value: int) -> None:
        self.ui.updateProgressBar.setMaximum(value)

    def resetProgressBar(self) -> None:
        self.ui.updateProgressBar.setValue(0)
