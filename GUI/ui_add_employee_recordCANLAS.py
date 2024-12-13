# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_employee_recordCANLASakZKTV.ui'
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -1969, 1429, 2576))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"color:black;\n"
"background-color:white;\n"
"border: 1px solid black")
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Position = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Position.setObjectName(u"Position")
        self.Position.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Position, 6, 1, 1, 16)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_14, 15, 10, 1, 4)

        self.elementary_school = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.elementary_school.setObjectName(u"elementary_school")
        self.elementary_school.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.elementary_school, 41, 1, 1, 16)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_38, 52, 1, 1, 2)

        self.staff_position2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_position2.setObjectName(u"staff_position2")
        self.staff_position2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_position2, 51, 13, 1, 4)

        self.staff_MiddleName1 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_MiddleName1.setObjectName(u"staff_MiddleName1")

        self.gridLayout.addWidget(self.staff_MiddleName1, 50, 2, 1, 2)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_19, 20, 1, 1, 1)

        self.FatherAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherAddress.setObjectName(u"FatherAddress")
        self.FatherAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherAddress, 30, 1, 1, 16)

        self.MotherAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherAddress.setObjectName(u"MotherAddress")
        self.MotherAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherAddress, 33, 1, 1, 16)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_30, 34, 1, 1, 2)

        self.NONFILIPINO_passport = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_passport.setObjectName(u"NONFILIPINO_passport")
        self.NONFILIPINO_passport.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_passport, 19, 1, 1, 7)

        self.ContactNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.ContactNumber.setObjectName(u"ContactNumber")
        self.ContactNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.ContactNumber, 21, 1, 1, 5)

        self.NONFILIPINO_dateissued = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_dateissued.setObjectName(u"NONFILIPINO_dateissued")
        self.NONFILIPINO_dateissued.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_dateissued, 19, 16, 1, 1)

        self.staff_relationship2_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_relationship2_2.setObjectName(u"staff_relationship2_2")
        self.staff_relationship2_2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_relationship2_2, 51, 5, 1, 8)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_25, 26, 1, 1, 2)

        self.staff_position3 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_position3.setObjectName(u"staff_position3")
        self.staff_position3.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_position3, 50, 13, 1, 4)

        self.Government_place = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Government_place.setObjectName(u"Government_place")
        self.Government_place.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Government_place, 57, 12, 1, 5)

        self.NONFILIPINO_acrnum = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_acrnum.setObjectName(u"NONFILIPINO_acrnum")
        self.NONFILIPINO_acrnum.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_acrnum, 19, 8, 1, 8)

        self.diploma_college = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_college.setObjectName(u"diploma_college")
        self.diploma_college.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_college, 46, 4, 1, 9)

        self.Email = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Email.setObjectName(u"Email")
        self.Email.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Email, 21, 6, 1, 11)

        self.DateOfBirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DateOfBirth.setObjectName(u"DateOfBirth")
        self.DateOfBirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DateOfBirth, 16, 1, 1, 1)

        self.yeargraduate_college = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_college.setObjectName(u"yeargraduate_college")
        self.yeargraduate_college.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_college, 46, 13, 1, 4)

        self.Department = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Department.setObjectName(u"Department")
        self.Department.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Department, 8, 1, 1, 16)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_31, 36, 1, 1, 1)

        self.government_examination = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.government_examination.setObjectName(u"government_examination")
        self.government_examination.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.government_examination, 57, 1, 1, 2)

        self.DateOfMarriage = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DateOfMarriage.setObjectName(u"DateOfMarriage")
        self.DateOfMarriage.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DateOfMarriage, 37, 15, 1, 2)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_23, 24, 1, 1, 2)

        self.EmployeeImageLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.EmployeeImageLabel.setObjectName(u"EmployeeImageLabel")
        self.EmployeeImageLabel.setStyleSheet(u"color:black;\n"
"background-color:white;")

        self.gridLayout.addWidget(self.EmployeeImageLabel, 5, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_7, 2, 11, 1, 3)

        self.address_graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_graduateschool.setObjectName(u"address_graduateschool")
        self.address_graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_graduateschool, 48, 1, 1, 3)

        self.child1_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_LastName.setObjectName(u"child1_LastName")

        self.gridLayout.addWidget(self.child1_LastName, 39, 10, 1, 3)

        self.Spouse_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Spouse_LastName.setObjectName(u"Spouse_LastName")

        self.gridLayout.addWidget(self.Spouse_LastName, 37, 8, 1, 2)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_34, 36, 15, 1, 2)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_36, 40, 1, 1, 2)

        self.College = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.College.setObjectName(u"College")
        self.College.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.College, 45, 1, 1, 16)

        self.ChurchAffiliation = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.ChurchAffiliation.setObjectName(u"ChurchAffiliation")
        self.ChurchAffiliation.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.ChurchAffiliation, 27, 1, 1, 16)

        self.staff_LastName1 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_LastName1.setObjectName(u"staff_LastName1")

        self.gridLayout.addWidget(self.staff_LastName1, 50, 4, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_24, 24, 8, 1, 4)

        self.Father_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Father_LastName.setObjectName(u"Father_LastName")

        self.gridLayout.addWidget(self.Father_LastName, 29, 9, 1, 1)

        self.DumaAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DumaAddress.setObjectName(u"DumaAddress")
        self.DumaAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DumaAddress, 11, 1, 1, 16)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_20, 20, 6, 1, 3)

        self.staff_relationship2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_relationship2.setObjectName(u"staff_relationship2")
        self.staff_relationship2.setMaximumSize(QSize(16777215, 16777215))
        self.staff_relationship2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_relationship2, 50, 5, 1, 8)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_21, 22, 1, 1, 2)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.checkBox, 0, 11, 1, 5)

        self.sibling1_address = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_address.setObjectName(u"sibling1_address")
        self.sibling1_address.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling1_address, 35, 14, 1, 3)

        self.sibling1_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_FirstName.setObjectName(u"sibling1_FirstName")
        self.sibling1_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling1_FirstName, 35, 1, 1, 1)

        self.sibling1_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_LastName.setObjectName(u"sibling1_LastName")

        self.gridLayout.addWidget(self.sibling1_LastName, 35, 4, 1, 1)

        self.sibling1_occupation = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_occupation.setObjectName(u"sibling1_occupation")
        self.sibling1_occupation.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling1_occupation, 35, 6, 1, 8)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_33, 36, 10, 1, 1)

        self.MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MiddleName.setObjectName(u"MiddleName")
        self.MiddleName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MiddleName, 4, 5, 1, 6)

        self.address_highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_highschool.setObjectName(u"address_highschool")
        self.address_highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_highschool, 44, 1, 1, 3)

        self.government_date = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.government_date.setObjectName(u"government_date")
        self.government_date.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.government_date, 57, 7, 1, 5)

        self.scholarships_awards = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.scholarships_awards.setObjectName(u"scholarships_awards")
        self.scholarships_awards.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.scholarships_awards, 53, 1, 1, 16)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_39, 54, 1, 1, 2)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_22, 22, 8, 1, 4)

        self.elementary_school_address = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.elementary_school_address.setObjectName(u"elementary_school_address")
        self.elementary_school_address.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.elementary_school_address, 42, 1, 1, 3)

        self.yeargraduate_elementary = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_elementary.setObjectName(u"yeargraduate_elementary")
        self.yeargraduate_elementary.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_elementary, 42, 13, 1, 4)

        self.yeargraduate_graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_graduateschool.setObjectName(u"yeargraduate_graduateschool")
        self.yeargraduate_graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_graduateschool, 48, 13, 1, 4)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_9, 7, 1, 1, 1)

        self.Mother_LastName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Mother_LastName.setObjectName(u"Mother_LastName")

        self.gridLayout.addWidget(self.Mother_LastName, 32, 9, 1, 1)

        self.Spouse_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Spouse_FirstName.setObjectName(u"Spouse_FirstName")
        self.Spouse_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Spouse_FirstName, 37, 2, 1, 4)

        self.PlaceOfMarriage = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PlaceOfMarriage.setObjectName(u"PlaceOfMarriage")
        self.PlaceOfMarriage.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PlaceOfMarriage, 37, 10, 1, 5)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_42, 58, 1, 1, 2)

        self.TINnumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.TINnumber.setObjectName(u"TINnumber")
        self.TINnumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.TINnumber, 23, 1, 1, 7)

        self.employee_picture = QLabel(self.scrollAreaWidgetContents_2)
        self.employee_picture.setObjectName(u"employee_picture")
        self.employee_picture.setStyleSheet(u"color:black;\n"
"background-color:white;")

        self.gridLayout.addWidget(self.employee_picture, 4, 0, 1, 1)

        self.publications = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.publications.setObjectName(u"publications")
        self.publications.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.publications, 55, 1, 1, 16)

        self.Spouse_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Spouse_MiddleName.setObjectName(u"Spouse_MiddleName")

        self.gridLayout.addWidget(self.Spouse_MiddleName, 37, 6, 1, 2)

        self.FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FirstName.setObjectName(u"FirstName")
        self.FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";\n"
"")

        self.gridLayout.addWidget(self.FirstName, 4, 1, 1, 4)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:black;\n"
"font: 600 14pt \"Outfit SemiBold\";\n"
"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_41, 56, 1, 1, 2)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"\n"
"background-color:white;\n"
"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_17, 18, 8, 1, 2)

        self.child1_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_FirstName.setObjectName(u"child1_FirstName")
        self.child1_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.child1_FirstName, 39, 1, 1, 5)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"border:none;\n"
"font: 9pt \"Outfit\";")

        self.gridLayout.addWidget(self.label_15, 17, 1, 1, 2)

        self.Citizenship = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Citizenship.setObjectName(u"Citizenship")
        self.Citizenship.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Citizenship, 16, 10, 1, 7)

        self.PlaceOfBirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PlaceOfBirth.setObjectName(u"PlaceOfBirth")
        self.PlaceOfBirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PlaceOfBirth, 16, 2, 1, 8)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_10, 10, 1, 1, 1)

        self.staff_MiddleName2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_MiddleName2.setObjectName(u"staff_MiddleName2")

        self.gridLayout.addWidget(self.staff_MiddleName2, 51, 2, 1, 2)

        self.HomeAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.HomeAddress.setObjectName(u"HomeAddress")
        self.HomeAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.HomeAddress, 13, 1, 2, 16)

        self.staff_FirstName1 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_FirstName1.setObjectName(u"staff_FirstName1")
        self.staff_FirstName1.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_FirstName1, 50, 1, 1, 1)

        self.FatherJob = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherJob.setObjectName(u"FatherJob")
        self.FatherJob.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherJob, 29, 10, 1, 7)

        self.child1_dateofbirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_dateofbirth.setObjectName(u"child1_dateofbirth")
        self.child1_dateofbirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.child1_dateofbirth, 39, 13, 1, 4)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_16, 18, 1, 1, 1)

        self.government_rating = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.government_rating.setObjectName(u"government_rating")
        self.government_rating.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.government_rating, 57, 3, 1, 4)

        self.child1_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_MiddleName.setObjectName(u"child1_MiddleName")

        self.gridLayout.addWidget(self.child1_MiddleName, 39, 6, 1, 4)

        self.diploma_highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_highschool.setObjectName(u"diploma_highschool")
        self.diploma_highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_highschool, 44, 4, 1, 9)

        self.MotherJob = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherJob.setObjectName(u"MotherJob")
        self.MotherJob.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherJob, 32, 10, 1, 7)

        self.Father_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Father_MiddleName.setObjectName(u"Father_MiddleName")
        self.Father_MiddleName.setMinimumSize(QSize(200, 0))
        self.Father_MiddleName.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.Father_MiddleName, 29, 7, 1, 2)

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

        self.diploma_graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_graduateschool.setObjectName(u"diploma_graduateschool")
        self.diploma_graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_graduateschool, 48, 4, 1, 9)

        self.address_college = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_college.setObjectName(u"address_college")
        self.address_college.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_college, 46, 1, 1, 3)

        self.label_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_32, 36, 2, 1, 2)

        self.Mother_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Mother_MiddleName.setObjectName(u"Mother_MiddleName")

        self.gridLayout.addWidget(self.Mother_MiddleName, 32, 7, 1, 2)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_28, 31, 1, 1, 2)

        self.staff_FirstName2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_FirstName2.setObjectName(u"staff_FirstName2")
        self.staff_FirstName2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_FirstName2, 51, 1, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_18, 18, 16, 1, 1)

        self.Father_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Father_FirstName.setObjectName(u"Father_FirstName")
        self.Father_FirstName.setMaximumSize(QSize(400, 16777215))
        self.Father_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Father_FirstName, 29, 1, 1, 6)

        self.PagIbigNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PagIbigNumber.setObjectName(u"PagIbigNumber")
        self.PagIbigNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PagIbigNumber, 25, 1, 1, 7)

        self.highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.highschool.setObjectName(u"highschool")
        self.highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.highschool, 43, 1, 1, 16)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)

        self.SurName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SurName.setObjectName(u"SurName")
        self.SurName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SurName, 4, 11, 1, 6)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_35, 38, 1, 1, 2)

        self.PhilHNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PhilHNumber.setObjectName(u"PhilHNumber")
        self.PhilHNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PhilHNumber, 25, 8, 1, 9)

        self.sibling1_MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_MiddleName.setObjectName(u"sibling1_MiddleName")

        self.gridLayout.addWidget(self.sibling1_MiddleName, 35, 2, 1, 2)

        self.CivilStatus = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus.setObjectName(u"CivilStatus")
        self.CivilStatus.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus, 37, 1, 1, 1)

        self.SSSnumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SSSnumber.setObjectName(u"SSSnumber")
        self.SSSnumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SSSnumber, 23, 8, 1, 9)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_12, 15, 1, 1, 1)

        self.Mother_FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Mother_FirstName.setObjectName(u"Mother_FirstName")
        self.Mother_FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Mother_FirstName, 32, 1, 1, 6)

        self.yeargraduate_highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_highschool.setObjectName(u"yeargraduate_highschool")
        self.yeargraduate_highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_highschool, 44, 13, 1, 4)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_13, 15, 2, 1, 1)

        self.diploma_elementary = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_elementary.setObjectName(u"diploma_elementary")
        self.diploma_elementary.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_elementary, 42, 4, 1, 9)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_37, 49, 1, 1, 2)

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

        self.label_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_26, 28, 1, 1, 2)

        self.Graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Graduateschool.setObjectName(u"Graduateschool")
        self.Graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Graduateschool, 47, 1, 1, 16)

        self.case_name = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.case_name.setObjectName(u"case_name")
        self.case_name.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.case_name, 59, 1, 1, 16)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"border:none;\n"
"")

        self.gridLayout.addWidget(self.label_11, 12, 1, 1, 1)

        self.staff_LastName2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_LastName2.setObjectName(u"staff_LastName2")

        self.gridLayout.addWidget(self.staff_LastName2, 51, 4, 1, 1)

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
        self.Position.setPlainText("")
        self.Position.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Citizenship", None))
        self.elementary_school.setPlainText("")
        self.elementary_school.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Elementary School...", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"School or college distinction(s)", None))
        self.staff_position2.setPlainText("")
        self.staff_position2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.staff_MiddleName1.setPlainText("")
        self.staff_MiddleName1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Contact number", None))
        self.FatherAddress.setPlainText("")
        self.FatherAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Father's current home address...", None))
        self.MotherAddress.setPlainText("")
        self.MotherAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mother's current home address...", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Sibling(s)", None))
        self.NONFILIPINO_passport.setPlainText("")
        self.NONFILIPINO_passport.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Passport number...", None))
        self.ContactNumber.setPlainText("")
        self.ContactNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contact number...", None))
        self.NONFILIPINO_dateissued.setPlainText("")
        self.NONFILIPINO_dateissued.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.staff_relationship2_2.setPlainText("")
        self.staff_relationship2_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Relationship...", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Church affiliation", None))
        self.staff_position3.setPlainText("")
        self.staff_position3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.Government_place.setPlainText("")
        self.Government_place.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Place...", None))
        self.NONFILIPINO_acrnum.setPlainText("")
        self.NONFILIPINO_acrnum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ACR number...", None))
        self.diploma_college.setPlainText("")
        self.diploma_college.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.Email.setPlainText("")
        self.Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail address...", None))
        self.DateOfBirth.setPlainText("")
        self.DateOfBirth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.yeargraduate_college.setPlainText("")
        self.yeargraduate_college.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.Department.setPlainText("")
        self.Department.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Department...", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Civil status", None))
        self.government_examination.setPlainText("")
        self.government_examination.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Examination...", None))
        self.DateOfMarriage.setPlainText("")
        self.DateOfMarriage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Pag-Ibig Number", None))
        self.EmployeeImageLabel.setText(QCoreApplication.translate("MainWindow", u"(image name here)", None))
        self.label_7.setText("")
        self.address_graduateschool.setPlainText("")
        self.address_graduateschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address of graduate school...", None))
        self.child1_LastName.setPlainText("")
        self.child1_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.Spouse_LastName.setPlainText("")
        self.Spouse_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Date of marriage", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Academic record", None))
        self.College.setPlainText("")
        self.College.setPlaceholderText(QCoreApplication.translate("MainWindow", u"College...", None))
        self.ChurchAffiliation.setPlainText("")
        self.ChurchAffiliation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Church affiliation...", None))
        self.staff_LastName1.setPlainText("")
        self.staff_LastName1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Philhealth Number", None))
        self.Father_LastName.setPlainText("")
        self.Father_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.DumaAddress.setPlainText("")
        self.DumaAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Dumaguete address...", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"E-mail address", None))
        self.staff_relationship2.setPlainText("")
        self.staff_relationship2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Relationship...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Tax Identification Number", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"This confirms that all details are true.", None))
        self.sibling1_address.setPlainText("")
        self.sibling1_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.sibling1_FirstName.setPlainText("")
        self.sibling1_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sibling's first name...", None))
        self.sibling1_LastName.setPlainText("")
        self.sibling1_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.sibling1_occupation.setPlainText("")
        self.sibling1_occupation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Occupation...", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Place of marriage", None))
        self.MiddleName.setPlainText("")
        self.MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.address_highschool.setPlainText("")
        self.address_highschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address of high school...", None))
        self.government_date.setPlainText("")
        self.government_date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Date of examination...", None))
        self.scholarships_awards.setPlainText("")
        self.scholarships_awards.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Includes scholarships, awards, etc ...", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Publication(s)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SSS Number", None))
        self.elementary_school_address.setPlainText("")
        self.elementary_school_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address of elementary school...", None))
        self.yeargraduate_elementary.setPlainText("")
        self.yeargraduate_elementary.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.yeargraduate_graduateschool.setPlainText("")
        self.yeargraduate_graduateschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Department(s)", None))
        self.Mother_LastName.setPlainText("")
        self.Mother_LastName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
        self.Spouse_FirstName.setPlainText("")
        self.Spouse_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.PlaceOfMarriage.setPlainText("")
        self.PlaceOfMarriage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Involvement in criminal case(s)*", None))
        self.TINnumber.setPlainText("")
        self.TINnumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TIN...", None))
        self.employee_picture.setText(QCoreApplication.translate("MainWindow", u"Profile Picture", None))
        self.publications.setPlainText("")
        self.publications.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Includes thesis papers, and other publications ...", None))
        self.Spouse_MiddleName.setPlainText("")
        self.Spouse_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.FirstName.setPlainText("")
        self.FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adding Employee Record", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Government examination(s) passed", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ACR number", None))
        self.child1_FirstName.setPlainText("")
        self.child1_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"If non-Filipino*, please fill the following fields...", None))
        self.Citizenship.setPlainText("")
        self.Citizenship.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Citizenship...", None))
        self.PlaceOfBirth.setPlainText("")
        self.PlaceOfBirth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Place of birth...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dumaguete address", None))
        self.staff_MiddleName2.setPlainText("")
        self.staff_MiddleName2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.HomeAddress.setPlainText("")
        self.HomeAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full home address...", None))
        self.staff_FirstName1.setPlainText("")
        self.staff_FirstName1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.FatherJob.setPlainText("")
        self.FatherJob.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Father's occupation...", None))
        self.child1_dateofbirth.setPlainText("")
        self.child1_dateofbirth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Date of birth...", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Passport number", None))
        self.government_rating.setPlainText("")
        self.government_rating.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rating...", None))
        self.child1_MiddleName.setPlainText("")
        self.child1_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.diploma_highschool.setPlainText("")
        self.diploma_highschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.MotherJob.setPlainText("")
        self.MotherJob.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mother's occupation...", None))
        self.Father_MiddleName.setPlainText("")
        self.Father_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.diploma_graduateschool.setPlainText("")
        self.diploma_graduateschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.address_college.setPlainText("")
        self.address_college.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address of College...", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Name of spouse", None))
        self.Mother_MiddleName.setPlainText("")
        self.Mother_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Mother", None))
        self.staff_FirstName2.setPlainText("")
        self.staff_FirstName2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Date issued", None))
        self.Father_FirstName.setPlainText("")
        self.Father_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.PagIbigNumber.setPlainText("")
        self.PagIbigNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pag-Ibig No. ...", None))
        self.highschool.setPlainText("")
        self.highschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"High School...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Position(s)", None))
        self.SurName.setPlainText("")
        self.SurName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Surname...", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Children (if any)", None))
        self.PhilHNumber.setPlainText("")
        self.PhilHNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Philhealth No. ...", None))
        self.sibling1_MiddleName.setPlainText("")
        self.sibling1_MiddleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.CivilStatus.setPlainText("")
        self.CivilStatus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Civil status...", None))
        self.SSSnumber.setPlainText("")
        self.SSSnumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SSS...", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Date of birth", None))
        self.Mother_FirstName.setPlainText("")
        self.Mother_FirstName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.yeargraduate_highschool.setPlainText("")
        self.yeargraduate_highschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Place of birth", None))
        self.diploma_elementary.setPlainText("")
        self.diploma_elementary.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Related staff member(s)", None))
        self.Image_Upload.setText(QCoreApplication.translate("MainWindow", u"Upload Employee Image", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Father", None))
        self.Graduateschool.setPlainText("")
        self.Graduateschool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Graduate School...", None))
        self.case_name.setPlainText("")
        self.case_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Case name...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Home address", None))
        self.staff_LastName2.setPlainText("")
        self.staff_LastName2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name...", None))
    # retranslateUi

