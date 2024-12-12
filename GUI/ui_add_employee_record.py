# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_employee_recordCANLASOgFRUw.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1483, 767)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1440, 700))
        MainWindow.setStyleSheet(u"background-color:white;\n"
"color: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Outfit Medium"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"font: 500 9pt \"Outfit Medium\";\n"
"color:black;\n"
"background-color:white;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: white;\n"
"color:black;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 91))
        self.groupBox.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"color:black;\n"
"")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 20, 221, 51))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Outfit Medium"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:black;\n"
"background-color:white;\n"
"font: 500 12pt \"Outfit Medium\";")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 500 12pt \"Outfit Medium\";color:black;\n"
"background-color:white;")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 101, 91))
        self.label_3.setStyleSheet(u"color:black;\n"
"background-color:white;")
        self.label_3.setPixmap(QPixmap(u"images/sillimanlogo.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    background-color: white; /* Background color for the scroll area */\n"
"	color: black;\n"
"    border: 2px solid black; /* Optional border */\n"
" \n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 0px solid #dcdcdc; /* Border around the scrollbar */\n"
"    background: #f5f5f5;       /* Background of the scrollbar area */\n"
"    width: 12px;               /* Width of the scrollbar */\n"
"    margin: 0px 0px 0px 0px;   /* Margins around the scrollbar */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #888;          /* Color of the scrollbar handle */\n"
"    min-height: 10px;          /* Minimum height of the scrollbar handle */\n"
"    border-radius: 5px;        /* Rounded corners of the scrollbar handle */\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #dcdcdc;       /* Background color of arrow buttons */\n"
"    border: 1px solid #aaa;    /* Border around the arrow buttons */\n"
"    height: 12px;              /* Height"
                        " of arrow buttons */\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top;  /* Positions at top and bottom */\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -803, 1429, 2742))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"color:black;\n"
"background-color:white;\n"
"border: 1px solid black")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"\n"
"background-color:white;\n"
"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.diploma_elementary = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_elementary.setObjectName(u"diploma_elementary")
        self.diploma_elementary.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_elementary, 43, 4, 1, 9)

        self.child1_dateofbirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_dateofbirth.setObjectName(u"child1_dateofbirth")
        self.child1_dateofbirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.child1_dateofbirth, 40, 13, 1, 4)

        self.elementary_school_address = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.elementary_school_address.setObjectName(u"elementary_school_address")
        self.elementary_school_address.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.elementary_school_address, 43, 1, 1, 3)

        self.case_name = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.case_name.setObjectName(u"case_name")
        self.case_name.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.case_name, 63, 1, 1, 16)

        self.staff_MiddleName1 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_MiddleName1.setObjectName(u"staff_MiddleName1")

        self.gridLayout.addWidget(self.staff_MiddleName1, 51, 2, 1, 2)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_21, 22, 1, 1, 2)

        self.staff_FirstName1 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_FirstName1.setObjectName(u"staff_FirstName1")
        self.staff_FirstName1.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_FirstName1, 51, 1, 1, 1)

        self.staff_relationship2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_relationship2.setObjectName(u"staff_relationship2")
        self.staff_relationship2.setMaximumSize(QSize(16777215, 16777215))
        self.staff_relationship2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_relationship2, 51, 5, 1, 8)

        self.ChurchAffiliation = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.ChurchAffiliation.setObjectName(u"ChurchAffiliation")
        self.ChurchAffiliation.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.ChurchAffiliation, 27, 1, 1, 16)

        self.Spouse_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Spouse_MiddleName.setObjectName(u"Spouse_MiddleName")

        self.gridLayout.addWidget(self.Spouse_MiddleName, 38, 6, 1, 2)

        self.Email = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Email.setObjectName(u"Email")
        self.Email.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Email, 21, 6, 1, 11)

        self.DumaAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DumaAddress.setObjectName(u"DumaAddress")
        self.DumaAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DumaAddress, 11, 1, 1, 16)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_10, 10, 1, 1, 1)

        self.Mother_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Mother_FirstName.setObjectName(u"Mother_FirstName")
        self.Mother_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Mother_FirstName, 32, 1, 1, 6)

        self.MotherJob = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherJob.setObjectName(u"MotherJob")
        self.MotherJob.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherJob, 32, 10, 1, 7)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_36, 41, 1, 1, 2)

        self.employee_picture = QLabel(self.scrollAreaWidgetContents_2)
        self.employee_picture.setObjectName(u"employee_picture")
        self.employee_picture.setStyleSheet(u"color:black;\n"
"background-color:white;")

        self.gridLayout.addWidget(self.employee_picture, 4, 0, 1, 1)

        self.highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.highschool.setObjectName(u"highschool")
        self.highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.highschool, 44, 1, 1, 16)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_23, 24, 1, 1, 2)

        self.publications = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.publications.setObjectName(u"publications")
        self.publications.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.publications, 56, 1, 1, 16)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_25, 26, 1, 1, 2)

        self.Father_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Father_MiddleName.setObjectName(u"Father_MiddleName")
        self.Father_MiddleName.setMinimumSize(QSize(200, 0))
        self.Father_MiddleName.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.Father_MiddleName, 29, 7, 1, 2)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_11, 12, 1, 1, 1)

        self.NONFILIPINO_passport = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_passport.setObjectName(u"NONFILIPINO_passport")
        self.NONFILIPINO_passport.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_passport, 19, 1, 1, 7)

        self.criminalcases_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.criminalcases_ignore.setObjectName(u"criminalcases_ignore")
        self.criminalcases_ignore.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.criminalcases_ignore, 62, 16, 1, 1)

        self.Position = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Position.setObjectName(u"Position")
        self.Position.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Position, 6, 1, 1, 16)

        self.staff_FirstName2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_FirstName2.setObjectName(u"staff_FirstName2")
        self.staff_FirstName2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_FirstName2, 52, 1, 1, 1)

        self.Siblings_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.Siblings_ignore.setObjectName(u"Siblings_ignore")
        self.Siblings_ignore.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.Siblings_ignore, 34, 16, 1, 1)

        self.address_employment = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_employment.setObjectName(u"address_employment")
        self.address_employment.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_employment, 59, 1, 1, 16)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_41, 60, 1, 1, 2)

        self.Spouse_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Spouse_FirstName.setObjectName(u"Spouse_FirstName")
        self.Spouse_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Spouse_FirstName, 38, 2, 1, 4)

        self.HomeAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.HomeAddress.setObjectName(u"HomeAddress")
        self.HomeAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.HomeAddress, 13, 1, 2, 16)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_31, 37, 1, 1, 1)

        self.NONFILIPINO_acrnum = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_acrnum.setObjectName(u"NONFILIPINO_acrnum")
        self.NONFILIPINO_acrnum.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_acrnum, 19, 8, 1, 8)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_35, 39, 1, 1, 2)

        self.Father_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Father_FirstName.setObjectName(u"Father_FirstName")
        self.Father_FirstName.setMaximumSize(QSize(400, 16777215))
        self.Father_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Father_FirstName, 29, 1, 1, 6)

        self.government_examination = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.government_examination.setObjectName(u"government_examination")
        self.government_examination.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.government_examination, 61, 1, 1, 2)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_34, 37, 15, 1, 2)

        self.ChurchAffiliation_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.ChurchAffiliation_ignore.setObjectName(u"ChurchAffiliation_ignore")
        self.ChurchAffiliation_ignore.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.ChurchAffiliation_ignore, 26, 16, 1, 1)

        self.College = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.College.setObjectName(u"College")
        self.College.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.College, 46, 1, 1, 16)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_30, 34, 1, 1, 2)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(128, 178, 65);\n"
"color: rgb(255, 255, 255);\n"
"font: 800 10pt \"Segoe UI\";\n"
"padding:5px;\n"
"border:none;\n"
"")

        self.gridLayout.addWidget(self.pushButton, 0, 16, 1, 1)

        self.scholarships_awards = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.scholarships_awards.setObjectName(u"scholarships_awards")
        self.scholarships_awards.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.scholarships_awards, 54, 1, 1, 16)

        self.government_rating = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.government_rating.setObjectName(u"government_rating")
        self.government_rating.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.government_rating, 61, 3, 1, 4)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"border:none;\n"
"font: 9pt \"Outfit\";")

        self.gridLayout.addWidget(self.label_15, 17, 1, 1, 2)

        self.staff_relationship2_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_relationship2_2.setObjectName(u"staff_relationship2_2")
        self.staff_relationship2_2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_relationship2_2, 52, 5, 1, 8)

        self.staff_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.staff_ignore.setObjectName(u"staff_ignore")
        self.staff_ignore.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.staff_ignore, 50, 15, 1, 2)

        self.Graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Graduateschool.setObjectName(u"Graduateschool")
        self.Graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Graduateschool, 48, 1, 1, 16)

        self.record_employee_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.record_employee_ignore.setObjectName(u"record_employee_ignore")
        self.record_employee_ignore.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.record_employee_ignore, 57, 14, 1, 3)

        self.civilstatus_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.civilstatus_ignore.setObjectName(u"civilstatus_ignore")
        self.civilstatus_ignore.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.civilstatus_ignore, 36, 16, 1, 1)

        self.sibling1_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_FirstName.setObjectName(u"sibling1_FirstName")
        self.sibling1_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling1_FirstName, 35, 1, 1, 1)

        self.staff_position3 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_position3.setObjectName(u"staff_position3")
        self.staff_position3.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_position3, 51, 13, 1, 4)

        self.child1_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_MiddleName.setObjectName(u"child1_MiddleName")

        self.gridLayout.addWidget(self.child1_MiddleName, 40, 6, 1, 4)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:black;\n"
"font: 600 14pt \"Outfit SemiBold\";\n"
"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.Mother_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Mother_LastName.setObjectName(u"Mother_LastName")

        self.gridLayout.addWidget(self.Mother_LastName, 32, 9, 1, 1)

        self.DateOfBirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DateOfBirth.setObjectName(u"DateOfBirth")
        self.DateOfBirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DateOfBirth, 16, 1, 1, 1)

        self.label_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_32, 37, 2, 1, 2)

        self.Mother_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Mother_MiddleName.setObjectName(u"Mother_MiddleName")

        self.gridLayout.addWidget(self.Mother_MiddleName, 32, 7, 1, 2)

        self.Image_Upload = QPushButton(self.scrollAreaWidgetContents_2)
        self.Image_Upload.setObjectName(u"Image_Upload")
        self.Image_Upload.setCursor(QCursor(Qt.PointingHandCursor))
        self.Image_Upload.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(128, 178, 65);\n"
"color: rgb(255, 255, 255);\n"
"font: 800 10pt \"Segoe UI\";\n"
"padding:5px;\n"
"border:none;\n"
"")

        self.gridLayout.addWidget(self.Image_Upload, 1, 0, 1, 1)

        self.elementary_school = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.elementary_school.setObjectName(u"elementary_school")
        self.elementary_school.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.elementary_school, 42, 1, 1, 16)

        self.diploma_college = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_college.setObjectName(u"diploma_college")
        self.diploma_college.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_college, 47, 4, 1, 9)

        self.DateOfMarriage = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DateOfMarriage.setObjectName(u"DateOfMarriage")
        self.DateOfMarriage.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DateOfMarriage, 38, 15, 1, 2)

        self.EmployeeImageLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.EmployeeImageLabel.setObjectName(u"EmployeeImageLabel")
        self.EmployeeImageLabel.setStyleSheet(u"color:black;\n"
"background-color:white;")

        self.gridLayout.addWidget(self.EmployeeImageLabel, 5, 0, 1, 1)

        self.reason = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.reason.setObjectName(u"reason")
        self.reason.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.reason, 58, 12, 1, 5)

        self.sibling1_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_LastName.setObjectName(u"sibling1_LastName")

        self.gridLayout.addWidget(self.sibling1_LastName, 35, 4, 1, 1)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_42, 62, 1, 1, 2)

        self.staff_position2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_position2.setObjectName(u"staff_position2")
        self.staff_position2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_position2, 52, 13, 1, 4)

        self.FatherJob = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherJob.setObjectName(u"FatherJob")
        self.FatherJob.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherJob, 29, 10, 1, 7)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_19, 20, 1, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_28, 31, 1, 1, 2)

        self.yeargraduate_college = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_college.setObjectName(u"yeargraduate_college")
        self.yeargraduate_college.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_college, 47, 13, 1, 4)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_7, 2, 11, 1, 3)

        self.SurName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SurName.setObjectName(u"SurName")
        self.SurName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SurName, 4, 11, 1, 6)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_38, 53, 1, 1, 2)

        self.PagIbigNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PagIbigNumber.setObjectName(u"PagIbigNumber")
        self.PagIbigNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PagIbigNumber, 25, 1, 1, 7)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_14, 15, 10, 1, 4)

        self.yeargraduate_graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_graduateschool.setObjectName(u"yeargraduate_graduateschool")
        self.yeargraduate_graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_graduateschool, 49, 13, 1, 4)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_17, 18, 8, 1, 2)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.checkBox, 0, 11, 1, 5)

        self.yeargraduate_highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_highschool.setObjectName(u"yeargraduate_highschool")
        self.yeargraduate_highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_highschool, 45, 13, 1, 4)

        self.Department = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Department.setObjectName(u"Department")
        self.Department.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Department, 8, 1, 1, 16)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_39, 55, 1, 1, 2)

        self.child1_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_FirstName.setObjectName(u"child1_FirstName")
        self.child1_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.child1_FirstName, 40, 1, 1, 5)

        self.PlaceOfBirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PlaceOfBirth.setObjectName(u"PlaceOfBirth")
        self.PlaceOfBirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PlaceOfBirth, 16, 2, 1, 8)

        self.government_date = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.government_date.setObjectName(u"government_date")
        self.government_date.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.government_date, 61, 7, 1, 5)

        self.diploma_highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_highschool.setObjectName(u"diploma_highschool")
        self.diploma_highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_highschool, 45, 4, 1, 9)

        self.children_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.children_ignore.setObjectName(u"children_ignore")
        self.children_ignore.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.children_ignore, 39, 16, 1, 1)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_26, 28, 1, 1, 2)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)

        self.government_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.government_ignore.setObjectName(u"government_ignore")
        self.government_ignore.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.government_ignore, 60, 16, 1, 1)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_33, 37, 10, 1, 1)

        self.address_graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_graduateschool.setObjectName(u"address_graduateschool")
        self.address_graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_graduateschool, 49, 1, 1, 3)

        self.name_employer = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.name_employer.setObjectName(u"name_employer")
        self.name_employer.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.name_employer, 58, 1, 1, 2)

        self.NONFILIPINO_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_ignore.setObjectName(u"NONFILIPINO_ignore")
        self.NONFILIPINO_ignore.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.NONFILIPINO_ignore, 17, 16, 1, 1)

        self.Government_place = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Government_place.setObjectName(u"Government_place")
        self.Government_place.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Government_place, 61, 12, 1, 5)

        self.TINnumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.TINnumber.setObjectName(u"TINnumber")
        self.TINnumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.TINnumber, 23, 1, 1, 7)

        self.FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FirstName.setObjectName(u"FirstName")
        self.FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";\n"
"")

        self.gridLayout.addWidget(self.FirstName, 4, 1, 1, 4)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_24, 24, 8, 1, 4)

        self.child1_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_LastName.setObjectName(u"child1_LastName")

        self.gridLayout.addWidget(self.child1_LastName, 40, 10, 1, 3)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_13, 15, 2, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_18, 18, 16, 1, 1)

        self.position_workplace = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.position_workplace.setObjectName(u"position_workplace")
        self.position_workplace.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.position_workplace, 58, 3, 1, 6)

        self.yeargraduate_elementary = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_elementary.setObjectName(u"yeargraduate_elementary")
        self.yeargraduate_elementary.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_elementary, 43, 13, 1, 4)

        self.NONFILIPINO_dateissued = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_dateissued.setObjectName(u"NONFILIPINO_dateissued")
        self.NONFILIPINO_dateissued.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_dateissued, 19, 16, 1, 1)

        self.address_highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_highschool.setObjectName(u"address_highschool")
        self.address_highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_highschool, 45, 1, 1, 3)

        self.ContactNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.ContactNumber.setObjectName(u"ContactNumber")
        self.ContactNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.ContactNumber, 21, 1, 1, 5)

        self.period_employment = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.period_employment.setObjectName(u"period_employment")
        self.period_employment.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.period_employment, 58, 9, 1, 3)

        self.MotherAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherAddress.setObjectName(u"MotherAddress")
        self.MotherAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherAddress, 33, 1, 1, 16)

        self.address_college = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_college.setObjectName(u"address_college")
        self.address_college.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_college, 47, 1, 1, 3)

        self.PhilHNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PhilHNumber.setObjectName(u"PhilHNumber")
        self.PhilHNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PhilHNumber, 25, 8, 1, 9)

        self.staff_LastName1 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_LastName1.setObjectName(u"staff_LastName1")

        self.gridLayout.addWidget(self.staff_LastName1, 51, 4, 1, 1)

        self.diploma_graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_graduateschool.setObjectName(u"diploma_graduateschool")
        self.diploma_graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_graduateschool, 49, 4, 1, 9)

        self.Citizenship = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Citizenship.setObjectName(u"Citizenship")
        self.Citizenship.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Citizenship, 16, 10, 1, 7)

        self.sibling1_occupation = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_occupation.setObjectName(u"sibling1_occupation")
        self.sibling1_occupation.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling1_occupation, 35, 6, 1, 8)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_20, 20, 6, 1, 3)

        self.sibling1_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_MiddleName.setObjectName(u"sibling1_MiddleName")

        self.gridLayout.addWidget(self.sibling1_MiddleName, 35, 2, 1, 2)

        self.staff_MiddleName2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_MiddleName2.setObjectName(u"staff_MiddleName2")

        self.gridLayout.addWidget(self.staff_MiddleName2, 52, 2, 1, 2)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_37, 50, 1, 1, 2)

        self.staff_LastName2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_LastName2.setObjectName(u"staff_LastName2")

        self.gridLayout.addWidget(self.staff_LastName2, 52, 4, 1, 1)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_40, 57, 1, 1, 2)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_22, 22, 8, 1, 4)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_16, 18, 1, 1, 1)

        self.CivilStatus = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus.setObjectName(u"CivilStatus")
        self.CivilStatus.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus, 38, 1, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_9, 7, 1, 1, 1)

        self.Father_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Father_LastName.setObjectName(u"Father_LastName")

        self.gridLayout.addWidget(self.Father_LastName, 29, 9, 1, 1)

        self.PlaceOfMarriage = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PlaceOfMarriage.setObjectName(u"PlaceOfMarriage")
        self.PlaceOfMarriage.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PlaceOfMarriage, 38, 10, 1, 5)

        self.SSSnumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SSSnumber.setObjectName(u"SSSnumber")
        self.SSSnumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SSSnumber, 23, 8, 1, 9)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_12, 15, 1, 1, 1)

        self.sibling1_address = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_address.setObjectName(u"sibling1_address")
        self.sibling1_address.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling1_address, 35, 14, 1, 3)

        self.Spouse_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Spouse_LastName.setObjectName(u"Spouse_LastName")

        self.gridLayout.addWidget(self.Spouse_LastName, 38, 8, 1, 2)

        self.MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MiddleName.setObjectName(u"MiddleName")
        self.MiddleName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MiddleName, 4, 5, 1, 6)

        self.FatherAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherAddress.setObjectName(u"FatherAddress")
        self.FatherAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherAddress, 30, 1, 1, 16)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


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
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Silliman University ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Personnel Record Dashboard", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.diploma_elementary.setPlainText("")
        self.diploma_elementary.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.child1_dateofbirth.setPlainText("")
        self.child1_dateofbirth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Date of birth...", None))
        self.elementary_school_address.setPlainText("")
        self.elementary_school_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address of elementary school...", None))
        self.case_name.setPlainText("")
        self.case_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Case name...", None))
        self.staff_MiddleName1.setPlainText("")
        self.staff_MiddleName1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Tax Identification Number", None))
        self.staff_FirstName1.setPlainText("")
        self.staff_FirstName1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.staff_relationship2.setPlainText("")
        self.staff_relationship2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Relationship...", None))
        self.ChurchAffiliation.setPlainText("")
        self.ChurchAffiliation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Church affiliation...", None))
        self.Spouse_MiddleName.setPlainText("")
        self.Spouse_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.Email.setPlainText("")
        self.Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail address...", None))
        self.DumaAddress.setPlainText("")
        self.DumaAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Dumaguete address...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dumaguete address", None))
        self.Mother_FirstName.setPlainText("")
        self.Mother_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.MotherJob.setPlainText("")
        self.MotherJob.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mother's occupation...", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Academic record", None))
        self.employee_picture.setText(QCoreApplication.translate("MainWindow", u"Profile Picture", None))
        self.highschool.setPlainText("")
        self.highschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"High School...", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Pag-Ibig Number", None))
        self.publications.setPlainText("")
        self.publications.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Includes thesis papers, and other publications ...", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Church affiliation", None))
        self.Father_MiddleName.setPlainText("")
        self.Father_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Home address", None))
        self.NONFILIPINO_passport.setPlainText("")
        self.NONFILIPINO_passport.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Passport number...", None))
        self.criminalcases_ignore.setText(QCoreApplication.translate("MainWindow", u"Does not apply", None))
        self.Position.setPlainText("")
        self.Position.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.staff_FirstName2.setPlainText("")
        self.staff_FirstName2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.Siblings_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no siblings.", None))
        self.address_employment.setPlainText("")
        self.address_employment.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Government examination(s) passed", None))
        self.Spouse_FirstName.setPlainText("")
        self.Spouse_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.HomeAddress.setPlainText("")
        self.HomeAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full home address...", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Civil status", None))
        self.NONFILIPINO_acrnum.setPlainText("")
        self.NONFILIPINO_acrnum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ACR number...", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Children (if any)", None))
        self.Father_FirstName.setPlainText("")
        self.Father_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.government_examination.setPlainText("")
        self.government_examination.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Examination...", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Date of marriage", None))
        self.ChurchAffiliation_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no church affiliation.", None))
        self.College.setPlainText("")
        self.College.setPlaceholderText(QCoreApplication.translate("MainWindow", u"College...", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Sibling(s)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.scholarships_awards.setPlainText("")
        self.scholarships_awards.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Includes scholarships, awards, etc ...", None))
        self.government_rating.setPlainText("")
        self.government_rating.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rating...", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"If non-Filipino*, please fill the following fields...", None))
        self.staff_relationship2_2.setPlainText("")
        self.staff_relationship2_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Relationship...", None))
        self.staff_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee is not related to any staff.", None))
        self.Graduateschool.setPlainText("")
        self.Graduateschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Graduate School...", None))
        self.record_employee_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no record of prior employment.", None))
        self.civilstatus_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee is unmarried.", None))
        self.sibling1_FirstName.setPlainText("")
        self.sibling1_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sibling's first name...", None))
        self.staff_position3.setPlainText("")
        self.staff_position3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.child1_MiddleName.setPlainText("")
        self.child1_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adding Employee Record", None))
        self.Mother_LastName.setPlainText("")
        self.Mother_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.DateOfBirth.setPlainText("")
        self.DateOfBirth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Name of spouse", None))
        self.Mother_MiddleName.setPlainText("")
        self.Mother_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.Image_Upload.setText(QCoreApplication.translate("MainWindow", u"Upload Employee Image", None))
        self.elementary_school.setPlainText("")
        self.elementary_school.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Elementary School...", None))
        self.diploma_college.setPlainText("")
        self.diploma_college.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.DateOfMarriage.setPlainText("")
        self.DateOfMarriage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.EmployeeImageLabel.setText(QCoreApplication.translate("MainWindow", u"(image name here)", None))
        self.reason.setPlainText("")
        self.reason.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Reason for leaving...", None))
        self.sibling1_LastName.setPlainText("")
        self.sibling1_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Involvement in criminal case(s)*", None))
        self.staff_position2.setPlainText("")
        self.staff_position2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.FatherJob.setPlainText("")
        self.FatherJob.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Father's occupation...", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Contact number", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Mother", None))
        self.yeargraduate_college.setPlainText("")
        self.yeargraduate_college.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.label_7.setText("")
        self.SurName.setPlainText("")
        self.SurName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Surname...", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"School or college distinction(s)", None))
        self.PagIbigNumber.setPlainText("")
        self.PagIbigNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pag-Ibig No. ...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Citizenship", None))
        self.yeargraduate_graduateschool.setPlainText("")
        self.yeargraduate_graduateschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ACR number", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"This confirms that all details are true.", None))
        self.yeargraduate_highschool.setPlainText("")
        self.yeargraduate_highschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.Department.setPlainText("")
        self.Department.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Department...", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Publication(s)", None))
        self.child1_FirstName.setPlainText("")
        self.child1_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.PlaceOfBirth.setPlainText("")
        self.PlaceOfBirth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Place of birth...", None))
        self.government_date.setPlainText("")
        self.government_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Date of examination...", None))
        self.diploma_highschool.setPlainText("")
        self.diploma_highschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.children_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no children.", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Father", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Position(s)", None))
        self.government_ignore.setText(QCoreApplication.translate("MainWindow", u"Does not apply", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Place of marriage", None))
        self.address_graduateschool.setPlainText("")
        self.address_graduateschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address of graduate school...", None))
        self.name_employer.setPlainText("")
        self.name_employer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of employer...", None))
        self.NONFILIPINO_ignore.setText(QCoreApplication.translate("MainWindow", u"Ignore fields", None))
        self.Government_place.setPlainText("")
        self.Government_place.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Place...", None))
        self.TINnumber.setPlainText("")
        self.TINnumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TIN...", None))
        self.FirstName.setPlainText("")
        self.FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Philhealth Number", None))
        self.child1_LastName.setPlainText("")
        self.child1_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Place of birth", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Date issued", None))
        self.position_workplace.setPlainText("")
        self.position_workplace.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Position at workplace...", None))
        self.yeargraduate_elementary.setPlainText("")
        self.yeargraduate_elementary.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.NONFILIPINO_dateissued.setPlainText("")
        self.NONFILIPINO_dateissued.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.address_highschool.setPlainText("")
        self.address_highschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address of high school...", None))
        self.ContactNumber.setPlainText("")
        self.ContactNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contact number...", None))
        self.period_employment.setPlainText("")
        self.period_employment.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Period of employment...", None))
        self.MotherAddress.setPlainText("")
        self.MotherAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mother's current home address...", None))
        self.address_college.setPlainText("")
        self.address_college.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address of College...", None))
        self.PhilHNumber.setPlainText("")
        self.PhilHNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Philhealth No. ...", None))
        self.staff_LastName1.setPlainText("")
        self.staff_LastName1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.diploma_graduateschool.setPlainText("")
        self.diploma_graduateschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.Citizenship.setPlainText("")
        self.Citizenship.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Citizenship...", None))
        self.sibling1_occupation.setPlainText("")
        self.sibling1_occupation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Occupation...", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"E-mail address", None))
        self.sibling1_MiddleName.setPlainText("")
        self.sibling1_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.staff_MiddleName2.setPlainText("")
        self.staff_MiddleName2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Related staff member(s)", None))
        self.staff_LastName2.setPlainText("")
        self.staff_LastName2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Record of previous employment", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SSS Number", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Passport number", None))
        self.CivilStatus.setPlainText("")
        self.CivilStatus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Civil status...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Department(s)", None))
        self.Father_LastName.setPlainText("")
        self.Father_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.PlaceOfMarriage.setPlainText("")
        self.PlaceOfMarriage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.SSSnumber.setPlainText("")
        self.SSSnumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SSS...", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Date of birth", None))
        self.sibling1_address.setPlainText("")
        self.sibling1_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.Spouse_LastName.setPlainText("")
        self.Spouse_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.MiddleName.setPlainText("")
        self.MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.FatherAddress.setPlainText("")
        self.FatherAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Father's current home address...", None))
    # retranslateUi

