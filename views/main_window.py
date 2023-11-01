# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class ListBookForm(object):
    def setupUi(self, ListBookForm):
        if not ListBookForm.objectName():
            ListBookForm.setObjectName(u"ListBookForm")
        ListBookForm.resize(961, 550)
        self.buttonsFrame = QFrame(ListBookForm)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(10, 10, 941, 91))
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.open_book_button = QPushButton(self.buttonsFrame)
        self.open_book_button.setObjectName(u"open_book_button")
        self.open_book_button.setGeometry(QRect(20, 10, 71, 51))
        self.open_book_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_book_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"./assets/icons/open-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_book_button.setIcon(icon)
        self.open_book_button.setIconSize(QSize(50, 50))
        self.open_book_button.setFlat(True)
        self.label = QLabel(self.buttonsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 91, 21))
        self.label_2 = QLabel(self.buttonsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 60, 91, 21))
        self.open_new_button = QPushButton(self.buttonsFrame)
        self.open_new_button.setObjectName(u"open_new_button")
        self.open_new_button.setGeometry(QRect(110, 10, 71, 51))
        self.open_new_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/add-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_new_button.setIcon(icon1)
        self.open_new_button.setIconSize(QSize(50, 50))
        self.open_new_button.setFlat(True)
        self.open_edit_button = QPushButton(self.buttonsFrame)
        self.open_edit_button.setObjectName(u"open_edit_button")
        self.open_edit_button.setGeometry(QRect(200, 10, 71, 51))
        self.open_edit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_edit_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/edit-book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_edit_button.setIcon(icon2)
        self.open_edit_button.setIconSize(QSize(50, 50))
        self.open_edit_button.setFlat(True)
        self.label_3 = QLabel(self.buttonsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 60, 91, 21))
        self.delete_book_button = QPushButton(self.buttonsFrame)
        self.delete_book_button.setObjectName(u"delete_book_button")
        self.delete_book_button.setGeometry(QRect(300, 10, 71, 51))
        self.delete_book_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/delete-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_book_button.setIcon(icon3)
        self.delete_book_button.setIconSize(QSize(50, 50))
        self.delete_book_button.setFlat(True)
        self.label_4 = QLabel(self.buttonsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 60, 91, 21))
        self.frame = QFrame(ListBookForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 941, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 71, 16))
        self.searchByCombobox = QComboBox(self.frame)
        self.searchByCombobox.setObjectName(u"searchByCombobox")
        self.searchByCombobox.setGeometry(QRect(70, 10, 161, 22))
        self.parameterLineEdit = QLineEdit(self.frame)
        self.parameterLineEdit.setObjectName(u"parameterLineEdit")
        self.parameterLineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(660, 10, 81, 25))
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon4)
        self.refreshButton = QPushButton(self.frame)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(740, 10, 121, 25))
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon5)
        self.export_button = QPushButton(self.frame)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setGeometry(QRect(880, 10, 31, 25))
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/icons8-export-excel-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_button.setIcon(icon6)
        self.export_button.setIconSize(QSize(26, 26))
        self.listBooksTable = QTableWidget(ListBookForm)
        self.listBooksTable.setObjectName(u"listBooksTable")
        self.listBooksTable.setGeometry(QRect(10, 160, 941, 341))
        self.label_6 = QLabel(ListBookForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 520, 111, 16))
        self.booksQtyLabel = QLabel(ListBookForm)
        self.booksQtyLabel.setObjectName(u"booksQtyLabel")
        self.booksQtyLabel.setGeometry(QRect(130, 520, 47, 13))

        self.retranslateUi(ListBookForm)

        QMetaObject.connectSlotsByName(ListBookForm)
    # setupUi

    def retranslateUi(self, ListBookForm):
        ListBookForm.setWindowTitle(QCoreApplication.translate("ListBookForm", u"Books List", None))
        self.open_book_button.setText("")
        self.label.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Abrir Libro</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nuevo Libro</span></p></body></html>", None))
        self.open_new_button.setText("")
        self.open_edit_button.setText("")
        self.label_3.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ediccion Libro</span></p></body></html>", None))
        self.delete_book_button.setText("")
        self.label_4.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar Libro</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("ListBookForm", u"buscar por:", None))
        self.searchButton.setText(QCoreApplication.translate("ListBookForm", u"BUSCAR", None))
        self.refreshButton.setText(QCoreApplication.translate("ListBookForm", u"ACTUALIZAR", None))
        self.export_button.setText("")
        self.label_6.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">cantidad de libros:</span></p></body></html>", None))
        self.booksQtyLabel.setText(QCoreApplication.translate("ListBookForm", u"#", None))
    # retranslateUi

