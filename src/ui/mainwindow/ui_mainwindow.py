# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindowJIKUHK.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QScrollBar,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)
from .assets_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(976, 920)
        icon = QIcon()
        icon.addFile(u":/app/assets/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"* {\n"
"font-family: 'Roboto';\n"
"}\n"
"QMainWindow {\n"
"background-color:#303440;\n"
"}\n"
"QMenuBar {\n"
"color:#fff;\n"
"background-color:#3d4454;\n"
"}\n"
"QMenu:hover {\n"
"color:yellow;\n"
"background-color:red;\n"
"}\n"
"QGroupBox {\n"
"background-color:#3d4454;\n"
"color:#dae0ec;\n"
"border:1px solid #616877;\n"
"padding-top: 15px;\n"
"}\n"
"QPushButton {\n"
"color:#fff;\n"
"background-color:#303440;\n"
"border:1px solid #616877;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#565b6b;\n"
"}\n"
"QComboBox {\n"
"color:#fff;\n"
"background-color:#303440;\n"
"outline:none;\n"
"padding:0 3px;\n"
"}\n"
"QLineEdit,\n"
"QDateEdit {\n"
"color: #fff;\n"
"background-color:#1b2125;\n"
"border:1px solid #3e464d;\n"
"padding:0 3px;\n"
"}\n"
"QLineEdit:focus {\n"
"border:1px solid #5b9aff;\n"
"}\n"
"QLabel {\n"
"color:#f4fbff;\n"
"padding-left: 1px;\n"
"}\n"
"Line {\n"
"background-color:#636870;\n"
"}\n"
"QCheckBox {\n"
"color:#fff;\n"
"}\n"
"QPlainTextEdit {\n"
"background-color:#303440;\n"
"color:#fff;\n"
"}\n"
""
                        "QStatusBar {\n"
"color:#fff;\n"
"}\n"
"QTableWidget {\n"
"background-color:#303440;\n"
"gridline-color:#636870;\n"
"}\n"
"QHeaderView {\n"
"background-color:#303440;\n"
"}\n"
"QHeaderView::section{\n"
"background-color:#303440;\n"
"color:#fff;\n"
"border:1px solid #636870;\n"
"border-top:none;\n"
"border-left:none;\n"
"}\n"
"QTableView::item {\n"
"color:#fff;\n"
"background-color:#1b2125;\n"
"}\n"
"QTableView::item:selected {\n"
"background-color:#5b9aff;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"border-top: 1px solid #5b9aff;\n"
"}")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        icon1 = QIcon()
        iconThemeName = u"document-print"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/print/assets/print-black-26.png", QSize(), QIcon.Normal, QIcon.Off)

        self.actionPrint.setIcon(icon1)
        self.actionPrint.setMenuRole(QAction.NoRole)
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionPreview = QAction(MainWindow)
        self.actionPreview.setObjectName(u"actionPreview")
        icon2 = QIcon()
        iconThemeName = u"document-print-preview"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u":/print/assets/preview-black-30.png", QSize(), QIcon.Normal, QIcon.Off)

        self.actionPreview.setIcon(icon2)
        self.actionPreview.setMenuRole(QAction.NoRole)
        self.actionCheckForUpdates = QAction(MainWindow)
        self.actionCheckForUpdates.setObjectName(u"actionCheckForUpdates")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalGroupBox_1 = QGroupBox(self.centralwidget)
        self.verticalGroupBox_1.setObjectName(u"verticalGroupBox_1")
        self.verticalGroupBox_1.setMinimumSize(QSize(450, 0))
        self.verticalGroupBox_1.setStyleSheet(u"#groupBox_7 {\n"
"border:none;\n"
"padding-top:0;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.verticalGroupBox_1)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalGroupBox_1_0 = QGroupBox(self.verticalGroupBox_1)
        self.verticalGroupBox_1_0.setObjectName(u"verticalGroupBox_1_0")
        self.verticalLayout_24 = QVBoxLayout(self.verticalGroupBox_1_0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.qTableViewLayout = QVBoxLayout()
        self.qTableViewLayout.setObjectName(u"qTableViewLayout")
        self.areaQTableView = QWidget(self.verticalGroupBox_1_0)
        self.areaQTableView.setObjectName(u"areaQTableView")

        self.qTableViewLayout.addWidget(self.areaQTableView)


        self.verticalLayout_24.addLayout(self.qTableViewLayout)

        self.rem_serv_btn = QPushButton(self.verticalGroupBox_1_0)
        self.rem_serv_btn.setObjectName(u"rem_serv_btn")
        self.rem_serv_btn.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        self.rem_serv_btn.setFont(font)
        self.rem_serv_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_24.addWidget(self.rem_serv_btn)

        self.verticalGroupBox_1_0_1 = QGroupBox(self.verticalGroupBox_1_0)
        self.verticalGroupBox_1_0_1.setObjectName(u"verticalGroupBox_1_0_1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalGroupBox_1_0_1.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_1_0_1.setSizePolicy(sizePolicy)
        self.verticalGroupBox_1_0_1.setMaximumSize(QSize(16777215, 190))
        self.verticalGroupBox_1_0_1.setCheckable(False)
        self.verticalLayout_23 = QVBoxLayout(self.verticalGroupBox_1_0_1)
        self.verticalLayout_23.setSpacing(4)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_1_0_1_1 = QVBoxLayout()
        self.verticalLayout_1_0_1_1.setSpacing(4)
        self.verticalLayout_1_0_1_1.setObjectName(u"verticalLayout_1_0_1_1")
        self.description_label = QLabel(self.verticalGroupBox_1_0_1)
        self.description_label.setObjectName(u"description_label")
        sizePolicy.setHeightForWidth(self.description_label.sizePolicy().hasHeightForWidth())
        self.description_label.setSizePolicy(sizePolicy)

        self.verticalLayout_1_0_1_1.addWidget(self.description_label)

        self.prod_desc_edit = QLineEdit(self.verticalGroupBox_1_0_1)
        self.prod_desc_edit.setObjectName(u"prod_desc_edit")
        self.prod_desc_edit.setMinimumSize(QSize(0, 35))
        self.prod_desc_edit.setFont(font)
        self.prod_desc_edit.setStyleSheet(u"")
        self.prod_desc_edit.setClearButtonEnabled(True)

        self.verticalLayout_1_0_1_1.addWidget(self.prod_desc_edit)


        self.verticalLayout_23.addLayout(self.verticalLayout_1_0_1_1)

        self.horizontalLayout_1_0_1_0 = QHBoxLayout()
        self.horizontalLayout_1_0_1_0.setObjectName(u"horizontalLayout_1_0_1_0")
        self.verticalLayout_1_0_1_0_1 = QVBoxLayout()
        self.verticalLayout_1_0_1_0_1.setSpacing(4)
        self.verticalLayout_1_0_1_0_1.setObjectName(u"verticalLayout_1_0_1_0_1")
        self.value_label = QLabel(self.verticalGroupBox_1_0_1)
        self.value_label.setObjectName(u"value_label")
        sizePolicy.setHeightForWidth(self.value_label.sizePolicy().hasHeightForWidth())
        self.value_label.setSizePolicy(sizePolicy)

        self.verticalLayout_1_0_1_0_1.addWidget(self.value_label)

        self.horizontalLayout_1_0_1_0_1_0 = QHBoxLayout()
        self.horizontalLayout_1_0_1_0_1_0.setSpacing(0)
        self.horizontalLayout_1_0_1_0_1_0.setObjectName(u"horizontalLayout_1_0_1_0_1_0")
        self.prod_valu_edit = QLineEdit(self.verticalGroupBox_1_0_1)
        self.prod_valu_edit.setObjectName(u"prod_valu_edit")
        self.prod_valu_edit.setMinimumSize(QSize(0, 35))
        self.prod_valu_edit.setFont(font)
        self.prod_valu_edit.setStyleSheet(u"")

        self.horizontalLayout_1_0_1_0_1_0.addWidget(self.prod_valu_edit)

        self.prod_valu_scro = QScrollBar(self.verticalGroupBox_1_0_1)
        self.prod_valu_scro.setObjectName(u"prod_valu_scro")
        self.prod_valu_scro.setMaximumSize(QSize(20, 35))
        self.prod_valu_scro.setMinimum(-999999999)
        self.prod_valu_scro.setMaximum(0)
        self.prod_valu_scro.setPageStep(1)
        self.prod_valu_scro.setValue(0)

        self.horizontalLayout_1_0_1_0_1_0.addWidget(self.prod_valu_scro)


        self.verticalLayout_1_0_1_0_1.addLayout(self.horizontalLayout_1_0_1_0_1_0)


        self.horizontalLayout_1_0_1_0.addLayout(self.verticalLayout_1_0_1_0_1)

        self.verticalLayout_1_0_1_0_0 = QVBoxLayout()
        self.verticalLayout_1_0_1_0_0.setSpacing(4)
        self.verticalLayout_1_0_1_0_0.setObjectName(u"verticalLayout_1_0_1_0_0")
        self.quantity_label = QLabel(self.verticalGroupBox_1_0_1)
        self.quantity_label.setObjectName(u"quantity_label")
        sizePolicy.setHeightForWidth(self.quantity_label.sizePolicy().hasHeightForWidth())
        self.quantity_label.setSizePolicy(sizePolicy)

        self.verticalLayout_1_0_1_0_0.addWidget(self.quantity_label)

        self.prod_quant_spin = QSpinBox(self.verticalGroupBox_1_0_1)
        self.prod_quant_spin.setObjectName(u"prod_quant_spin")
        self.prod_quant_spin.setMinimumSize(QSize(0, 35))
        self.prod_quant_spin.setFont(font)
        self.prod_quant_spin.setStyleSheet(u"")
        self.prod_quant_spin.setMinimum(1)

        self.verticalLayout_1_0_1_0_0.addWidget(self.prod_quant_spin)


        self.horizontalLayout_1_0_1_0.addLayout(self.verticalLayout_1_0_1_0_0)


        self.verticalLayout_23.addLayout(self.horizontalLayout_1_0_1_0)

        self.add_serv_btn = QPushButton(self.verticalGroupBox_1_0_1)
        self.add_serv_btn.setObjectName(u"add_serv_btn")
        self.add_serv_btn.setMinimumSize(QSize(0, 35))
        self.add_serv_btn.setFont(font)
        self.add_serv_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.add_serv_btn)


        self.verticalLayout_24.addWidget(self.verticalGroupBox_1_0_1)

        self.horizontalGroupBox_1_0_0 = QGroupBox(self.verticalGroupBox_1_0)
        self.horizontalGroupBox_1_0_0.setObjectName(u"horizontalGroupBox_1_0_0")
        sizePolicy.setHeightForWidth(self.horizontalGroupBox_1_0_0.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_1_0_0.setSizePolicy(sizePolicy)
        self.horizontalGroupBox_1_0_0.setStyleSheet(u"QGroupBox{\n"
"padding-top:0;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalGroupBox_1_0_0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.total_value_label = QLabel(self.horizontalGroupBox_1_0_0)
        self.total_value_label.setObjectName(u"total_value_label")
        self.total_value_label.setFont(font)
        self.total_value_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.total_value_label)

        self.horizontalLayout_1_0_0_1 = QHBoxLayout()
        self.horizontalLayout_1_0_0_1.setSpacing(0)
        self.horizontalLayout_1_0_0_1.setObjectName(u"horizontalLayout_1_0_0_1")
        self.currency_line_edit = QLineEdit(self.horizontalGroupBox_1_0_0)
        self.currency_line_edit.setObjectName(u"currency_line_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.currency_line_edit.sizePolicy().hasHeightForWidth())
        self.currency_line_edit.setSizePolicy(sizePolicy1)
        self.currency_line_edit.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.currency_line_edit.setFont(font1)
        self.currency_line_edit.setStyleSheet(u"color:#5b9aff;\n"
"border-radius:15px;\n"
"border:1px solid #5b9aff;\n"
"background-color:transparent;")
        self.currency_line_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_1_0_0_1.addWidget(self.currency_line_edit)

        self.currency_btn = QPushButton(self.horizontalGroupBox_1_0_0)
        self.currency_btn.setObjectName(u"currency_btn")
        self.currency_btn.setMinimumSize(QSize(0, 30))
        self.currency_btn.setFont(font1)
        self.currency_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.currency_btn.setStyleSheet(u"QPushButton {\n"
"color:#fff;\n"
"border-radius:15px;\n"
"border:1px solid #5b9aff;\n"
"background-color:#5b9aff;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:#82b3ff;\n"
"}")

        self.horizontalLayout_1_0_0_1.addWidget(self.currency_btn)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_1_0_0_1)

        self.total_value_lbl = QLabel(self.horizontalGroupBox_1_0_0)
        self.total_value_lbl.setObjectName(u"total_value_lbl")
        self.total_value_lbl.setMinimumSize(QSize(80, 0))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.total_value_lbl.setFont(font2)
        self.total_value_lbl.setStyleSheet(u"")
        self.total_value_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.total_value_lbl)


        self.verticalLayout_24.addWidget(self.horizontalGroupBox_1_0_0)


        self.verticalLayout_21.addWidget(self.verticalGroupBox_1_0)

        self.verticalGroupBox_1_1 = QGroupBox(self.verticalGroupBox_1)
        self.verticalGroupBox_1_1.setObjectName(u"verticalGroupBox_1_1")
        sizePolicy.setHeightForWidth(self.verticalGroupBox_1_1.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_1_1.setSizePolicy(sizePolicy)
        self.verticalGroupBox_1_1.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.verticalGroupBox_1_1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.receipt_obs_edit = QPlainTextEdit(self.verticalGroupBox_1_1)
        self.receipt_obs_edit.setObjectName(u"receipt_obs_edit")
        self.receipt_obs_edit.setMaximumSize(QSize(16777215, 50))
        self.receipt_obs_edit.setFont(font)
        self.receipt_obs_edit.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.receipt_obs_edit)


        self.verticalLayout_21.addWidget(self.verticalGroupBox_1_1)


        self.gridLayout.addWidget(self.verticalGroupBox_1, 0, 2, 1, 1)

        self.verticalGroupBox_0 = QGroupBox(self.centralwidget)
        self.verticalGroupBox_0.setObjectName(u"verticalGroupBox_0")
        self.verticalGroupBox_0.setMinimumSize(QSize(450, 0))
        self.verticalGroupBox_0.setStyleSheet(u"#verticalGroupBox {\n"
"border:none;\n"
"padding-top:0;\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.verticalGroupBox_0)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalGroupBox_0_0 = QGroupBox(self.verticalGroupBox_0)
        self.verticalGroupBox_0_0.setObjectName(u"verticalGroupBox_0_0")
        self.verticalGroupBox_0_0.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.verticalGroupBox_0_0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_0_0_1 = QVBoxLayout()
        self.verticalLayout_0_0_1.setSpacing(4)
        self.verticalLayout_0_0_1.setObjectName(u"verticalLayout_0_0_1")
        self.company_label = QLabel(self.verticalGroupBox_0_0)
        self.company_label.setObjectName(u"company_label")
        sizePolicy.setHeightForWidth(self.company_label.sizePolicy().hasHeightForWidth())
        self.company_label.setSizePolicy(sizePolicy)

        self.verticalLayout_0_0_1.addWidget(self.company_label)

        self.comp_edit = QLineEdit(self.verticalGroupBox_0_0)
        self.comp_edit.setObjectName(u"comp_edit")
        self.comp_edit.setMinimumSize(QSize(0, 35))
        self.comp_edit.setFont(font)
        self.comp_edit.setStyleSheet(u"")
        self.comp_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_0_1.addWidget(self.comp_edit)


        self.verticalLayout_22.addLayout(self.verticalLayout_0_0_1)

        self.horizontalLayout_0_0_0 = QHBoxLayout()
        self.horizontalLayout_0_0_0.setObjectName(u"horizontalLayout_0_0_0")
        self.verticalGroupBox_0_0_0_1 = QVBoxLayout()
        self.verticalGroupBox_0_0_0_1.setSpacing(4)
        self.verticalGroupBox_0_0_0_1.setObjectName(u"verticalGroupBox_0_0_0_1")
        self.verticalLayout_0_0_0_1_0 = QVBoxLayout()
        self.verticalLayout_0_0_0_1_0.setSpacing(4)
        self.verticalLayout_0_0_0_1_0.setObjectName(u"verticalLayout_0_0_0_1_0")
        self.date_label = QLabel(self.verticalGroupBox_0_0)
        self.date_label.setObjectName(u"date_label")
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        self.date_label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_0_0_0_1_0.addWidget(self.date_label)

        self.date_edit = QDateEdit(self.verticalGroupBox_0_0)
        self.date_edit.setObjectName(u"date_edit")
        self.date_edit.setMinimumSize(QSize(0, 35))
        self.date_edit.setFont(font)
        self.date_edit.setWrapping(False)
        self.date_edit.setCalendarPopup(True)

        self.verticalLayout_0_0_0_1_0.addWidget(self.date_edit)


        self.verticalGroupBox_0_0_0_1.addLayout(self.verticalLayout_0_0_0_1_0)

        self.verticalLayout_0_0_0_1_1 = QVBoxLayout()
        self.verticalLayout_0_0_0_1_1.setSpacing(0)
        self.verticalLayout_0_0_0_1_1.setObjectName(u"verticalLayout_0_0_0_1_1")
        self.reicept_number = QLabel(self.verticalGroupBox_0_0)
        self.reicept_number.setObjectName(u"reicept_number")
        sizePolicy.setHeightForWidth(self.reicept_number.sizePolicy().hasHeightForWidth())
        self.reicept_number.setSizePolicy(sizePolicy)
        self.reicept_number.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_0_0_0_1_1.addWidget(self.reicept_number)

        self.horizontalLayout_0_0_0_1_1_0 = QHBoxLayout()
        self.horizontalLayout_0_0_0_1_1_0.setSpacing(2)
        self.horizontalLayout_0_0_0_1_1_0.setObjectName(u"horizontalLayout_0_0_0_1_1_0")
        self.receipt_num_edit = QLineEdit(self.verticalGroupBox_0_0)
        self.receipt_num_edit.setObjectName(u"receipt_num_edit")
        self.receipt_num_edit.setEnabled(False)
        self.receipt_num_edit.setMinimumSize(QSize(0, 35))
        self.receipt_num_edit.setFont(font)
        self.receipt_num_edit.setStyleSheet(u"")
        self.receipt_num_edit.setClearButtonEnabled(False)

        self.horizontalLayout_0_0_0_1_1_0.addWidget(self.receipt_num_edit)

        self.toggle_lock_num_btn = QPushButton(self.verticalGroupBox_0_0)
        self.toggle_lock_num_btn.setObjectName(u"toggle_lock_num_btn")
        self.toggle_lock_num_btn.setMinimumSize(QSize(25, 25))
        self.toggle_lock_num_btn.setMaximumSize(QSize(25, 25))
        self.toggle_lock_num_btn.setStyleSheet(u"QPushButton {\n"
"border-radius:12px;\n"
"background-color:#303440;\n"
"border:none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/padlock/assets/padlock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_lock_num_btn.setIcon(icon3)
        self.toggle_lock_num_btn.setCheckable(True)

        self.horizontalLayout_0_0_0_1_1_0.addWidget(self.toggle_lock_num_btn)


        self.verticalLayout_0_0_0_1_1.addLayout(self.horizontalLayout_0_0_0_1_1_0)


        self.verticalGroupBox_0_0_0_1.addLayout(self.verticalLayout_0_0_0_1_1)


        self.horizontalLayout_0_0_0.addLayout(self.verticalGroupBox_0_0_0_1)

        self.line_0 = QFrame(self.verticalGroupBox_0_0)
        self.line_0.setObjectName(u"line_0")
        self.line_0.setFrameShape(QFrame.VLine)
        self.line_0.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_0_0_0.addWidget(self.line_0)

        self.verticalGroupBox_0_0_0_0 = QGroupBox(self.verticalGroupBox_0_0)
        self.verticalGroupBox_0_0_0_0.setObjectName(u"verticalGroupBox_0_0_0_0")
        sizePolicy.setHeightForWidth(self.verticalGroupBox_0_0_0_0.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_0_0_0_0.setSizePolicy(sizePolicy)
        self.verticalGroupBox_0_0_0_0.setMinimumSize(QSize(160, 120))
        self.verticalGroupBox_0_0_0_0.setStyleSheet(u"QGroupBox{\n"
"padding-top:0;\n"
"border:none;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.verticalGroupBox_0_0_0_0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.logo_btn = QPushButton(self.verticalGroupBox_0_0_0_0)
        self.logo_btn.setObjectName(u"logo_btn")
        self.logo_btn.setMinimumSize(QSize(0, 80))
        self.logo_btn.setFont(font)
        self.logo_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logo_btn.setStyleSheet(u"border-bottom:none;")
        icon4 = QIcon()
        icon4.addFile(u":/logo/assets/photo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_btn.setIcon(icon4)
        self.logo_btn.setIconSize(QSize(120, 60))

        self.verticalLayout_12.addWidget(self.logo_btn)

        self.logo_load_btn = QPushButton(self.verticalGroupBox_0_0_0_0)
        self.logo_load_btn.setObjectName(u"logo_load_btn")
        self.logo_load_btn.setMinimumSize(QSize(0, 20))
        self.logo_load_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logo_load_btn.setStyleSheet(u"text-decoration:underline;\n"
"background-color:transparent;\n"
"color:#5b9aff;\n"
"border-top:none;")

        self.verticalLayout_12.addWidget(self.logo_load_btn)


        self.horizontalLayout_0_0_0.addWidget(self.verticalGroupBox_0_0_0_0)


        self.verticalLayout_22.addLayout(self.horizontalLayout_0_0_0)


        self.verticalLayout_18.addWidget(self.verticalGroupBox_0_0)

        self.verticalGroupBox_0_1 = QGroupBox(self.verticalGroupBox_0)
        self.verticalGroupBox_0_1.setObjectName(u"verticalGroupBox_0_1")
        self.verticalLayout = QVBoxLayout(self.verticalGroupBox_0_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_0_1_1 = QVBoxLayout()
        self.verticalLayout_0_1_1.setSpacing(4)
        self.verticalLayout_0_1_1.setObjectName(u"verticalLayout_0_1_1")
        self.name_label_0 = QLabel(self.verticalGroupBox_0_1)
        self.name_label_0.setObjectName(u"name_label_0")
        sizePolicy1.setHeightForWidth(self.name_label_0.sizePolicy().hasHeightForWidth())
        self.name_label_0.setSizePolicy(sizePolicy1)

        self.verticalLayout_0_1_1.addWidget(self.name_label_0)

        self.payer_nam_edit = QLineEdit(self.verticalGroupBox_0_1)
        self.payer_nam_edit.setObjectName(u"payer_nam_edit")
        self.payer_nam_edit.setMinimumSize(QSize(0, 35))
        self.payer_nam_edit.setFont(font)
        self.payer_nam_edit.setStyleSheet(u"")
        self.payer_nam_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_1_1.addWidget(self.payer_nam_edit)


        self.verticalLayout.addLayout(self.verticalLayout_0_1_1)

        self.horizontalLayout_0_1_0 = QHBoxLayout()
        self.horizontalLayout_0_1_0.setObjectName(u"horizontalLayout_0_1_0")
        self.verticalLayout_0_1_0_0 = QVBoxLayout()
        self.verticalLayout_0_1_0_0.setSpacing(4)
        self.verticalLayout_0_1_0_0.setObjectName(u"verticalLayout_0_1_0_0")
        self.cpf_label_0 = QLabel(self.verticalGroupBox_0_1)
        self.cpf_label_0.setObjectName(u"cpf_label_0")
        sizePolicy1.setHeightForWidth(self.cpf_label_0.sizePolicy().hasHeightForWidth())
        self.cpf_label_0.setSizePolicy(sizePolicy1)

        self.verticalLayout_0_1_0_0.addWidget(self.cpf_label_0)

        self.payer_cpf_edit = QLineEdit(self.verticalGroupBox_0_1)
        self.payer_cpf_edit.setObjectName(u"payer_cpf_edit")
        self.payer_cpf_edit.setMinimumSize(QSize(0, 35))
        self.payer_cpf_edit.setFont(font)
        self.payer_cpf_edit.setStyleSheet(u"")
        self.payer_cpf_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_1_0_0.addWidget(self.payer_cpf_edit)


        self.horizontalLayout_0_1_0.addLayout(self.verticalLayout_0_1_0_0)

        self.verticalLayout_0_1_0_1 = QVBoxLayout()
        self.verticalLayout_0_1_0_1.setSpacing(4)
        self.verticalLayout_0_1_0_1.setObjectName(u"verticalLayout_0_1_0_1")
        self.phone_label_0 = QLabel(self.verticalGroupBox_0_1)
        self.phone_label_0.setObjectName(u"phone_label_0")
        sizePolicy1.setHeightForWidth(self.phone_label_0.sizePolicy().hasHeightForWidth())
        self.phone_label_0.setSizePolicy(sizePolicy1)

        self.verticalLayout_0_1_0_1.addWidget(self.phone_label_0)

        self.payer_pho_edit = QLineEdit(self.verticalGroupBox_0_1)
        self.payer_pho_edit.setObjectName(u"payer_pho_edit")
        self.payer_pho_edit.setMinimumSize(QSize(0, 35))
        self.payer_pho_edit.setFont(font)
        self.payer_pho_edit.setStyleSheet(u"")
        self.payer_pho_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_1_0_1.addWidget(self.payer_pho_edit)


        self.horizontalLayout_0_1_0.addLayout(self.verticalLayout_0_1_0_1)


        self.verticalLayout.addLayout(self.horizontalLayout_0_1_0)


        self.verticalLayout_18.addWidget(self.verticalGroupBox_0_1)

        self.verticalGroupBox_0_2 = QGroupBox(self.verticalGroupBox_0)
        self.verticalGroupBox_0_2.setObjectName(u"verticalGroupBox_0_2")
        self.verticalLayout_6 = QVBoxLayout(self.verticalGroupBox_0_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_0_2_2 = QHBoxLayout()
        self.horizontalLayout_0_2_2.setObjectName(u"horizontalLayout_0_2_2")
        self.verticalLayout_0_2_2_0 = QVBoxLayout()
        self.verticalLayout_0_2_2_0.setSpacing(4)
        self.verticalLayout_0_2_2_0.setObjectName(u"verticalLayout_0_2_2_0")
        self.name_label_1 = QLabel(self.verticalGroupBox_0_2)
        self.name_label_1.setObjectName(u"name_label_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.name_label_1.sizePolicy().hasHeightForWidth())
        self.name_label_1.setSizePolicy(sizePolicy2)

        self.verticalLayout_0_2_2_0.addWidget(self.name_label_1)

        self.benef_nam_edit = QLineEdit(self.verticalGroupBox_0_2)
        self.benef_nam_edit.setObjectName(u"benef_nam_edit")
        self.benef_nam_edit.setMinimumSize(QSize(0, 35))
        self.benef_nam_edit.setFont(font)
        self.benef_nam_edit.setStyleSheet(u"")
        self.benef_nam_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_2_2_0.addWidget(self.benef_nam_edit)


        self.horizontalLayout_0_2_2.addLayout(self.verticalLayout_0_2_2_0)

        self.verticalLayout_0_2_2_1 = QVBoxLayout()
        self.verticalLayout_0_2_2_1.setSpacing(4)
        self.verticalLayout_0_2_2_1.setObjectName(u"verticalLayout_0_2_2_1")
        self.cpf_label_1 = QLabel(self.verticalGroupBox_0_2)
        self.cpf_label_1.setObjectName(u"cpf_label_1")
        sizePolicy2.setHeightForWidth(self.cpf_label_1.sizePolicy().hasHeightForWidth())
        self.cpf_label_1.setSizePolicy(sizePolicy2)

        self.verticalLayout_0_2_2_1.addWidget(self.cpf_label_1)

        self.benef_cpf_edit = QLineEdit(self.verticalGroupBox_0_2)
        self.benef_cpf_edit.setObjectName(u"benef_cpf_edit")
        self.benef_cpf_edit.setMinimumSize(QSize(0, 35))
        self.benef_cpf_edit.setFont(font)
        self.benef_cpf_edit.setStyleSheet(u"")
        self.benef_cpf_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_2_2_1.addWidget(self.benef_cpf_edit)


        self.horizontalLayout_0_2_2.addLayout(self.verticalLayout_0_2_2_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_0_2_2)

        self.verticalLayout_0_2_4 = QVBoxLayout()
        self.verticalLayout_0_2_4.setSpacing(4)
        self.verticalLayout_0_2_4.setObjectName(u"verticalLayout_0_2_4")
        self.cep_label = QLabel(self.verticalGroupBox_0_2)
        self.cep_label.setObjectName(u"cep_label")
        sizePolicy.setHeightForWidth(self.cep_label.sizePolicy().hasHeightForWidth())
        self.cep_label.setSizePolicy(sizePolicy)

        self.verticalLayout_0_2_4.addWidget(self.cep_label)

        self.benef_cep_edit = QLineEdit(self.verticalGroupBox_0_2)
        self.benef_cep_edit.setObjectName(u"benef_cep_edit")
        self.benef_cep_edit.setMinimumSize(QSize(0, 35))
        self.benef_cep_edit.setFont(font)
        self.benef_cep_edit.setStyleSheet(u"")
        self.benef_cep_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_2_4.addWidget(self.benef_cep_edit)


        self.verticalLayout_6.addLayout(self.verticalLayout_0_2_4)

        self.horizontalLayout_0_2_1 = QHBoxLayout()
        self.horizontalLayout_0_2_1.setObjectName(u"horizontalLayout_0_2_1")
        self.verticalLayout_0_2_1_0 = QVBoxLayout()
        self.verticalLayout_0_2_1_0.setSpacing(4)
        self.verticalLayout_0_2_1_0.setObjectName(u"verticalLayout_0_2_1_0")
        self.state_label = QLabel(self.verticalGroupBox_0_2)
        self.state_label.setObjectName(u"state_label")

        self.verticalLayout_0_2_1_0.addWidget(self.state_label)

        self.benef_sta_edit = QLineEdit(self.verticalGroupBox_0_2)
        self.benef_sta_edit.setObjectName(u"benef_sta_edit")
        self.benef_sta_edit.setMinimumSize(QSize(0, 35))
        self.benef_sta_edit.setFont(font)
        self.benef_sta_edit.setStyleSheet(u"")
        self.benef_sta_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_2_1_0.addWidget(self.benef_sta_edit)


        self.horizontalLayout_0_2_1.addLayout(self.verticalLayout_0_2_1_0)

        self.verticalLayout_0_2_1_1 = QVBoxLayout()
        self.verticalLayout_0_2_1_1.setSpacing(4)
        self.verticalLayout_0_2_1_1.setObjectName(u"verticalLayout_0_2_1_1")
        self.city_label = QLabel(self.verticalGroupBox_0_2)
        self.city_label.setObjectName(u"city_label")
        sizePolicy.setHeightForWidth(self.city_label.sizePolicy().hasHeightForWidth())
        self.city_label.setSizePolicy(sizePolicy)

        self.verticalLayout_0_2_1_1.addWidget(self.city_label)

        self.benef_cit_edit = QLineEdit(self.verticalGroupBox_0_2)
        self.benef_cit_edit.setObjectName(u"benef_cit_edit")
        self.benef_cit_edit.setMinimumSize(QSize(0, 35))
        self.benef_cit_edit.setFont(font)
        self.benef_cit_edit.setStyleSheet(u"")
        self.benef_cit_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_2_1_1.addWidget(self.benef_cit_edit)


        self.horizontalLayout_0_2_1.addLayout(self.verticalLayout_0_2_1_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_0_2_1)

        self.horizontalLayout_0_2_3 = QHBoxLayout()
        self.horizontalLayout_0_2_3.setObjectName(u"horizontalLayout_0_2_3")
        self.verticalLayout_0_2_3_0 = QVBoxLayout()
        self.verticalLayout_0_2_3_0.setSpacing(4)
        self.verticalLayout_0_2_3_0.setObjectName(u"verticalLayout_0_2_3_0")
        self.street_label = QLabel(self.verticalGroupBox_0_2)
        self.street_label.setObjectName(u"street_label")
        sizePolicy.setHeightForWidth(self.street_label.sizePolicy().hasHeightForWidth())
        self.street_label.setSizePolicy(sizePolicy)

        self.verticalLayout_0_2_3_0.addWidget(self.street_label)

        self.benef_str_edit = QLineEdit(self.verticalGroupBox_0_2)
        self.benef_str_edit.setObjectName(u"benef_str_edit")
        self.benef_str_edit.setMinimumSize(QSize(0, 35))
        self.benef_str_edit.setFont(font)
        self.benef_str_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_2_3_0.addWidget(self.benef_str_edit)


        self.horizontalLayout_0_2_3.addLayout(self.verticalLayout_0_2_3_0)

        self.verticalLayout_0_2_3_1 = QVBoxLayout()
        self.verticalLayout_0_2_3_1.setSpacing(4)
        self.verticalLayout_0_2_3_1.setObjectName(u"verticalLayout_0_2_3_1")
        self.number_label = QLabel(self.verticalGroupBox_0_2)
        self.number_label.setObjectName(u"number_label")

        self.verticalLayout_0_2_3_1.addWidget(self.number_label)

        self.benef_num_edit = QLineEdit(self.verticalGroupBox_0_2)
        self.benef_num_edit.setObjectName(u"benef_num_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.benef_num_edit.sizePolicy().hasHeightForWidth())
        self.benef_num_edit.setSizePolicy(sizePolicy3)
        self.benef_num_edit.setMinimumSize(QSize(0, 35))
        self.benef_num_edit.setMaximumSize(QSize(70, 16777215))
        self.benef_num_edit.setClearButtonEnabled(True)

        self.verticalLayout_0_2_3_1.addWidget(self.benef_num_edit)


        self.horizontalLayout_0_2_3.addLayout(self.verticalLayout_0_2_3_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_0_2_3)

        self.horizontalLayout_0_2_0 = QHBoxLayout()
        self.horizontalLayout_0_2_0.setObjectName(u"horizontalLayout_0_2_0")
        self.verticalLayout_0_2_0_0 = QVBoxLayout()
        self.verticalLayout_0_2_0_0.setSpacing(4)
        self.verticalLayout_0_2_0_0.setObjectName(u"verticalLayout_0_2_0_0")
        self.neighborhood_label = QLabel(self.verticalGroupBox_0_2)
        self.neighborhood_label.setObjectName(u"neighborhood_label")
        sizePolicy.setHeightForWidth(self.neighborhood_label.sizePolicy().hasHeightForWidth())
        self.neighborhood_label.setSizePolicy(sizePolicy)

        self.verticalLayout_0_2_0_0.addWidget(self.neighborhood_label)

        self.benef_nei_edit = QLineEdit(self.verticalGroupBox_0_2)
        self.benef_nei_edit.setObjectName(u"benef_nei_edit")
        self.benef_nei_edit.setMinimumSize(QSize(0, 35))

        self.verticalLayout_0_2_0_0.addWidget(self.benef_nei_edit)


        self.horizontalLayout_0_2_0.addLayout(self.verticalLayout_0_2_0_0)

        self.verticalLayout_0_2_0_1 = QVBoxLayout()
        self.verticalLayout_0_2_0_1.setSpacing(4)
        self.verticalLayout_0_2_0_1.setObjectName(u"verticalLayout_0_2_0_1")
        self.phone_label_1 = QLabel(self.verticalGroupBox_0_2)
        self.phone_label_1.setObjectName(u"phone_label_1")
        sizePolicy.setHeightForWidth(self.phone_label_1.sizePolicy().hasHeightForWidth())
        self.phone_label_1.setSizePolicy(sizePolicy)

        self.verticalLayout_0_2_0_1.addWidget(self.phone_label_1)

        self.benef_pho_edit = QLineEdit(self.verticalGroupBox_0_2)
        self.benef_pho_edit.setObjectName(u"benef_pho_edit")
        self.benef_pho_edit.setMinimumSize(QSize(0, 35))

        self.verticalLayout_0_2_0_1.addWidget(self.benef_pho_edit)


        self.horizontalLayout_0_2_0.addLayout(self.verticalLayout_0_2_0_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_0_2_0)

        self.country_combo = QComboBox(self.verticalGroupBox_0_2)
        self.country_combo.setObjectName(u"country_combo")
        self.country_combo.setMinimumSize(QSize(0, 35))
        self.country_combo.setFont(font)
        self.country_combo.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.country_combo)


        self.verticalLayout_18.addWidget(self.verticalGroupBox_0_2)


        self.gridLayout.addWidget(self.verticalGroupBox_0, 0, 1, 1, 1)

        self.verticalGroupBox_2 = QGroupBox(self.centralwidget)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        sizePolicy.setHeightForWidth(self.verticalGroupBox_2.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_2.setSizePolicy(sizePolicy)
        self.verticalGroupBox_2.setStyleSheet(u"QGroupBox {\n"
"padding-top:0;\n"
"border:none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.verticalGroupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_data_ckb = QCheckBox(self.verticalGroupBox_2)
        self.save_data_ckb.setObjectName(u"save_data_ckb")
        self.save_data_ckb.setChecked(True)

        self.horizontalLayout.addWidget(self.save_data_ckb)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.print_btn = QPushButton(self.verticalGroupBox_2)
        self.print_btn.setObjectName(u"print_btn")
        self.print_btn.setMinimumSize(QSize(130, 30))
        self.print_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.print_btn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/print/assets/print-blue-26.png", QSize(), QIcon.Normal, QIcon.Off)
        self.print_btn.setIcon(icon5)
        self.print_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.print_btn)

        self.preview_btn = QPushButton(self.verticalGroupBox_2)
        self.preview_btn.setObjectName(u"preview_btn")
        self.preview_btn.setMinimumSize(QSize(150, 30))
        self.preview_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/print/assets/preview-blue-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.preview_btn.setIcon(icon6)
        self.preview_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.preview_btn)


        self.gridLayout.addWidget(self.verticalGroupBox_2, 1, 1, 1, 2)

        self.horizontalSpacer_1 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_1, 0, 3, 2, 1)

        self.horizontalSpacer_0 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_0, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 976, 20))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.comp_edit, self.date_edit)
        QWidget.setTabOrder(self.date_edit, self.receipt_num_edit)
        QWidget.setTabOrder(self.receipt_num_edit, self.toggle_lock_num_btn)
        QWidget.setTabOrder(self.toggle_lock_num_btn, self.logo_btn)
        QWidget.setTabOrder(self.logo_btn, self.logo_load_btn)
        QWidget.setTabOrder(self.logo_load_btn, self.payer_nam_edit)
        QWidget.setTabOrder(self.payer_nam_edit, self.payer_cpf_edit)
        QWidget.setTabOrder(self.payer_cpf_edit, self.payer_pho_edit)
        QWidget.setTabOrder(self.payer_pho_edit, self.benef_nam_edit)
        QWidget.setTabOrder(self.benef_nam_edit, self.benef_cpf_edit)
        QWidget.setTabOrder(self.benef_cpf_edit, self.benef_cep_edit)
        QWidget.setTabOrder(self.benef_cep_edit, self.benef_sta_edit)
        QWidget.setTabOrder(self.benef_sta_edit, self.benef_cit_edit)
        QWidget.setTabOrder(self.benef_cit_edit, self.benef_str_edit)
        QWidget.setTabOrder(self.benef_str_edit, self.benef_num_edit)
        QWidget.setTabOrder(self.benef_num_edit, self.benef_nei_edit)
        QWidget.setTabOrder(self.benef_nei_edit, self.benef_pho_edit)
        QWidget.setTabOrder(self.benef_pho_edit, self.country_combo)
        QWidget.setTabOrder(self.country_combo, self.rem_serv_btn)
        QWidget.setTabOrder(self.rem_serv_btn, self.prod_desc_edit)
        QWidget.setTabOrder(self.prod_desc_edit, self.prod_valu_edit)
        QWidget.setTabOrder(self.prod_valu_edit, self.add_serv_btn)
        QWidget.setTabOrder(self.add_serv_btn, self.currency_line_edit)
        QWidget.setTabOrder(self.currency_line_edit, self.currency_btn)
        QWidget.setTabOrder(self.currency_btn, self.receipt_obs_edit)
        QWidget.setTabOrder(self.receipt_obs_edit, self.save_data_ckb)
        QWidget.setTabOrder(self.save_data_ckb, self.print_btn)
        QWidget.setTabOrder(self.print_btn, self.preview_btn)
        QWidget.setTabOrder(self.preview_btn, self.prod_quant_spin)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionPreview)
        self.menuEdit.addAction(self.actionPrint)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionCheckForUpdates)

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gerador de Recibos", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
#if QT_CONFIG(tooltip)
        self.actionPrint.setToolTip(QCoreApplication.translate("MainWindow", u"Go to print area", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPrint.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionPreview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
#if QT_CONFIG(tooltip)
        self.actionPreview.setToolTip(QCoreApplication.translate("MainWindow", u"Go to preview area", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPreview.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
        self.actionCheckForUpdates.setText(QCoreApplication.translate("MainWindow", u"Check for updates", None))
        self.verticalGroupBox_1.setTitle("")
        self.verticalGroupBox_1_0.setTitle(QCoreApplication.translate("MainWindow", u"Servi\u00e7os/Produtos", None))
        self.rem_serv_btn.setText(QCoreApplication.translate("MainWindow", u"Remover servi\u00e7o/produto", None))
        self.verticalGroupBox_1_0_1.setTitle(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o: *", None))
        self.value_label.setText(QCoreApplication.translate("MainWindow", u"Valor: *", None))
        self.prod_valu_edit.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.prod_valu_edit.setPlaceholderText("")
        self.quantity_label.setText(QCoreApplication.translate("MainWindow", u"Quant.: *", None))
        self.add_serv_btn.setText(QCoreApplication.translate("MainWindow", u"Adicionar servi\u00e7o/produto", None))
        self.total_value_label.setText(QCoreApplication.translate("MainWindow", u"TOTAL:", None))
        self.currency_btn.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.total_value_lbl.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.verticalGroupBox_1_1.setTitle(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00e3o", None))
        self.receipt_obs_edit.setPlainText("")
        self.verticalGroupBox_0.setTitle("")
        self.verticalGroupBox_0_0.setTitle(QCoreApplication.translate("MainWindow", u"Dados do recibo", None))
        self.company_label.setText(QCoreApplication.translate("MainWindow", u"Empresa:", None))
        self.comp_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informe o nome da empresa, se houver", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Data do recibo: *", None))
        self.date_edit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.reicept_number.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 do recibo: *", None))
        self.receipt_num_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0000", None))
#if QT_CONFIG(tooltip)
        self.toggle_lock_num_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Desbloquear n\u00famero de recibo.</p><p>Se voc\u00ea desejar um n\u00famero personalizado, clique aqui para desbloquear.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toggle_lock_num_btn.setText("")
#if QT_CONFIG(tooltip)
        self.verticalGroupBox_0_0_0_0.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Carregar logo</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.logo_load_btn.setText(QCoreApplication.translate("MainWindow", u"Carregar logo", None))
        self.verticalGroupBox_0_1.setTitle(QCoreApplication.translate("MainWindow", u"Dados do pagador", None))
        self.name_label_0.setText(QCoreApplication.translate("MainWindow", u"Nome: *", None))
        self.payer_nam_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do pagador", None))
        self.cpf_label_0.setText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ:", None))
        self.payer_cpf_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ do pagador", None))
        self.phone_label_0.setText(QCoreApplication.translate("MainWindow", u"Celular:", None))
        self.payer_pho_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Celular do pagador", None))
        self.verticalGroupBox_0_2.setTitle(QCoreApplication.translate("MainWindow", u"Dados do benefici\u00e1rio", None))
        self.name_label_1.setText(QCoreApplication.translate("MainWindow", u"Nome: *", None))
        self.benef_nam_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do benefici\u00e1rio", None))
        self.cpf_label_1.setText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ:", None))
        self.benef_cpf_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ do benefici\u00e1rio", None))
        self.cep_label.setText(QCoreApplication.translate("MainWindow", u"CEP: *", None))
        self.benef_cep_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP do benefici\u00e1rio", None))
        self.state_label.setText(QCoreApplication.translate("MainWindow", u"Estado: *", None))
        self.benef_sta_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.city_label.setText(QCoreApplication.translate("MainWindow", u"Cidade: *", None))
        self.benef_cit_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.street_label.setText(QCoreApplication.translate("MainWindow", u"Rua: *", None))
        self.benef_str_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rua Exemplo", None))
        self.number_label.setText(QCoreApplication.translate("MainWindow", u"N\u00b0: *", None))
        self.benef_num_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXX", None))
        self.neighborhood_label.setText(QCoreApplication.translate("MainWindow", u"Bairro: *", None))
        self.benef_nei_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro Exemplo", None))
        self.phone_label_1.setText(QCoreApplication.translate("MainWindow", u"Fone:", None))
        self.benef_pho_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Celular do benefici\u00e1rio", None))
        self.country_combo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione o pa\u00eds", None))
        self.verticalGroupBox_2.setTitle("")
        self.save_data_ckb.setText(QCoreApplication.translate("MainWindow", u"Salvar dados para a pr\u00f3xima vez", None))
        self.print_btn.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.preview_btn.setText(QCoreApplication.translate("MainWindow", u"Visualizar modelo", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

