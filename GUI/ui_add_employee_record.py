# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_employee_recordjIEKaR.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1440, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Outfit Medium"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"font: 500 9pt \"Outfit Medium\";\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.listView = QListView(self.widget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(-10, 0, 1451, 111))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 40, 171, 16))
        font1 = QFont()
        font1.setFamilies([u"Outfit Medium"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: 500 10pt \"Outfit Medium\";")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 60, 171, 16))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 500 10pt \"Outfit Medium\";")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 101, 91))
        self.label_3.setPixmap(QPixmap(u"images/sillimanlogo.png"))
        self.label_3.setScaledContents(True)
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 120, 1331, 571))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1312, 3610))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"\n"
"font: 600 14pt \"Outfit SemiBold\";")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 11, 1, 5)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 16, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 5, 1, 3)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 11, 1, 3)

        self.Image_Upload = QPushButton(self.scrollAreaWidgetContents_2)
        self.Image_Upload.setObjectName(u"Image_Upload")

        self.gridLayout.addWidget(self.Image_Upload, 2, 0, 5, 1)

        self.FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FirstName.setObjectName(u"FirstName")
        self.FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";\n"
"")

        self.gridLayout.addWidget(self.FirstName, 2, 1, 1, 4)

        self.MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MiddleName.setObjectName(u"MiddleName")
        self.MiddleName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MiddleName, 2, 5, 1, 6)

        self.SurName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SurName.setObjectName(u"SurName")
        self.SurName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SurName, 2, 11, 1, 6)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.Position = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Position.setObjectName(u"Position")
        self.Position.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Position, 4, 1, 1, 16)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)

        self.Department = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Department.setObjectName(u"Department")
        self.Department.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Department, 6, 1, 1, 16)

        self.EmployeeImageLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.EmployeeImageLabel.setObjectName(u"EmployeeImageLabel")

        self.gridLayout.addWidget(self.EmployeeImageLabel, 7, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 7, 1, 1, 1)

        self.Signature_Upload = QPushButton(self.scrollAreaWidgetContents_2)
        self.Signature_Upload.setObjectName(u"Signature_Upload")

        self.gridLayout.addWidget(self.Signature_Upload, 8, 0, 3, 1)

        self.DumaAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DumaAddress.setObjectName(u"DumaAddress")
        self.DumaAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DumaAddress, 8, 1, 1, 16)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 9, 1, 1, 1)

        self.HomeAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.HomeAddress.setObjectName(u"HomeAddress")
        self.HomeAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.HomeAddress, 10, 1, 2, 16)

        self.SignatureLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.SignatureLabel.setObjectName(u"SignatureLabel")

        self.gridLayout.addWidget(self.SignatureLabel, 11, 0, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 12, 0, 60, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 12, 1, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 12, 2, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 12, 10, 1, 4)

        self.DateOfBirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DateOfBirth.setObjectName(u"DateOfBirth")
        self.DateOfBirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DateOfBirth, 13, 1, 1, 1)

        self.PlaceOfBirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PlaceOfBirth.setObjectName(u"PlaceOfBirth")
        self.PlaceOfBirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PlaceOfBirth, 13, 2, 1, 8)

        self.Citizenship = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Citizenship.setObjectName(u"Citizenship")
        self.Citizenship.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Citizenship, 13, 10, 1, 7)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 9pt \"Outfit\";")

        self.gridLayout.addWidget(self.label_15, 14, 1, 1, 2)

        self.NONFILIPINO_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_ignore.setObjectName(u"NONFILIPINO_ignore")

        self.gridLayout.addWidget(self.NONFILIPINO_ignore, 14, 16, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 15, 1, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 15, 8, 1, 2)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 15, 16, 1, 1)

        self.NONFILIPINO_passport = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_passport.setObjectName(u"NONFILIPINO_passport")
        self.NONFILIPINO_passport.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_passport, 16, 1, 1, 7)

        self.NONFILIPINO_acrnum = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_acrnum.setObjectName(u"NONFILIPINO_acrnum")
        self.NONFILIPINO_acrnum.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_acrnum, 16, 8, 1, 8)

        self.NONFILIPINO_dateissued = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_dateissued.setObjectName(u"NONFILIPINO_dateissued")
        self.NONFILIPINO_dateissued.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_dateissued, 16, 16, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 17, 1, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 17, 6, 1, 3)

        self.ContactNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.ContactNumber.setObjectName(u"ContactNumber")
        self.ContactNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.ContactNumber, 18, 1, 1, 5)

        self.Email = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Email.setObjectName(u"Email")
        self.Email.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Email, 18, 6, 1, 11)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 19, 1, 1, 2)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 19, 8, 1, 4)

        self.TINnumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.TINnumber.setObjectName(u"TINnumber")
        self.TINnumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.TINnumber, 20, 1, 1, 7)

        self.SSSnumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SSSnumber.setObjectName(u"SSSnumber")
        self.SSSnumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SSSnumber, 20, 8, 1, 9)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 21, 1, 1, 2)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 21, 8, 1, 4)

        self.PagIbigNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PagIbigNumber.setObjectName(u"PagIbigNumber")
        self.PagIbigNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PagIbigNumber, 22, 1, 1, 7)

        self.PhilHNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PhilHNumber.setObjectName(u"PhilHNumber")
        self.PhilHNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PhilHNumber, 22, 8, 1, 9)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 23, 1, 1, 2)

        self.ChurchAffiliation_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.ChurchAffiliation_ignore.setObjectName(u"ChurchAffiliation_ignore")

        self.gridLayout.addWidget(self.ChurchAffiliation_ignore, 23, 16, 1, 1)

        self.ChurchAffiliation = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.ChurchAffiliation.setObjectName(u"ChurchAffiliation")
        self.ChurchAffiliation.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.ChurchAffiliation, 24, 1, 1, 16)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 25, 1, 1, 2)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 25, 10, 1, 5)

        self.FatherName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName.setObjectName(u"FatherName")
        self.FatherName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName, 26, 1, 1, 9)

        self.FatherJob = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherJob.setObjectName(u"FatherJob")
        self.FatherJob.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherJob, 26, 10, 1, 7)

        self.FatherAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherAddress.setObjectName(u"FatherAddress")
        self.FatherAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherAddress, 27, 1, 1, 16)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 28, 1, 1, 2)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 28, 10, 1, 5)

        self.MotherName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherName.setObjectName(u"MotherName")
        self.MotherName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherName, 29, 1, 1, 9)

        self.MotherJob = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherJob.setObjectName(u"MotherJob")
        self.MotherJob.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherJob, 29, 10, 1, 7)

        self.MotherAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherAddress.setObjectName(u"MotherAddress")
        self.MotherAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherAddress, 30, 1, 1, 16)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 31, 1, 1, 2)

        self.Siblings_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.Siblings_ignore.setObjectName(u"Siblings_ignore")

        self.gridLayout.addWidget(self.Siblings_ignore, 31, 16, 1, 1)

        self.FatherName_3 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_3.setObjectName(u"FatherName_3")
        self.FatherName_3.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_3, 32, 1, 1, 3)

        self.FatherName_4 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_4.setObjectName(u"FatherName_4")
        self.FatherName_4.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_4, 32, 4, 1, 9)

        self.FatherName_5 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_5.setObjectName(u"FatherName_5")
        self.FatherName_5.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_5, 32, 13, 1, 4)

        self.FatherName_8 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_8.setObjectName(u"FatherName_8")
        self.FatherName_8.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_8, 33, 1, 1, 3)

        self.FatherName_6 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_6.setObjectName(u"FatherName_6")
        self.FatherName_6.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_6, 33, 4, 1, 9)

        self.FatherName_7 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_7.setObjectName(u"FatherName_7")
        self.FatherName_7.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_7, 33, 13, 1, 4)

        self.Sibling_addfield = QPushButton(self.scrollAreaWidgetContents_2)
        self.Sibling_addfield.setObjectName(u"Sibling_addfield")

        self.gridLayout.addWidget(self.Sibling_addfield, 34, 1, 1, 16)

        self.Siblings_ignore_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.Siblings_ignore_2.setObjectName(u"Siblings_ignore_2")

        self.gridLayout.addWidget(self.Siblings_ignore_2, 35, 16, 1, 1)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 36, 1, 1, 1)

        self.label_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 36, 2, 1, 2)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout.addWidget(self.label_33, 36, 9, 1, 4)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 36, 15, 1, 2)

        self.CivilStatus = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus.setObjectName(u"CivilStatus")
        self.CivilStatus.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus, 37, 1, 1, 1)

        self.SpouseName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SpouseName.setObjectName(u"SpouseName")
        self.SpouseName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SpouseName, 37, 2, 1, 7)

        self.PlaceOfMarriage = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PlaceOfMarriage.setObjectName(u"PlaceOfMarriage")
        self.PlaceOfMarriage.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PlaceOfMarriage, 37, 9, 1, 6)

        self.DateOfMarriage = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DateOfMarriage.setObjectName(u"DateOfMarriage")
        self.DateOfMarriage.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DateOfMarriage, 37, 15, 1, 2)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout.addWidget(self.label_35, 38, 1, 1, 2)

        self.Siblings_ignore_3 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.Siblings_ignore_3.setObjectName(u"Siblings_ignore_3")

        self.gridLayout.addWidget(self.Siblings_ignore_3, 38, 16, 1, 1)

        self.FatherName_14 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_14.setObjectName(u"FatherName_14")
        self.FatherName_14.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_14, 39, 1, 1, 12)

        self.FatherName_13 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_13.setObjectName(u"FatherName_13")
        self.FatherName_13.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_13, 39, 13, 1, 4)

        self.FatherName_10 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_10.setObjectName(u"FatherName_10")
        self.FatherName_10.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_10, 40, 1, 1, 12)

        self.FatherName_9 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_9.setObjectName(u"FatherName_9")
        self.FatherName_9.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_9, 40, 13, 1, 4)

        self.Sibling_addfield_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Sibling_addfield_2.setObjectName(u"Sibling_addfield_2")

        self.gridLayout.addWidget(self.Sibling_addfield_2, 41, 1, 1, 16)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout.addWidget(self.label_36, 42, 1, 1, 2)

        self.CivilStatus_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus_2.setObjectName(u"CivilStatus_2")
        self.CivilStatus_2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus_2, 43, 1, 1, 16)

        self.FatherName_12 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_12.setObjectName(u"FatherName_12")
        self.FatherName_12.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_12, 44, 1, 1, 3)

        self.FatherName_15 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_15.setObjectName(u"FatherName_15")
        self.FatherName_15.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_15, 44, 4, 1, 9)

        self.FatherName_11 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_11.setObjectName(u"FatherName_11")
        self.FatherName_11.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_11, 44, 13, 1, 4)

        self.CivilStatus_3 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus_3.setObjectName(u"CivilStatus_3")
        self.CivilStatus_3.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus_3, 45, 1, 1, 16)

        self.FatherName_16 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_16.setObjectName(u"FatherName_16")
        self.FatherName_16.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_16, 46, 1, 1, 3)

        self.FatherName_17 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_17.setObjectName(u"FatherName_17")
        self.FatherName_17.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_17, 46, 4, 1, 9)

        self.FatherName_18 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_18.setObjectName(u"FatherName_18")
        self.FatherName_18.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_18, 46, 13, 1, 4)

        self.CivilStatus_4 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus_4.setObjectName(u"CivilStatus_4")
        self.CivilStatus_4.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus_4, 47, 1, 1, 16)

        self.FatherName_21 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_21.setObjectName(u"FatherName_21")
        self.FatherName_21.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_21, 48, 1, 1, 3)

        self.FatherName_19 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_19.setObjectName(u"FatherName_19")
        self.FatherName_19.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_19, 48, 4, 1, 9)

        self.FatherName_20 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_20.setObjectName(u"FatherName_20")
        self.FatherName_20.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_20, 48, 13, 1, 4)

        self.CivilStatus_5 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus_5.setObjectName(u"CivilStatus_5")
        self.CivilStatus_5.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus_5, 49, 1, 1, 16)

        self.FatherName_24 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_24.setObjectName(u"FatherName_24")
        self.FatherName_24.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_24, 50, 1, 1, 3)

        self.FatherName_23 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_23.setObjectName(u"FatherName_23")
        self.FatherName_23.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_23, 50, 4, 1, 9)

        self.FatherName_22 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_22.setObjectName(u"FatherName_22")
        self.FatherName_22.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_22, 50, 13, 1, 4)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout.addWidget(self.label_37, 51, 1, 1, 2)

        self.Siblings_ignore_4 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.Siblings_ignore_4.setObjectName(u"Siblings_ignore_4")

        self.gridLayout.addWidget(self.Siblings_ignore_4, 51, 15, 1, 2)

        self.FatherName_30 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_30.setObjectName(u"FatherName_30")
        self.FatherName_30.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_30, 52, 1, 1, 3)

        self.FatherName_28 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_28.setObjectName(u"FatherName_28")
        self.FatherName_28.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_28, 52, 4, 1, 9)

        self.FatherName_29 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_29.setObjectName(u"FatherName_29")
        self.FatherName_29.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_29, 52, 13, 1, 4)

        self.FatherName_26 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_26.setObjectName(u"FatherName_26")
        self.FatherName_26.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_26, 53, 1, 1, 3)

        self.FatherName_27 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_27.setObjectName(u"FatherName_27")
        self.FatherName_27.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_27, 53, 4, 1, 9)

        self.FatherName_25 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_25.setObjectName(u"FatherName_25")
        self.FatherName_25.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_25, 53, 13, 1, 4)

        self.Sibling_addfield_3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Sibling_addfield_3.setObjectName(u"Sibling_addfield_3")

        self.gridLayout.addWidget(self.Sibling_addfield_3, 54, 1, 1, 16)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout.addWidget(self.label_38, 55, 1, 1, 2)

        self.CivilStatus_6 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus_6.setObjectName(u"CivilStatus_6")
        self.CivilStatus_6.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus_6, 56, 1, 1, 16)

        self.Sibling_addfield_4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Sibling_addfield_4.setObjectName(u"Sibling_addfield_4")

        self.gridLayout.addWidget(self.Sibling_addfield_4, 57, 1, 1, 16)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout.addWidget(self.label_39, 58, 1, 1, 2)

        self.CivilStatus_7 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus_7.setObjectName(u"CivilStatus_7")
        self.CivilStatus_7.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus_7, 59, 1, 1, 16)

        self.Sibling_addfield_5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Sibling_addfield_5.setObjectName(u"Sibling_addfield_5")

        self.gridLayout.addWidget(self.Sibling_addfield_5, 60, 1, 1, 16)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout.addWidget(self.label_40, 61, 1, 1, 2)

        self.Siblings_ignore_5 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.Siblings_ignore_5.setObjectName(u"Siblings_ignore_5")

        self.gridLayout.addWidget(self.Siblings_ignore_5, 61, 14, 1, 3)

        self.FatherName_36 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_36.setObjectName(u"FatherName_36")
        self.FatherName_36.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_36, 62, 1, 1, 2)

        self.FatherName_32 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_32.setObjectName(u"FatherName_32")
        self.FatherName_32.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_32, 62, 3, 1, 6)

        self.FatherName_35 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_35.setObjectName(u"FatherName_35")
        self.FatherName_35.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_35, 62, 9, 1, 3)

        self.FatherName_37 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_37.setObjectName(u"FatherName_37")
        self.FatherName_37.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_37, 62, 12, 1, 5)

        self.FatherName_33 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_33.setObjectName(u"FatherName_33")
        self.FatherName_33.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_33, 63, 1, 1, 16)

        self.Sibling_addfield_6 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Sibling_addfield_6.setObjectName(u"Sibling_addfield_6")

        self.gridLayout.addWidget(self.Sibling_addfield_6, 64, 1, 1, 16)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout.addWidget(self.label_41, 65, 1, 1, 2)

        self.Siblings_ignore_6 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.Siblings_ignore_6.setObjectName(u"Siblings_ignore_6")

        self.gridLayout.addWidget(self.Siblings_ignore_6, 65, 16, 1, 1)

        self.FatherName_44 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_44.setObjectName(u"FatherName_44")
        self.FatherName_44.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_44, 66, 1, 1, 2)

        self.FatherName_42 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_42.setObjectName(u"FatherName_42")
        self.FatherName_42.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_42, 66, 3, 1, 4)

        self.FatherName_43 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_43.setObjectName(u"FatherName_43")
        self.FatherName_43.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_43, 66, 7, 1, 5)

        self.FatherName_41 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_41.setObjectName(u"FatherName_41")
        self.FatherName_41.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_41, 66, 12, 1, 5)

        self.Sibling_addfield_7 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Sibling_addfield_7.setObjectName(u"Sibling_addfield_7")

        self.gridLayout.addWidget(self.Sibling_addfield_7, 67, 1, 1, 16)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout.addWidget(self.label_42, 68, 1, 1, 2)

        self.Siblings_ignore_7 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.Siblings_ignore_7.setObjectName(u"Siblings_ignore_7")

        self.gridLayout.addWidget(self.Siblings_ignore_7, 68, 16, 1, 1)

        self.FatherName_45 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName_45.setObjectName(u"FatherName_45")
        self.FatherName_45.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName_45, 69, 1, 1, 16)

        self.Sibling_addfield_8 = QPushButton(self.scrollAreaWidgetContents_2)
        self.Sibling_addfield_8.setObjectName(u"Sibling_addfield_8")

        self.gridLayout.addWidget(self.Sibling_addfield_8, 70, 1, 1, 16)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 71, 11, 1, 5)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 71, 16, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.listView.raise_()
        self.scrollArea.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()

        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Silliman University ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Personnel Record Dashboard", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adding Employee Record", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"This confirms that all details are true.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.Image_Upload.setText(QCoreApplication.translate("MainWindow", u"Upload Employee Image", None))
        self.FirstName.setPlainText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.MiddleName.setPlainText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.SurName.setPlainText(QCoreApplication.translate("MainWindow", u"Surname...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Position(s)", None))
        self.Position.setPlainText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Department(s)", None))
        self.Department.setPlainText(QCoreApplication.translate("MainWindow", u"Department...", None))
        self.EmployeeImageLabel.setText(QCoreApplication.translate("MainWindow", u"(image name here)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dumaguete address", None))
        self.Signature_Upload.setText(QCoreApplication.translate("MainWindow", u"Upload Employee Signature", None))
        self.DumaAddress.setPlainText(QCoreApplication.translate("MainWindow", u"Full Dumaguete address...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Home address", None))
        self.HomeAddress.setPlainText(QCoreApplication.translate("MainWindow", u"Full home address...", None))
        self.SignatureLabel.setText(QCoreApplication.translate("MainWindow", u"(image name here)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Date of birth", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Place of birth", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Citizenship", None))
        self.DateOfBirth.setPlainText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.PlaceOfBirth.setPlainText(QCoreApplication.translate("MainWindow", u"Place of birth...", None))
        self.Citizenship.setPlainText(QCoreApplication.translate("MainWindow", u"Citizenship...", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"If non-Filipino*, please fill the following fields...", None))
        self.NONFILIPINO_ignore.setText(QCoreApplication.translate("MainWindow", u"Ignore fields", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Passport number", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ACR number", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Date issued", None))
        self.NONFILIPINO_passport.setPlainText(QCoreApplication.translate("MainWindow", u"Passport number...", None))
        self.NONFILIPINO_acrnum.setPlainText(QCoreApplication.translate("MainWindow", u"ACR number...", None))
        self.NONFILIPINO_dateissued.setPlainText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Contact number", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"E-mail address", None))
        self.ContactNumber.setPlainText(QCoreApplication.translate("MainWindow", u"Contact number...", None))
        self.Email.setPlainText(QCoreApplication.translate("MainWindow", u"E-mail address...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Tax Identification Number", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SSS Number", None))
        self.TINnumber.setPlainText(QCoreApplication.translate("MainWindow", u"TIN...", None))
        self.SSSnumber.setPlainText(QCoreApplication.translate("MainWindow", u"SSS...", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Pag-Ibig Number", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Philhealth Number", None))
        self.PagIbigNumber.setPlainText(QCoreApplication.translate("MainWindow", u"Pag-Ibig No. ...", None))
        self.PhilHNumber.setPlainText(QCoreApplication.translate("MainWindow", u"Philhealth No. ...", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Church affiliation", None))
        self.ChurchAffiliation_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no church affiliation.", None))
        self.ChurchAffiliation.setPlainText(QCoreApplication.translate("MainWindow", u"Church affiliation...", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Father", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Father's occupation", None))
        self.FatherName.setPlainText(QCoreApplication.translate("MainWindow", u"Father's full name...", None))
        self.FatherJob.setPlainText(QCoreApplication.translate("MainWindow", u"Father's occupation...", None))
        self.FatherAddress.setPlainText(QCoreApplication.translate("MainWindow", u"Father's current home address...", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Mother", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Mother's occupation", None))
        self.MotherName.setPlainText(QCoreApplication.translate("MainWindow", u"Mother's full name...", None))
        self.MotherJob.setPlainText(QCoreApplication.translate("MainWindow", u"Mother's occupation...", None))
        self.MotherAddress.setPlainText(QCoreApplication.translate("MainWindow", u"Mother's current home address...", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Sibling(s)", None))
        self.Siblings_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no siblings.", None))
        self.FatherName_3.setPlainText(QCoreApplication.translate("MainWindow", u"Sibling's full name...", None))
        self.FatherName_4.setPlainText(QCoreApplication.translate("MainWindow", u"Occupation...", None))
        self.FatherName_5.setPlainText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.FatherName_8.setPlainText(QCoreApplication.translate("MainWindow", u"Sibling's full name...", None))
        self.FatherName_6.setPlainText(QCoreApplication.translate("MainWindow", u"Occupation...", None))
        self.FatherName_7.setPlainText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.Sibling_addfield.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.Siblings_ignore_2.setText(QCoreApplication.translate("MainWindow", u"Employee is unmarried.", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Civil status", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Name of spouse", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Place of marriage", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Date of marriage", None))
        self.CivilStatus.setPlainText(QCoreApplication.translate("MainWindow", u"Civil status...", None))
        self.SpouseName.setPlainText(QCoreApplication.translate("MainWindow", u"Name of spouse...", None))
        self.PlaceOfMarriage.setPlainText(QCoreApplication.translate("MainWindow", u"Place of marriage...", None))
        self.DateOfMarriage.setPlainText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Children (if any)", None))
        self.Siblings_ignore_3.setText(QCoreApplication.translate("MainWindow", u"Employee has no children.", None))
        self.FatherName_14.setPlainText(QCoreApplication.translate("MainWindow", u"Name of child...", None))
        self.FatherName_13.setPlainText(QCoreApplication.translate("MainWindow", u"Date of birth...", None))
        self.FatherName_10.setPlainText(QCoreApplication.translate("MainWindow", u"Name of child...", None))
        self.FatherName_9.setPlainText(QCoreApplication.translate("MainWindow", u"Date of birth...", None))
        self.Sibling_addfield_2.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Academic record", None))
        self.CivilStatus_2.setPlainText(QCoreApplication.translate("MainWindow", u"Elementary School...", None))
        self.FatherName_12.setPlainText(QCoreApplication.translate("MainWindow", u"Address of elementary school...", None))
        self.FatherName_15.setPlainText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.FatherName_11.setPlainText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.CivilStatus_3.setPlainText(QCoreApplication.translate("MainWindow", u"High School...", None))
        self.FatherName_16.setPlainText(QCoreApplication.translate("MainWindow", u"Address of high school...", None))
        self.FatherName_17.setPlainText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.FatherName_18.setPlainText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.CivilStatus_4.setPlainText(QCoreApplication.translate("MainWindow", u"College...", None))
        self.FatherName_21.setPlainText(QCoreApplication.translate("MainWindow", u"Address of College...", None))
        self.FatherName_19.setPlainText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.FatherName_20.setPlainText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.CivilStatus_5.setPlainText(QCoreApplication.translate("MainWindow", u"Graduate School...", None))
        self.FatherName_24.setPlainText(QCoreApplication.translate("MainWindow", u"Address of graduate school...", None))
        self.FatherName_23.setPlainText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.FatherName_22.setPlainText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Related staff member(s)", None))
        self.Siblings_ignore_4.setText(QCoreApplication.translate("MainWindow", u"Employee is not related to any staff.", None))
        self.FatherName_30.setPlainText(QCoreApplication.translate("MainWindow", u"Name...", None))
        self.FatherName_28.setPlainText(QCoreApplication.translate("MainWindow", u"Relationship...", None))
        self.FatherName_29.setPlainText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.FatherName_26.setPlainText(QCoreApplication.translate("MainWindow", u"Name...", None))
        self.FatherName_27.setPlainText(QCoreApplication.translate("MainWindow", u"Relationship...", None))
        self.FatherName_25.setPlainText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.Sibling_addfield_3.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"School or college distinction(s)", None))
        self.CivilStatus_6.setPlainText(QCoreApplication.translate("MainWindow", u"Includes scholarships, awards, etc ...", None))
        self.Sibling_addfield_4.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Publication(s)", None))
        self.CivilStatus_7.setPlainText(QCoreApplication.translate("MainWindow", u"Includes thesis papers, and other publications ...", None))
        self.Sibling_addfield_5.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Record of previous employment", None))
        self.Siblings_ignore_5.setText(QCoreApplication.translate("MainWindow", u"Employee has no record of prior employment.", None))
        self.FatherName_36.setPlainText(QCoreApplication.translate("MainWindow", u"Name of employer...", None))
        self.FatherName_32.setPlainText(QCoreApplication.translate("MainWindow", u"Position at workplace...", None))
        self.FatherName_35.setPlainText(QCoreApplication.translate("MainWindow", u"Period of employment...", None))
        self.FatherName_37.setPlainText(QCoreApplication.translate("MainWindow", u"Reason for leaving...", None))
        self.FatherName_33.setPlainText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.Sibling_addfield_6.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Government examination(s) passed", None))
        self.Siblings_ignore_6.setText(QCoreApplication.translate("MainWindow", u"Does not apply", None))
        self.FatherName_44.setPlainText(QCoreApplication.translate("MainWindow", u"Examination...", None))
        self.FatherName_42.setPlainText(QCoreApplication.translate("MainWindow", u"Rating...", None))
        self.FatherName_43.setPlainText(QCoreApplication.translate("MainWindow", u"Date of examination...", None))
        self.FatherName_41.setPlainText(QCoreApplication.translate("MainWindow", u"Place...", None))
        self.Sibling_addfield_7.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Involvement in criminal case(s)*", None))
        self.Siblings_ignore_7.setText(QCoreApplication.translate("MainWindow", u"Does not apply", None))
        self.FatherName_45.setPlainText(QCoreApplication.translate("MainWindow", u"Case name...", None))
        self.Sibling_addfield_8.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"This confirms that all details are true.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
    # retranslateUi

