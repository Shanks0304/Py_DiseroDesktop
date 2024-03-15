# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designer_newbkxjdp.ui'
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
        MainWindow.resize(900, 775)
        MainWindow.setMinimumSize(QSize(900, 775))
        MainWindow.setMaximumSize(QSize(900, 775))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(70, 100, 801, 541))
        self.stackedWidget.setMouseTracking(False)
        self.importPg = QWidget()
        self.importPg.setObjectName(u"importPg")
        self.importPg_lbl = QLabel(self.importPg)
        self.importPg_lbl.setObjectName(u"importPg_lbl")
        self.importPg_lbl.setGeometry(QRect(270, 450, 261, 81))
        self.importPg_lbl.setLayoutDirection(Qt.LeftToRight)
        self.importPg_lbl.setAutoFillBackground(True)
        self.importPg_lbl.setAlignment(Qt.AlignCenter)
        self.importPg_wid_fileDrg = Drag(self.importPg)
        self.importPg_wid_fileDrg.setObjectName(u"importPg_wid_fileDrg")
        self.importPg_wid_fileDrg.setGeometry(QRect(100, 60, 581, 371))
        self.importPg_wid_fileDrg.setAutoFillBackground(False)
        self.importPg_wid_fileDrg.setStyleSheet(u"")
        self.importPg_btn_spl = QPushButton(self.importPg_wid_fileDrg)
        self.importPg_btn_spl.setObjectName(u"importPg_btn_spl")
        self.importPg_btn_spl.setGeometry(QRect(180, 260, 251, 71))
        self.importPg_btn_spl.setMouseTracking(True)
        self.importPg_btn_spl.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/icons/Splitter_GUI_Assets_3/Split Button Default.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importPg_btn_spl.setIcon(icon)
        self.importPg_btn_spl.setIconSize(QSize(300, 101))
        self.importPg_btn_spl.setFlat(True)
        self.importPg_btn_imp = QPushButton(self.importPg_wid_fileDrg)
        self.importPg_btn_imp.setObjectName(u"importPg_btn_imp")
        self.importPg_btn_imp.setGeometry(QRect(170, 260, 271, 71))
        self.importPg_btn_imp.setMouseTracking(True)
        self.importPg_btn_imp.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Splitter_GUI_Assets_3/Browse Button Default.png", QSize(), QIcon.Normal, QIcon.Off)
        self.importPg_btn_imp.setIcon(icon1)
        self.importPg_btn_imp.setIconSize(QSize(300, 100))
        self.importPg_btn_imp.setFlat(True)
        self.filesLogo = QLabel(self.importPg)
        self.filesLogo.setObjectName(u"filesLogo")
        self.filesLogo.setGeometry(QRect(330, 150, 151, 141))
        self.filesLogo.setStyleSheet(u"background-color: rgba(0, 0, 0, 0); /* Set background color to transparent */\n"
"border-image: url(path/to/your/image.png) 10 10 10 10 stretch stretch; /* Adjust path to your image and border size */")
        self.filesLogo.setPixmap(QPixmap(u":/icons/Splitter_GUI_Assets_3/File Drop Icon.png"))
        self.filesLogo.setScaledContents(True)
        self.stackedWidget.addWidget(self.importPg)
        self.splitPg = QWidget()
        self.splitPg.setObjectName(u"splitPg")
        self.splitPg_crl = Spin(self.splitPg)
        self.splitPg_crl.setObjectName(u"splitPg_crl")
        self.splitPg_crl.setGeometry(QRect(0, 0, 781, 581))
        self.splitPg_crl.setAutoFillBackground(False)
        self.splitPg_crl.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.splitPg)
        self.donePg = QWidget()
        self.donePg.setObjectName(u"donePg")
        self.donePg_lbl2 = QLabel(self.donePg)
        self.donePg_lbl2.setObjectName(u"donePg_lbl2")
        self.donePg_lbl2.setGeometry(QRect(250, 310, 311, 121))
        self.donePg_lbl2.setAutoFillBackground(True)
        self.donePg_lbl2.setAlignment(Qt.AlignCenter)
        self.donePg_lbl = QLabel(self.donePg)
        self.donePg_lbl.setObjectName(u"donePg_lbl")
        self.donePg_lbl.setGeometry(QRect(210, 90, 391, 91))
        self.donePg_lbl.setAutoFillBackground(True)
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
        self.licensePg_lb.setAlignment(Qt.AlignCenter)
        self.licensePg_text = QTextEdit(self.licensePg)
        self.licensePg_text.setObjectName(u"licensePg_text")
        self.licensePg_text.setGeometry(QRect(300, 220, 211, 61))
        self.licensePg_cnf_btn = QPushButton(self.licensePg)
        self.licensePg_cnf_btn.setObjectName(u"licensePg_cnf_btn")
        self.licensePg_cnf_btn.setGeometry(QRect(530, 240, 75, 23))
        self.stackedWidget.addWidget(self.licensePg)
        self.settingsPg = QWidget()
        self.settingsPg.setObjectName(u"settingsPg")
        self.settingsPg_exp_btn = QPushButton(self.settingsPg)
        self.settingsPg_exp_btn.setObjectName(u"settingsPg_exp_btn")
        self.settingsPg_exp_btn.setGeometry(QRect(240, 220, 75, 23))
        self.settingsPg_exp_lbl = QLabel(self.settingsPg)
        self.settingsPg_exp_lbl.setObjectName(u"settingsPg_exp_lbl")
        self.settingsPg_exp_lbl.setGeometry(QRect(320, 220, 181, 16))
        self.settingsPg_stp_lbl = QLabel(self.settingsPg)
        self.settingsPg_stp_lbl.setObjectName(u"settingsPg_stp_lbl")
        self.settingsPg_stp_lbl.setGeometry(QRect(240, 280, 321, 161))
        self.settingsPg_stp_lbl.setAlignment(Qt.AlignCenter)
        self.settingsPg_ext_btn = QToolButton(self.settingsPg)
        self.settingsPg_ext_btn.setObjectName(u"settingsPg_ext_btn")
        self.settingsPg_ext_btn.setGeometry(QRect(620, 70, 61, 31))
        self.stackedWidget.addWidget(self.settingsPg)
        self.settingsBtn = QPushButton(self.centralwidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setGeometry(QRect(830, 10, 61, 51))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Splitter_GUI_Assets_3/Settings Icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon2)
        self.settingsBtn.setIconSize(QSize(77, 77))
        self.settingsBtn.setFlat(True)
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
        self.importPg_btn_spl.setText("")
        self.importPg_btn_imp.setText("")
        self.filesLogo.setText("")
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
        self.settingsPg_exp_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.settingsPg_exp_lbl.setText(QCoreApplication.translate("MainWindow", u"export location", None))
        self.settingsPg_stp_lbl.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
        self.settingsPg_ext_btn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.settingsBtn.setText("")
    # retranslateUi

