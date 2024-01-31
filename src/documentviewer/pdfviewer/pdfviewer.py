# Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from math import sqrt

from PySide6.QtWidgets import (QListView)
from PySide6.QtGui import QIcon, QPainter
from PySide6.QtCore import (QDir, QIODevice, QModelIndex,
                            QPointF, Slot)
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView, QPdfPageSelector

from ..abstractviewer import AbstractViewer
from .zoomselector import ZoomSelector

ZOOM_MULTIPLIER = sqrt(2.0)

class PdfViewer(AbstractViewer):

    def __init__(self):
        super().__init__()
        self.uiInitialized.connect(self.initPdfViewer)
        self._toolBar = None
        self._zoomSelector = None
        self._pageSelector = None
        self._document = None
        self._pdfView = None
        self._pages = None

    def init(self, file, parent, mainWindow):
        self._pdfView = QPdfView(parent)
        super().init(file, self._pdfView, mainWindow)
        self._document = QPdfDocument(self)

    def supportedMimeTypes(self):
        return ["application/pdf"]

    def initPdfViewer(self):
        self._toolBar = self.addToolBar("PDF")
        self._zoomSelector = ZoomSelector(self._toolBar)

        nav = self._pdfView.pageNavigator()
        self._pageSelector = QPdfPageSelector(self._toolBar)
        self._toolBar.insertWidget(self._uiAssets_print, self._pageSelector)
        self._pageSelector.setDocument(self._document)
        self._pageSelector.currentPageChanged.connect(self.pageSelected)
        nav.currentPageChanged.connect(self._pageSelector.setCurrentPage)

        self._toolBar.addSeparator()
        self._toolBar.addWidget(self._zoomSelector)

        actionZoomIn = self._toolBar.addAction("Zoom in")
        actionZoomIn.setToolTip("Increase zoom level")
        actionZoomIn.setIcon(QIcon(":/demos/documentviewer/images/zoom-in.png"))
        self._toolBar.addAction(actionZoomIn)
        actionZoomIn.triggered.connect(self.onActionZoomInTriggered)

        actionZoomOut = self._toolBar.addAction("Zoom out")
        actionZoomOut.setToolTip("Decrease zoom level")
        actionZoomOut.setIcon(QIcon(":/demos/documentviewer/images/zoom-out.png"))
        self._toolBar.addAction(actionZoomOut)
        actionZoomOut.triggered.connect(self.onActionZoomOutTriggered)

        self._zoomSelector.zoomModeChanged.connect(self._pdfView.setZoomMode)
        self._zoomSelector.zoomFactorChanged.connect(self._pdfView.setZoomFactor)
        self._zoomSelector.reset()

        self._pdfView.setDocument(self._document)
        self._pdfView.setPageMode(QPdfView.PageMode.MultiPage)

        self.openPdfFile()
        if not self._document.pageCount():
            return

        self._pages = QListView()
        self._pages.setModel(self._document.pageModel())

        self._pages.selectionModel().currentRowChanged.connect(self._currentRowChanged)
        self._pdfView.pageNavigator().currentPageChanged.connect(self._pageChanged)

    def viewerName(self):
        return "PdfViewer"

    @Slot(QModelIndex, QModelIndex)
    def _currentRowChanged(self, current, previous):
        if previous == current:
            return

        nav = self._pdfView.pageNavigator()
        row = current.row()
        if nav.currentPage() == row:
            return
        nav.jump(row, QPointF(), nav.currentZoom())

    @Slot(int)
    def _pageChanged(self, page):
        if self._pages.currentIndex().row() == page:
            return
        self._pages.setCurrentIndex(self._pages.model().index(page, 0))

    @Slot()
    def openPdfFile(self):
        self.disablePrinting()

        if self._file.open(QIODevice.ReadOnly):
            self._document.load(self._file)

        documentTitle = self._document.metaData(QPdfDocument.MetaDataField.Title)
        if not documentTitle:
            documentTitle = "PDF Viewer"
        self.statusMessage(documentTitle)
        self.pageSelected(0)

        file_name = QDir.toNativeSeparators(self._file.fileName())
        self.statusMessage(f"Opened PDF file {file_name}")
        self.maybeEnablePrinting()

    def hasContent(self):
        return self._document if self._document.pageCount() > 0 else False

    def supportsOverview(self):
        return True

    def printDocument(self, printer):
        if not self.hasContent():
            return

        painter = QPainter()
        painter.begin(printer)
        pageRect = printer.pageRect(QPrinter.Unit.DevicePixel).toRect()
        pageSize = pageRect.size()
        for i in range(0, self._document.pageCount()):
            if i > 0:
                printer.newPage()
            page = self._document.render(i, pageSize)
            painter.drawImage(pageRect, page)
        painter.end()

    @Slot(int)
    def pageSelected(self, page):
        nav = self._pdfView.pageNavigator()
        nav.jump(page, QPointF(), nav.currentZoom())

    @Slot()
    def onActionZoomInTriggered(self):
        self._pdfView.setZoomFactor(self._pdfView.zoomFactor() * ZOOM_MULTIPLIER)

    @Slot()
    def onActionZoomOutTriggered(self):
        self._pdfView.setZoomFactor(self._pdfView.zoomFactor() / ZOOM_MULTIPLIER)
