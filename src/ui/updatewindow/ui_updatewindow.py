# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_updatewindowqthgfc.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGroupBox,
    QHBoxLayout, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from .assets_rc import *

class Ui_UpdateWindow(object):
    def setupUi(self, UpdateWindow):
        if not UpdateWindow.objectName():
            UpdateWindow.setObjectName(u"UpdateWindow")
        UpdateWindow.resize(273, 168)
        icon = QIcon()
        icon.addFile(u":/logo/assets/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        UpdateWindow.setWindowIcon(icon)
        UpdateWindow.setStyleSheet(u"* {\n"
"font-family: 'Roboto';\n"
"}\n"
"QDialog {\n"
"background-color:#303440;\n"
"}\n"
"QGroupBox {\n"
"background-color:#3d4454;\n"
"color:#dae0ec;\n"
"border:1px solid #616877;\n"
"}\n"
"QPushButton {\n"
"color:#fff;\n"
"background-color:#303440;\n"
"border:1px solid #616877;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#565b6b;\n"
"}\n"
"QListWidget {\n"
"background-color:#303440;\n"
"gridline-color:#636870;\n"
"}\n"
"QListView::item {\n"
"color:#fff;\n"
"background-color:#1b2125;\n"
"min-height:25px;\n"
"}\n"
"QListView::item:selected {\n"
"background-color:#5b9aff;\n"
"}")
        self.verticalLayout = QVBoxLayout(UpdateWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.messages_list = QListWidget(UpdateWindow)
        QListWidgetItem(self.messages_list)
        QListWidgetItem(self.messages_list)
        QListWidgetItem(self.messages_list)
        QListWidgetItem(self.messages_list)
        self.messages_list.setObjectName(u"messages_list")
        self.messages_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.messages_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.messages_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.messages_list.setProperty("showDropIndicator", False)
        self.messages_list.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout.addWidget(self.messages_list)

        self.updateProgressBar = QProgressBar(UpdateWindow)
        self.updateProgressBar.setObjectName(u"updateProgressBar")
        self.updateProgressBar.setMinimumSize(QSize(0, 25))
        self.updateProgressBar.setMaximumSize(QSize(16777215, 25))
        self.updateProgressBar.setValue(2)
        self.updateProgressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.updateProgressBar)

        self.groupBox = QGroupBox(UpdateWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"padding-top:0;")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.download_btn = QPushButton(self.groupBox)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setEnabled(False)
        self.download_btn.setMinimumSize(QSize(90, 20))
        self.download_btn.setMaximumSize(QSize(90, 20))

        self.horizontalLayout.addWidget(self.download_btn)

        self.quit_btn = QPushButton(self.groupBox)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setMinimumSize(QSize(79, 20))
        self.quit_btn.setMaximumSize(QSize(70, 20))

        self.horizontalLayout.addWidget(self.quit_btn)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(UpdateWindow)

        QMetaObject.connectSlotsByName(UpdateWindow)
    # setupUi

    def retranslateUi(self, UpdateWindow):
        UpdateWindow.setWindowTitle(QCoreApplication.translate("UpdateWindow", u"Procurando por atualiza\u00e7\u00f5es...", None))

        __sortingEnabled = self.messages_list.isSortingEnabled()
        self.messages_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.messages_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("UpdateWindow", u"1", None));
        ___qlistwidgetitem1 = self.messages_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("UpdateWindow", u"2", None));
        ___qlistwidgetitem2 = self.messages_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("UpdateWindow", u"3", None));
        ___qlistwidgetitem3 = self.messages_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("UpdateWindow", u"4", None));
        self.messages_list.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle("")
        self.download_btn.setText(QCoreApplication.translate("UpdateWindow", u"Baixar", None))
        self.quit_btn.setText(QCoreApplication.translate("UpdateWindow", u"Sair", None))
    # retranslateUi

