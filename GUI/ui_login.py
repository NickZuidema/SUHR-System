# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginEjAKeu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import resources_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(1543, 850)
        Login.setAcceptDrops(False)
        Login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.silliman_bg = QLabel(self.centralwidget)
        self.silliman_bg.setObjectName(u"silliman_bg")
        self.silliman_bg.setGeometry(QRect(100, -180, 1281, 1111))
        self.silliman_bg.setPixmap(QPixmap(u":/images/background1_silliman.png"))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, -10, 821, 871))
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label.setPixmap(QPixmap(u":/images/background1_fade.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 100, 131, 131))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setLineWidth(1)
        self.label_2.setPixmap(QPixmap(u"images/silliman-logo.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 90, 361, 141))
        self.label_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_3.setPixmap(QPixmap(u":/images/title1_header1.png"))
        self.label_3.setScaledContents(False)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 200, 321, 71))
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_4.setPixmap(QPixmap(u":/images/title1_header2.png"))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 320, 141, 81))
        self.label_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_5.setPixmap(QPixmap(u":/images/title_login-bold.png"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 520, 191, 51))
        self.pushButton.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        icon = QIcon()
        icon.addFile(u":/images/button_login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(186, 49))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 420, 181, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 470, 181, 21))
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName(u"statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        Login.setWindowFilePath("")
        self.silliman_bg.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.pushButton.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Login", u"Username", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
    # retranslateUi

