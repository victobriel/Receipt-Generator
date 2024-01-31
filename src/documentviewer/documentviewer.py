# Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from PySide6.QtWidgets import (QDialog, QFileDialog, QMainWindow)
from PySide6.QtCore import (QDir, QFile, QFileInfo, Slot)

from .ui_mainwindow import Ui_MainWindow
from .viewerfactory import ViewerFactory

class DocumentViewer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()

        self._currentDir = QDir()
        self._viewer = None

        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self.onActionOpenTriggered)

        self._factory = ViewerFactory(self.ui.viewArea, self)

    @Slot(int)
    def onActionOpenTriggered(self):
        fileDialog = QFileDialog(self, "Open Document",
                                 self._currentDir.absolutePath())
        while (fileDialog.exec() == QDialog.Accepted
               and not self.openFile(fileDialog.selectedFiles()[0])):
            pass

    @Slot(str)
    def openFile(self, fileName):
        file = QFile(fileName)
        if not file.exists():
            nf = QDir.toNativeSeparators(fileName)
            self.statusBar().showMessage(f"File {nf} could not be opened")
            return False

        fileInfo = QFileInfo(file)
        self._currentDir = fileInfo.dir()

        self._viewer = self._factory.viewer(file)
        if not self._viewer:
            nf = QDir.toNativeSeparators(fileName)
            self.statusBar().showMessage(f"File {nf} can't be opened.")
            return False

        self.ui.actionPrint.setEnabled(self._viewer.hasContent())
        self._viewer.printingEnabledChanged.connect(self.ui.actionPrint.setEnabled)
        self.ui.actionPrint.triggered.connect(self._viewer.print_)
        self._viewer.showMessage.connect(self.statusBar().showMessage)

        self._viewer.initViewer(self.ui.actionPrint)
        self.ui.scrollArea.setWidget(self._viewer.widget())
        return True
