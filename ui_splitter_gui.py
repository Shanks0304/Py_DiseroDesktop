# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splitter_guiifSboB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from dragFunction import Drag
from spinnerFunction import Spin

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 750)
        MainWindow.setMinimumSize(QSize(900, 750))
        MainWindow.setMaximumSize(QSize(900, 750))
        MainWindow.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 900, 750))
        self.stackedWidget.setMouseTracking(False)
        self.importPg = QWidget()
        self.importPg.setObjectName(u"importPg")
        self.importPg_lbl = QLabel(self.importPg)
        self.importPg_lbl.setObjectName(u"importPg_lbl")
        self.importPg_lbl.setGeometry(QRect(330, 640, 261, 81))
        self.importPg_lbl.setLayoutDirection(Qt.LeftToRight)
        self.importPg_lbl.setAutoFillBackground(False)
        self.importPg_lbl.setStyleSheet(u"background-color: rgb(86, 86, 86);")
        self.importPg_lbl.setAlignment(Qt.AlignCenter)
        self.importPg_wid_fileDrg = Drag(self.importPg)
        self.importPg_wid_fileDrg.setObjectName(u"importPg_wid_fileDrg")
        self.importPg_wid_fileDrg.setGeometry(QRect(181, 185, 538, 380))
        self.importPg_wid_fileDrg.setMinimumSize(QSize(538, 380))
        self.importPg_wid_fileDrg.setMaximumSize(QSize(538, 380))
        self.importPg_wid_fileDrg.setAutoFillBackground(False)
        self.importPg_wid_fileDrg.setStyleSheet(u"")
        self.importPg_dot_lbl = QLabel(self.importPg_wid_fileDrg)
        self.importPg_dot_lbl.setObjectName(u"importPg_dot_lbl")
        self.importPg_dot_lbl.setGeometry(QRect(0, 0, 538, 380))
        self.importPg_dot_lbl.setPixmap(QPixmap(u":/icons/Splitter_GUI_Assets_3/Rectangle Default.png"))
        self.importPg_top_lbl = QLabel(self.importPg_wid_fileDrg)
        self.importPg_top_lbl.setObjectName(u"importPg_top_lbl")
        self.importPg_top_lbl.setGeometry(QRect(20, 40, 501, 31))
        self.importPg_top_lbl.setStyleSheet(u"color: rgb(95, 95, 95);\n"
"font-family: \"Source Sans Pro\";\n"
"font-size: 15pt; /* Adjust the font size as needed */\n"
"font-weight: bold; /* Set to bold */\n"
"font-style: italic; /* Set to italic */\n"
"background-color: transparent;")
        self.importPg_top_lbl.setAlignment(Qt.AlignCenter)
        self.importPg_btn_spl = QPushButton(self.importPg)
        self.importPg_btn_spl.setObjectName(u"importPg_btn_spl")
        self.importPg_btn_spl.setGeometry(QRect(344, 464, 211, 60))
        self.importPg_btn_spl.setMouseTracking(True)
        self.importPg_btn_spl.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/icons/Splitter_GUI_Assets_3/Split Button 2 Default.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importPg_btn_spl.setIcon(icon)
        self.importPg_btn_spl.setIconSize(QSize(211, 60))
        self.importPg_btn_spl.setFlat(True)
        self.importPg_btn_imp = QPushButton(self.importPg)
        self.importPg_btn_imp.setObjectName(u"importPg_btn_imp")
        self.importPg_btn_imp.setGeometry(QRect(326, 464, 248, 60))
        self.importPg_btn_imp.setMouseTracking(True)
        self.importPg_btn_imp.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Splitter_GUI_Assets_3/Browse Button Default 2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importPg_btn_imp.setIcon(icon1)
        self.importPg_btn_imp.setIconSize(QSize(248, 60))
        self.importPg_btn_imp.setFlat(True)
        self.filesLogo = QLabel(self.importPg)
        self.filesLogo.setObjectName(u"filesLogo")
        self.filesLogo.setGeometry(QRect(373, 279, 154, 154))
        self.filesLogo.setMaximumSize(QSize(16777215, 16777215))
        self.filesLogo.setStyleSheet(u"background-color: rgba(0, 0, 0, 0); /* Set background color to transparent */\n"
"border-image: url(path/to/your/image.png) 10 10 10 10 stretch stretch; /* Adjust path to your image and border size */")
        self.filesLogo.setPixmap(QPixmap(u":/icons/Splitter_GUI_Assets_3/File Drop Icon.png"))
        self.filesLogo.setScaledContents(True)
        self.importPg_file_lbl = QLabel(self.importPg)
        self.importPg_file_lbl.setObjectName(u"importPg_file_lbl")
        self.importPg_file_lbl.setGeometry(QRect(189, 347, 521, 31))
        self.importPg_file_lbl.setStyleSheet(u"color: rgb(95, 95, 95);\n"
"font-family: \"Source Sans Pro\";\n"
"font-size: 15pt; /* Adjust the font size as needed */\n"
"font-weight: 600; /* Set to bold */\n"
"background-color: transparent;")
        self.importPg_file_lbl.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.importPg)
        self.splitPg = QWidget()
        self.splitPg.setObjectName(u"splitPg")
        self.splitPg_crl = Spin(self.splitPg)
        self.splitPg_crl.setObjectName(u"splitPg_crl")
        self.splitPg_crl.setGeometry(QRect(0, 0, 900, 750))
        self.splitPg_crl.setAutoFillBackground(False)
        self.splitPg_crl.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.splitPg)
        self.donePg = QWidget()
        self.donePg.setObjectName(u"donePg")
        self.donePg_lbl2 = QLabel(self.donePg)
        self.donePg_lbl2.setObjectName(u"donePg_lbl2")
        self.donePg_lbl2.setGeometry(QRect(250, 310, 311, 121))
        self.donePg_lbl2.setAutoFillBackground(False)
        self.donePg_lbl2.setAlignment(Qt.AlignCenter)
        self.donePg_lbl = QLabel(self.donePg)
        self.donePg_lbl.setObjectName(u"donePg_lbl")
        self.donePg_lbl.setGeometry(QRect(210, 90, 391, 91))
        self.donePg_lbl.setAutoFillBackground(False)
        self.donePg_lbl.setAlignment(Qt.AlignCenter)
        self.donePg_btn_newSplt = QPushButton(self.donePg)
        self.donePg_btn_newSplt.setObjectName(u"donePg_btn_newSplt")
        self.donePg_btn_newSplt.setGeometry(QRect(350, 240, 111, 23))
        self.stackedWidget.addWidget(self.donePg)
        self.licensePg = QWidget()
        self.licensePg.setObjectName(u"licensePg")
        self.licensePg_lb = QLabel(self.licensePg)
        self.licensePg_lb.setObjectName(u"licensePg_lb")
        self.licensePg_lb.setGeometry(QRect(280, 300, 251, 91))
        self.licensePg_lb.setStyleSheet(u"background-color: rgb(86, 86, 86);")
        self.licensePg_lb.setAlignment(Qt.AlignCenter)
        self.licensePg_text = QTextEdit(self.licensePg)
        self.licensePg_text.setObjectName(u"licensePg_text")
        self.licensePg_text.setGeometry(QRect(300, 220, 211, 61))
        self.licensePg_text.setStyleSheet(u"background-color: rgb(86, 86, 86);")
        self.licensePg_cnf_btn = QPushButton(self.licensePg)
        self.licensePg_cnf_btn.setObjectName(u"licensePg_cnf_btn")
        self.licensePg_cnf_btn.setGeometry(QRect(530, 240, 75, 23))
        self.licensePg_cnf_btn.setStyleSheet(u"background-color: rgb(86, 86, 86);")
        self.stackedWidget.addWidget(self.licensePg)
        self.settingsPg = QWidget()
        self.settingsPg.setObjectName(u"settingsPg")
        self.settingsPg_exp_lbl = QLabel(self.settingsPg)
        self.settingsPg_exp_lbl.setObjectName(u"settingsPg_exp_lbl")
        self.settingsPg_exp_lbl.setGeometry(QRect(148, 468, 604, 55))
        self.settingsPg_exp_lbl.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border: none;\n"
"border-radius: 15px;\n"
"color: rgb(30, 30, 30);\n"
"font-family: \"Source Sans Pro\";\n"
"font-size: 15pt; /* Adjust the font size as needed */\n"
"font-weight: bold; /* Set to bold */\n"
"padding-left: 10px;")
        self.settingsPg_stp_lbl = QLabel(self.settingsPg)
        self.settingsPg_stp_lbl.setObjectName(u"settingsPg_stp_lbl")
        self.settingsPg_stp_lbl.setGeometry(QRect(360, 560, 211, 131))
        self.settingsPg_stp_lbl.setStyleSheet(u"background-color: rgb(86, 86, 86);")
        self.settingsPg_stp_lbl.setAlignment(Qt.AlignCenter)
        self.settingsPg_licens_enter_btn = QLineEdit(self.settingsPg)
        self.settingsPg_licens_enter_btn.setObjectName(u"settingsPg_licens_enter_btn")
        self.settingsPg_licens_enter_btn.setGeometry(QRect(148, 265, 604, 55))
        self.settingsPg_licens_enter_btn.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"border: none;\n"
"border-radius: 15px;\n"
"color: rgb(30, 30, 30);\n"
"font-family: \"Source Sans Pro\";\n"
"font-size: 15pt; /* Adjust the font size as needed */\n"
"font-weight: bold; /* Set to bold */\n"
"padding-left: 10px;")
        self.settingsPg_lic_lbl = QLabel(self.settingsPg)
        self.settingsPg_lic_lbl.setObjectName(u"settingsPg_lic_lbl")
        self.settingsPg_lic_lbl.setGeometry(QRect(270, 230, 371, 31))
        self.settingsPg_lic_lbl.setStyleSheet(u"color: rgb(95, 95, 95);\n"
"font-family: \"Source Sans Pro\";\n"
"font-size: 15pt; /* Adjust the font size as needed */\n"
"font-weight: bold; /* Set to bold */\n"
"font-style: italic; /* Set to italic */\n"
"background-color: transparent;")
        self.settingsPg_lic_lbl.setAlignment(Qt.AlignCenter)
        self.settingsPg_exp_head_lbl = QLabel(self.settingsPg)
        self.settingsPg_exp_head_lbl.setObjectName(u"settingsPg_exp_head_lbl")
        self.settingsPg_exp_head_lbl.setGeometry(QRect(240, 440, 451, 21))
        self.settingsPg_exp_head_lbl.setStyleSheet(u"color: rgb(95, 95, 95);\n"
"font-family: \"Source Sans Pro\";\n"
"font-size: 15pt; /* Adjust the font size as needed */\n"
"font-weight: bold; /* Set to bold */\n"
"font-style: italic; /* Set to italic */\n"
"background-color: transparent;")
        self.settingsPg_exp_head_lbl.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.settingsPg)
        self.settingsBtn = QPushButton(self.centralwidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setGeometry(QRect(827, 25, 48, 48))
        self.settingsBtn.setMouseTracking(True)
        self.settingsBtn.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Splitter_GUI_Assets_3/Settings Icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon2)
        self.settingsBtn.setIconSize(QSize(77, 77))
        self.settingsBtn.setFlat(True)
        self.settingsPg_ext_btn = QToolButton(self.centralwidget)
        self.settingsPg_ext_btn.setObjectName(u"settingsPg_ext_btn")
        self.settingsPg_ext_btn.setGeometry(QRect(827, 25, 48, 48))
        self.settingsPg_ext_btn.setMouseTracking(True)
        self.settingsPg_ext_btn.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Splitter_GUI_Assets_3/Exit Icon Default.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsPg_ext_btn.setIcon(icon3)
        self.settingsPg_ext_btn.setIconSize(QSize(100, 100))
        self.settingsPg_exp_btn = QPushButton(self.centralwidget)
        self.settingsPg_exp_btn.setObjectName(u"settingsPg_exp_btn")
        self.settingsPg_exp_btn.setGeometry(QRect(705, 476, 39, 39))
        self.settingsPg_exp_btn.setMinimumSize(QSize(39, 39))
        self.settingsPg_exp_btn.setMaximumSize(QSize(39, 39))
        self.settingsPg_exp_btn.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Splitter_GUI_Assets_3/Dots_Icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsPg_exp_btn.setIcon(icon4)
        self.settingsPg_exp_btn.setIconSize(QSize(39, 39))
        self.settingsPg_exp_btn.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.importPg_lbl.setText(QCoreApplication.translate("MainWindow", u"Step 1: Drag and Drop File", None))
        self.importPg_dot_lbl.setText("")
        self.importPg_top_lbl.setText(QCoreApplication.translate("MainWindow", u"DROP YOUR REFERENCE FILE HERE", None))
        self.importPg_btn_spl.setText("")
        self.importPg_btn_imp.setText("")
        self.filesLogo.setText("")
        self.importPg_file_lbl.setText("")
        self.donePg_lbl2.setText(QCoreApplication.translate("MainWindow", u"Step 4: Process Completed", None))
        self.donePg_lbl.setText(QCoreApplication.translate("MainWindow", u"Congrats or something", None))
        self.donePg_btn_newSplt.setText(QCoreApplication.translate("MainWindow", u"Split new thing", None))
        self.licensePg_lb.setText(QCoreApplication.translate("MainWindow", u"License Entry Page", None))
        self.licensePg_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter License Code Here</p></body></html>", None))
        self.licensePg_cnf_btn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.settingsPg_exp_lbl.setText("")
        self.settingsPg_stp_lbl.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
        self.settingsPg_licens_enter_btn.setText("")
        self.settingsPg_lic_lbl.setText(QCoreApplication.translate("MainWindow", u"Please enter your license:", None))
        self.settingsPg_exp_head_lbl.setText(QCoreApplication.translate("MainWindow", u"Please enter a default export folder:", None))
        self.settingsBtn.setText("")
        self.settingsPg_ext_btn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.settingsPg_exp_btn.setText("")
    # retranslateUi

