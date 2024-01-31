# Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from PySide6.QtCore import QObject

from PySide6.QtWidgets import (QDialog)
from PySide6.QtCore import Signal, Slot
from PySide6.QtPrintSupport import QPrinter, QPrintDialog

MENU_NAME = "qtFileMenu"

class AbstractViewer(QObject):

    uiInitialized = Signal()
    printingEnabledChanged = Signal(bool)
    showMessage = Signal(str, int)

    def __init__(self):
        super().__init__()
        self._file = None
        self._widget = None
        self._menus = []
        self._toolBars = []
        self._printingEnabled = False

    def __del__(self):
        self.cleanup()

    def viewerName(self):
        return ""

    def supportedMimeTypes():
        return []

    def init(self, file, widget, mainWindow):
        self._file = file
        self._widget = widget
        self._uiAssets_mainWindow = mainWindow

    def hasContent(self):
        return False

    def supportsOverview(self):
        return False

    def widget(self):
        return self._widget

    def mainWindow(self):
        return self._uiAssets_mainWindow

    def maybeEnablePrinting(self):
        self.maybeSetPrintingEnabled(True)

    def disablePrinting(self):
        self.maybeSetPrintingEnabled(False)

    def isDefaultViewer(self):
        return False

    def viewer(self):
        return self

    def statusMessage(self, message, type="", timeout=8000):
        msg = self.viewerName()
        if type:
            msg += "/" + type
        msg += ": " + message
        self.showMessage.emit(msg, timeout)

    def addToolBar(self, title):
        bar = self.mainWindow().addToolBar(title)
        name = title.replace(' ', '')
        bar.setObjectName(name)
        self._toolBars.append(bar)
        return bar

    def cleanup(self):
        # delete all objects created by the viewer which need to be displayed
        # and therefore parented on MainWindow
        if self._file:
            self._file = None
        self._menus.clear()
        self._toolBars.clear()

    @Slot()
    def print_(self):
        type = "Printing"
        if not self.hasContent():
            self.statusMessage("No content to print.", type)
            return
        printer = QPrinter(QPrinter.HighResolution)
        dlg = QPrintDialog(printer, self.mainWindow())
        dlg.setWindowTitle("Print Document")
        if dlg.exec() == QDialog.Accepted:
            self.printDocument(printer)
        else:
            self.statusMessage("Printing canceled!", type)
            return
        state = printer.printerState()
        message = self.viewerName() + " : "
        if state == QPrinter.PrinterState.Aborted:
            message += "Printing aborted."
        elif state == QPrinter.PrinterState.Active:
            message += "Printing active."
        elif state == QPrinter.PrinterState.Idle:
            message += "Printing completed."
        elif state == QPrinter.PrinterState.Error:
            message += "Printing error."
        self.statusMessage(message, type)

    def maybeSetPrintingEnabled(self, enabled):
        if enabled == self._printingEnabled:
            return
        self._printingEnabled = enabled
        self.printingEnabledChanged.emit(enabled)

    def initViewer(self, print):
        self._uiAssets_print = print
        self.uiInitialized.emit()
