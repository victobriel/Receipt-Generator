# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowQmsrtO.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QScrollArea, QSizePolicy,
    QToolBar, QVBoxLayout, QWidget)
from .rc_documentviewer import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(983, 602)
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionPrint.setEnabled(False)
        icon = QIcon()
        iconThemeName = u"document-print"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/demos/documentviewer/images/print.png", QSize(), QIcon.Normal, QIcon.Off)

        self.actionPrint.setIcon(icon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon1 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionQuit.setIcon(icon1)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/demos/documentviewer/images/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.viewArea = QWidget(self.centralwidget)
        self.viewArea.setObjectName(u"viewArea")
        self.verticalLayout_2 = QVBoxLayout(self.viewArea)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.viewArea)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 945, 530))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.viewArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)

        self.mainToolBar.addAction(self.actionOpen)
        self.mainToolBar.addAction(self.actionPrint)
        self.mainToolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Document Viewer", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
#if QT_CONFIG(tooltip)
        self.actionPrint.setToolTip(QCoreApplication.translate("MainWindow", u"Print current file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPrint.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(tooltip)
        self.actionQuit.setToolTip(QCoreApplication.translate("MainWindow", u"Quit the application", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Open File", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.mainToolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

