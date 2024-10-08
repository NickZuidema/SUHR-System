# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_employee_recordPGBymD.ui'
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
        self.label_3.setPixmap(QPixmap(u"sillimanlogo.png"))
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
        self.criminalcases_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.criminalcases_ignore.setObjectName(u"criminalcases_ignore")

        self.gridLayout.addWidget(self.criminalcases_ignore, 68, 16, 1, 1)

        self.diploma_highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_highschool.setObjectName(u"diploma_highschool")
        self.diploma_highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_highschool, 46, 4, 1, 9)

        self.staff_position2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_position2.setObjectName(u"staff_position2")
        self.staff_position2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_position2, 53, 13, 1, 4)

        self.PagIbigNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PagIbigNumber.setObjectName(u"PagIbigNumber")
        self.PagIbigNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PagIbigNumber, 22, 1, 1, 7)

        self.record_addfield = QPushButton(self.scrollAreaWidgetContents_2)
        self.record_addfield.setObjectName(u"record_addfield")

        self.gridLayout.addWidget(self.record_addfield, 64, 1, 1, 16)

        self.MotherJob = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherJob.setObjectName(u"MotherJob")
        self.MotherJob.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherJob, 29, 10, 1, 7)

        self.EmployeeImageLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.EmployeeImageLabel.setObjectName(u"EmployeeImageLabel")

        self.gridLayout.addWidget(self.EmployeeImageLabel, 7, 0, 1, 1)

        self.staff_position3 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_position3.setObjectName(u"staff_position3")
        self.staff_position3.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_position3, 52, 13, 1, 4)

        self.staff_relationship2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_relationship2.setObjectName(u"staff_relationship2")
        self.staff_relationship2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_relationship2, 52, 4, 1, 9)

        self.staff_relationship2_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_relationship2_2.setObjectName(u"staff_relationship2_2")
        self.staff_relationship2_2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_relationship2_2, 53, 4, 1, 9)

        self.yeargraduate_college = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_college.setObjectName(u"yeargraduate_college")
        self.yeargraduate_college.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_college, 48, 13, 1, 4)

        self.DateOfMarriage = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DateOfMarriage.setObjectName(u"DateOfMarriage")
        self.DateOfMarriage.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DateOfMarriage, 37, 15, 1, 2)

        self.Email = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Email.setObjectName(u"Email")
        self.Email.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Email, 18, 6, 1, 11)

        self.government_rating = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.government_rating.setObjectName(u"government_rating")
        self.government_rating.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.government_rating, 66, 3, 1, 4)

        self.children_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.children_ignore.setObjectName(u"children_ignore")

        self.gridLayout.addWidget(self.children_ignore, 38, 16, 1, 1)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout.addWidget(self.label_41, 65, 1, 1, 2)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 15, 1, 1, 1)

        self.SurName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SurName.setObjectName(u"SurName")
        self.SurName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SurName, 2, 11, 1, 6)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 11, 1, 5)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 21, 8, 1, 4)

        self.NONFILIPINO_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_ignore.setObjectName(u"NONFILIPINO_ignore")

        self.gridLayout.addWidget(self.NONFILIPINO_ignore, 14, 16, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 17, 1, 1, 1)

        self.elementary_school = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.elementary_school.setObjectName(u"elementary_school")
        self.elementary_school.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.elementary_school, 43, 1, 1, 16)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 19, 1, 1, 2)

        self.DateOfBirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DateOfBirth.setObjectName(u"DateOfBirth")
        self.DateOfBirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DateOfBirth, 13, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"\n"
"font: 600 14pt \"Outfit SemiBold\";")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 12, 1, 1, 1)

        self.Sibling_addfield = QPushButton(self.scrollAreaWidgetContents_2)
        self.Sibling_addfield.setObjectName(u"Sibling_addfield")

        self.gridLayout.addWidget(self.Sibling_addfield, 34, 1, 1, 16)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 28, 10, 1, 5)

        self.PlaceOfBirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PlaceOfBirth.setObjectName(u"PlaceOfBirth")
        self.PlaceOfBirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PlaceOfBirth, 13, 2, 1, 8)

        self.civilstatus_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.civilstatus_ignore.setObjectName(u"civilstatus_ignore")

        self.gridLayout.addWidget(self.civilstatus_ignore, 35, 16, 1, 1)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 36, 1, 1, 1)

        self.FatherJob = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherJob.setObjectName(u"FatherJob")
        self.FatherJob.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherJob, 26, 10, 1, 7)

        self.Image_Upload = QPushButton(self.scrollAreaWidgetContents_2)
        self.Image_Upload.setObjectName(u"Image_Upload")

        self.gridLayout.addWidget(self.Image_Upload, 2, 0, 5, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 9pt \"Outfit\";")

        self.gridLayout.addWidget(self.label_15, 14, 1, 1, 2)

        self.yeargraduate_highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_highschool.setObjectName(u"yeargraduate_highschool")
        self.yeargraduate_highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_highschool, 46, 13, 1, 4)

        self.FirstName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FirstName.setObjectName(u"FirstName")
        self.FirstName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";\n"
"")

        self.gridLayout.addWidget(self.FirstName, 2, 1, 1, 4)

        self.Position = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Position.setObjectName(u"Position")
        self.Position.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Position, 4, 1, 1, 16)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 9, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 71, 11, 1, 5)

        self.sibling1_address = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_address.setObjectName(u"sibling1_address")
        self.sibling1_address.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling1_address, 32, 13, 1, 4)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout.addWidget(self.label_33, 36, 9, 1, 4)

        self.child1_name = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_name.setObjectName(u"child1_name")
        self.child1_name.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.child1_name, 39, 1, 1, 12)

        self.staff_name2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_name2.setObjectName(u"staff_name2")
        self.staff_name2.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_name2, 53, 1, 1, 3)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 7, 1, 1, 1)

        self.address_highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_highschool.setObjectName(u"address_highschool")
        self.address_highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_highschool, 46, 1, 1, 3)

        self.child1_dateofbirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child1_dateofbirth.setObjectName(u"child1_dateofbirth")
        self.child1_dateofbirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.child1_dateofbirth, 39, 13, 1, 4)

        self.record_employee_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.record_employee_ignore.setObjectName(u"record_employee_ignore")

        self.gridLayout.addWidget(self.record_employee_ignore, 61, 14, 1, 3)

        self.address_employment = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_employment.setObjectName(u"address_employment")
        self.address_employment.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_employment, 63, 1, 1, 16)

        self.publications_addfield = QPushButton(self.scrollAreaWidgetContents_2)
        self.publications_addfield.setObjectName(u"publications_addfield")

        self.gridLayout.addWidget(self.publications_addfield, 60, 1, 1, 16)

        self.scholarships_addfield = QPushButton(self.scrollAreaWidgetContents_2)
        self.scholarships_addfield.setObjectName(u"scholarships_addfield")

        self.gridLayout.addWidget(self.scholarships_addfield, 57, 1, 1, 16)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 21, 1, 1, 2)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 36, 15, 1, 2)

        self.staff_addfield = QPushButton(self.scrollAreaWidgetContents_2)
        self.staff_addfield.setObjectName(u"staff_addfield")

        self.gridLayout.addWidget(self.staff_addfield, 54, 1, 1, 16)

        self.sibling2_address = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling2_address.setObjectName(u"sibling2_address")
        self.sibling2_address.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling2_address, 33, 13, 1, 4)

        self.SpouseName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SpouseName.setObjectName(u"SpouseName")
        self.SpouseName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SpouseName, 37, 2, 1, 7)

        self.government_date = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.government_date.setObjectName(u"government_date")
        self.government_date.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.government_date, 66, 7, 1, 5)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 19, 8, 1, 4)

        self.children_addfield = QPushButton(self.scrollAreaWidgetContents_2)
        self.children_addfield.setObjectName(u"children_addfield")

        self.gridLayout.addWidget(self.children_addfield, 41, 1, 1, 16)

        self.FatherName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherName.setObjectName(u"FatherName")
        self.FatherName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherName, 26, 1, 1, 9)

        self.government_addfield = QPushButton(self.scrollAreaWidgetContents_2)
        self.government_addfield.setObjectName(u"government_addfield")

        self.gridLayout.addWidget(self.government_addfield, 67, 1, 1, 16)

        self.PhilHNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PhilHNumber.setObjectName(u"PhilHNumber")
        self.PhilHNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PhilHNumber, 22, 8, 1, 9)

        self.staff_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.staff_ignore.setObjectName(u"staff_ignore")

        self.gridLayout.addWidget(self.staff_ignore, 51, 15, 1, 2)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout.addWidget(self.label_42, 68, 1, 1, 2)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 28, 1, 1, 2)

        self.sibling1_name = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_name.setObjectName(u"sibling1_name")
        self.sibling1_name.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling1_name, 32, 1, 1, 3)

        self.MotherName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherName.setObjectName(u"MotherName")
        self.MotherName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherName, 29, 1, 1, 9)

        self.sibling1_occupation = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling1_occupation.setObjectName(u"sibling1_occupation")
        self.sibling1_occupation.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling1_occupation, 32, 4, 1, 9)

        self.NONFILIPINO_acrnum = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_acrnum.setObjectName(u"NONFILIPINO_acrnum")
        self.NONFILIPINO_acrnum.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_acrnum, 16, 8, 1, 8)

        self.staff_name1 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.staff_name1.setObjectName(u"staff_name1")
        self.staff_name1.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.staff_name1, 52, 1, 1, 3)

        self.ContactNumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.ContactNumber.setObjectName(u"ContactNumber")
        self.ContactNumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.ContactNumber, 18, 1, 1, 5)

        self.TINnumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.TINnumber.setObjectName(u"TINnumber")
        self.TINnumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.TINnumber, 20, 1, 1, 7)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 15, 16, 1, 1)

        self.publications = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.publications.setObjectName(u"publications")
        self.publications.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.publications, 59, 1, 1, 16)

        self.address_graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_graduateschool.setObjectName(u"address_graduateschool")
        self.address_graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_graduateschool, 50, 1, 1, 3)

        self.child2_name = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child2_name.setObjectName(u"child2_name")
        self.child2_name.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.child2_name, 40, 1, 1, 12)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 12, 10, 1, 4)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 31, 1, 1, 2)

        self.address_college = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.address_college.setObjectName(u"address_college")
        self.address_college.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.address_college, 48, 1, 1, 3)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 12, 0, 60, 1)

        self.Department = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Department.setObjectName(u"Department")
        self.Department.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Department, 6, 1, 1, 16)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout.addWidget(self.label_36, 42, 1, 1, 2)

        self.Government_place = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Government_place.setObjectName(u"Government_place")
        self.Government_place.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Government_place, 66, 12, 1, 5)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 12, 2, 1, 1)

        self.case_name = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.case_name.setObjectName(u"case_name")
        self.case_name.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.case_name, 69, 1, 1, 16)

        self.DumaAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.DumaAddress.setObjectName(u"DumaAddress")
        self.DumaAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.DumaAddress, 8, 1, 1, 16)

        self.government_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.government_ignore.setObjectName(u"government_ignore")

        self.gridLayout.addWidget(self.government_ignore, 65, 16, 1, 1)

        self.College = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.College.setObjectName(u"College")
        self.College.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.College, 47, 1, 1, 16)

        self.sibling2_occupation = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling2_occupation.setObjectName(u"sibling2_occupation")
        self.sibling2_occupation.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling2_occupation, 33, 4, 1, 9)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 5, 1, 3)

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

        self.SignatureLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.SignatureLabel.setObjectName(u"SignatureLabel")

        self.gridLayout.addWidget(self.SignatureLabel, 11, 0, 1, 1)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout.addWidget(self.label_37, 51, 1, 1, 2)

        self.elementary_school_address = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.elementary_school_address.setObjectName(u"elementary_school_address")
        self.elementary_school_address.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.elementary_school_address, 44, 1, 1, 3)

        self.diploma_college = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_college.setObjectName(u"diploma_college")
        self.diploma_college.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_college, 48, 4, 1, 9)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 71, 16, 1, 1)

        self.Graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Graduateschool.setObjectName(u"Graduateschool")
        self.Graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Graduateschool, 49, 1, 1, 16)

        self.scholarships_awards = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.scholarships_awards.setObjectName(u"scholarships_awards")
        self.scholarships_awards.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.scholarships_awards, 56, 1, 1, 16)

        self.yeargraduate_graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_graduateschool.setObjectName(u"yeargraduate_graduateschool")
        self.yeargraduate_graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_graduateschool, 50, 13, 1, 4)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 16, 1, 1)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout.addWidget(self.label_35, 38, 1, 1, 2)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout.addWidget(self.label_39, 58, 1, 1, 2)

        self.SSSnumber = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.SSSnumber.setObjectName(u"SSSnumber")
        self.SSSnumber.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.SSSnumber, 20, 8, 1, 9)

        self.diploma_elementary = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_elementary.setObjectName(u"diploma_elementary")
        self.diploma_elementary.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_elementary, 44, 4, 1, 9)

        self.name_employer = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.name_employer.setObjectName(u"name_employer")
        self.name_employer.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.name_employer, 62, 1, 1, 2)

        self.ChurchAffiliation_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.ChurchAffiliation_ignore.setObjectName(u"ChurchAffiliation_ignore")

        self.gridLayout.addWidget(self.ChurchAffiliation_ignore, 23, 16, 1, 1)

        self.NONFILIPINO_passport = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_passport.setObjectName(u"NONFILIPINO_passport")
        self.NONFILIPINO_passport.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_passport, 16, 1, 1, 7)

        self.MiddleName = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MiddleName.setObjectName(u"MiddleName")
        self.MiddleName.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MiddleName, 2, 5, 1, 6)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 23, 1, 1, 2)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout.addWidget(self.label_38, 55, 1, 1, 2)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 11, 1, 3)

        self.CivilStatus = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.CivilStatus.setObjectName(u"CivilStatus")
        self.CivilStatus.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.CivilStatus, 37, 1, 1, 1)

        self.HomeAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.HomeAddress.setObjectName(u"HomeAddress")
        self.HomeAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.HomeAddress, 10, 1, 2, 16)

        self.diploma_graduateschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.diploma_graduateschool.setObjectName(u"diploma_graduateschool")
        self.diploma_graduateschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.diploma_graduateschool, 50, 4, 1, 9)

        self.NONFILIPINO_dateissued = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.NONFILIPINO_dateissued.setObjectName(u"NONFILIPINO_dateissued")
        self.NONFILIPINO_dateissued.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.NONFILIPINO_dateissued, 16, 16, 1, 1)

        self.child2_dateofbirth = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.child2_dateofbirth.setObjectName(u"child2_dateofbirth")
        self.child2_dateofbirth.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.child2_dateofbirth, 40, 13, 1, 4)

        self.yeargraduate_elementary = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.yeargraduate_elementary.setObjectName(u"yeargraduate_elementary")
        self.yeargraduate_elementary.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.yeargraduate_elementary, 44, 13, 1, 4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.highschool = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.highschool.setObjectName(u"highschool")
        self.highschool.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.highschool, 45, 1, 1, 16)

        self.FatherAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.FatherAddress.setObjectName(u"FatherAddress")
        self.FatherAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.FatherAddress, 27, 1, 1, 16)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout.addWidget(self.label_40, 61, 1, 1, 2)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 17, 6, 1, 3)

        self.government_examination = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.government_examination.setObjectName(u"government_examination")
        self.government_examination.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.government_examination, 66, 1, 1, 2)

        self.MotherAddress = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.MotherAddress.setObjectName(u"MotherAddress")
        self.MotherAddress.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.MotherAddress, 30, 1, 1, 16)

        self.Siblings_ignore = QCheckBox(self.scrollAreaWidgetContents_2)
        self.Siblings_ignore.setObjectName(u"Siblings_ignore")

        self.gridLayout.addWidget(self.Siblings_ignore, 31, 16, 1, 1)

        self.PlaceOfMarriage = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.PlaceOfMarriage.setObjectName(u"PlaceOfMarriage")
        self.PlaceOfMarriage.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.PlaceOfMarriage, 37, 9, 1, 6)

        self.period_employment = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.period_employment.setObjectName(u"period_employment")
        self.period_employment.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.period_employment, 62, 9, 1, 3)

        self.case_addfield = QPushButton(self.scrollAreaWidgetContents_2)
        self.case_addfield.setObjectName(u"case_addfield")

        self.gridLayout.addWidget(self.case_addfield, 70, 1, 1, 16)

        self.label_32 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 36, 2, 1, 2)

        self.position_workplace = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.position_workplace.setObjectName(u"position_workplace")
        self.position_workplace.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.position_workplace, 62, 3, 1, 6)

        self.reason = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.reason.setObjectName(u"reason")
        self.reason.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.reason, 62, 12, 1, 5)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 15, 8, 1, 2)

        self.Signature_Upload = QPushButton(self.scrollAreaWidgetContents_2)
        self.Signature_Upload.setObjectName(u"Signature_Upload")

        self.gridLayout.addWidget(self.Signature_Upload, 8, 0, 3, 1)

        self.Citizenship = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.Citizenship.setObjectName(u"Citizenship")
        self.Citizenship.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.Citizenship, 13, 10, 1, 7)

        self.sibling2_name = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.sibling2_name.setObjectName(u"sibling2_name")
        self.sibling2_name.setStyleSheet(u"font: 300 9pt \"Outfit Light\";")

        self.gridLayout.addWidget(self.sibling2_name, 33, 1, 1, 3)

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
        self.criminalcases_ignore.setText(QCoreApplication.translate("MainWindow", u"Does not apply", None))
        self.diploma_highschool.setPlainText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.staff_position2.setPlainText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.PagIbigNumber.setPlainText(QCoreApplication.translate("MainWindow", u"Pag-Ibig No. ...", None))
        self.record_addfield.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.MotherJob.setPlainText(QCoreApplication.translate("MainWindow", u"Mother's occupation...", None))
        self.EmployeeImageLabel.setText(QCoreApplication.translate("MainWindow", u"(image name here)", None))
        self.staff_position3.setPlainText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.staff_relationship2.setPlainText(QCoreApplication.translate("MainWindow", u"Relationship...", None))
        self.staff_relationship2_2.setPlainText(QCoreApplication.translate("MainWindow", u"Relationship...", None))
        self.yeargraduate_college.setPlainText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.DateOfMarriage.setPlainText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.Email.setPlainText(QCoreApplication.translate("MainWindow", u"E-mail address...", None))
        self.government_rating.setPlainText(QCoreApplication.translate("MainWindow", u"Rating...", None))
        self.children_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no children.", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Government examination(s) passed", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Passport number", None))
        self.SurName.setPlainText(QCoreApplication.translate("MainWindow", u"Surname...", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"This confirms that all details are true.", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Philhealth Number", None))
        self.NONFILIPINO_ignore.setText(QCoreApplication.translate("MainWindow", u"Ignore fields", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Department(s)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Contact number", None))
        self.elementary_school.setPlainText(QCoreApplication.translate("MainWindow", u"Elementary School...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Tax Identification Number", None))
        self.DateOfBirth.setPlainText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Adding Employee Record", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Date of birth", None))
        self.Sibling_addfield.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Mother's occupation", None))
        self.PlaceOfBirth.setPlainText(QCoreApplication.translate("MainWindow", u"Place of birth...", None))
        self.civilstatus_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee is unmarried.", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Civil status", None))
        self.FatherJob.setPlainText(QCoreApplication.translate("MainWindow", u"Father's occupation...", None))
        self.Image_Upload.setText(QCoreApplication.translate("MainWindow", u"Upload Employee Image", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"If non-Filipino*, please fill the following fields...", None))
        self.yeargraduate_highschool.setPlainText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.FirstName.setPlainText(QCoreApplication.translate("MainWindow", u"First name...", None))
        self.Position.setPlainText(QCoreApplication.translate("MainWindow", u"Position...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Home address", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"This confirms that all details are true.", None))
        self.sibling1_address.setPlainText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Place of marriage", None))
        self.child1_name.setPlainText(QCoreApplication.translate("MainWindow", u"Name of child...", None))
        self.staff_name2.setPlainText(QCoreApplication.translate("MainWindow", u"Name...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Dumaguete address", None))
        self.address_highschool.setPlainText(QCoreApplication.translate("MainWindow", u"Address of high school...", None))
        self.child1_dateofbirth.setPlainText(QCoreApplication.translate("MainWindow", u"Date of birth...", None))
        self.record_employee_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no record of prior employment.", None))
        self.address_employment.setPlainText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.publications_addfield.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.scholarships_addfield.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Pag-Ibig Number", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Date of marriage", None))
        self.staff_addfield.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.sibling2_address.setPlainText(QCoreApplication.translate("MainWindow", u"Address...", None))
        self.SpouseName.setPlainText(QCoreApplication.translate("MainWindow", u"Name of spouse...", None))
        self.government_date.setPlainText(QCoreApplication.translate("MainWindow", u"Date of examination...", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SSS Number", None))
        self.children_addfield.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.FatherName.setPlainText(QCoreApplication.translate("MainWindow", u"Father's full name...", None))
        self.government_addfield.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.PhilHNumber.setPlainText(QCoreApplication.translate("MainWindow", u"Philhealth No. ...", None))
        self.staff_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee is not related to any staff.", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Involvement in criminal case(s)*", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Mother", None))
        self.sibling1_name.setPlainText(QCoreApplication.translate("MainWindow", u"Sibling's full name...", None))
        self.MotherName.setPlainText(QCoreApplication.translate("MainWindow", u"Mother's full name...", None))
        self.sibling1_occupation.setPlainText(QCoreApplication.translate("MainWindow", u"Occupation...", None))
        self.NONFILIPINO_acrnum.setPlainText(QCoreApplication.translate("MainWindow", u"ACR number...", None))
        self.staff_name1.setPlainText(QCoreApplication.translate("MainWindow", u"Name...", None))
        self.ContactNumber.setPlainText(QCoreApplication.translate("MainWindow", u"Contact number...", None))
        self.TINnumber.setPlainText(QCoreApplication.translate("MainWindow", u"TIN...", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Date issued", None))
        self.publications.setPlainText(QCoreApplication.translate("MainWindow", u"Includes thesis papers, and other publications ...", None))
        self.address_graduateschool.setPlainText(QCoreApplication.translate("MainWindow", u"Address of graduate school...", None))
        self.child2_name.setPlainText(QCoreApplication.translate("MainWindow", u"Name of child...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Citizenship", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Sibling(s)", None))
        self.address_college.setPlainText(QCoreApplication.translate("MainWindow", u"Address of College...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Position(s)", None))
        self.Department.setPlainText(QCoreApplication.translate("MainWindow", u"Department...", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Academic record", None))
        self.Government_place.setPlainText(QCoreApplication.translate("MainWindow", u"Place...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Place of birth", None))
        self.case_name.setPlainText(QCoreApplication.translate("MainWindow", u"Case name...", None))
        self.DumaAddress.setPlainText(QCoreApplication.translate("MainWindow", u"Full Dumaguete address...", None))
        self.government_ignore.setText(QCoreApplication.translate("MainWindow", u"Does not apply", None))
        self.College.setPlainText(QCoreApplication.translate("MainWindow", u"College...", None))
        self.sibling2_occupation.setPlainText(QCoreApplication.translate("MainWindow", u"Occupation...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.ChurchAffiliation.setPlainText(QCoreApplication.translate("MainWindow", u"Church affiliation...", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Father", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Father's occupation", None))
        self.SignatureLabel.setText(QCoreApplication.translate("MainWindow", u"(image name here)", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Related staff member(s)", None))
        self.elementary_school_address.setPlainText(QCoreApplication.translate("MainWindow", u"Address of elementary school...", None))
        self.diploma_college.setPlainText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.Graduateschool.setPlainText(QCoreApplication.translate("MainWindow", u"Graduate School...", None))
        self.scholarships_awards.setPlainText(QCoreApplication.translate("MainWindow", u"Includes scholarships, awards, etc ...", None))
        self.yeargraduate_graduateschool.setPlainText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Children (if any)", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Publication(s)", None))
        self.SSSnumber.setPlainText(QCoreApplication.translate("MainWindow", u"SSS...", None))
        self.diploma_elementary.setPlainText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.name_employer.setPlainText(QCoreApplication.translate("MainWindow", u"Name of employer...", None))
        self.ChurchAffiliation_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no church affiliation.", None))
        self.NONFILIPINO_passport.setPlainText(QCoreApplication.translate("MainWindow", u"Passport number...", None))
        self.MiddleName.setPlainText(QCoreApplication.translate("MainWindow", u"Middle name...", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Church affiliation", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"School or college distinction(s)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.CivilStatus.setPlainText(QCoreApplication.translate("MainWindow", u"Civil status...", None))
        self.HomeAddress.setPlainText(QCoreApplication.translate("MainWindow", u"Full home address...", None))
        self.diploma_graduateschool.setPlainText(QCoreApplication.translate("MainWindow", u"Diploma or degree...", None))
        self.NONFILIPINO_dateissued.setPlainText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.child2_dateofbirth.setPlainText(QCoreApplication.translate("MainWindow", u"Date of birth...", None))
        self.yeargraduate_elementary.setPlainText(QCoreApplication.translate("MainWindow", u"Year graduated...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.highschool.setPlainText(QCoreApplication.translate("MainWindow", u"High School...", None))
        self.FatherAddress.setPlainText(QCoreApplication.translate("MainWindow", u"Father's current home address...", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Record of previous employment", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"E-mail address", None))
        self.government_examination.setPlainText(QCoreApplication.translate("MainWindow", u"Examination...", None))
        self.MotherAddress.setPlainText(QCoreApplication.translate("MainWindow", u"Mother's current home address...", None))
        self.Siblings_ignore.setText(QCoreApplication.translate("MainWindow", u"Employee has no siblings.", None))
        self.PlaceOfMarriage.setPlainText(QCoreApplication.translate("MainWindow", u"Place of marriage...", None))
        self.period_employment.setPlainText(QCoreApplication.translate("MainWindow", u"Period of employment...", None))
        self.case_addfield.setText(QCoreApplication.translate("MainWindow", u"Add field", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Name of spouse", None))
        self.position_workplace.setPlainText(QCoreApplication.translate("MainWindow", u"Position at workplace...", None))
        self.reason.setPlainText(QCoreApplication.translate("MainWindow", u"Reason for leaving...", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ACR number", None))
        self.Signature_Upload.setText(QCoreApplication.translate("MainWindow", u"Upload Employee Signature", None))
        self.Citizenship.setPlainText(QCoreApplication.translate("MainWindow", u"Citizenship...", None))
        self.sibling2_name.setPlainText(QCoreApplication.translate("MainWindow", u"Sibling's full name...", None))
    # retranslateUi

