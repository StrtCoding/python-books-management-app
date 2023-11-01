import re
import os
import shutil

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.edit_book_window import EditBookForm
from db.books import select_book_by_id, update_book


class EditBookWindow(QWidget, EditBookForm):

    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.populate_inputs()
        self.selectFileButton.clicked.connect(self.select_file)
        self.editButton.clicked.connect(self.edit_book)


    def populate_inputs(self):
        data = select_book_by_id(self._id)
        
        self.titleLineEdit.setText(data[1])
        self.categoryLineEdit.setText(data[2])
        self.pageQtySpinBox.setValue(data[3])
        self.pageReadQtySpinBox.setValue(data[4])
        self.filePathLineEdit.setText(data[5])
        self.descriptionTextedit.setText(data[6])

    def select_file(self):
        self.old_path = self.filePathLineEdit.text()
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)

        print(file_path)

    def check_inputs(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pageQtySpinBox.value()
        path = self.filePathLineEdit.text()

        errors_count = 0
        
        if title == "":
            print("El campo titulo es obligatorio")
            errors_count += 1
        if category == "":
            print("El campo cateogria es obligatorio")
            errors_count +=1
        if path == "":
            print("Debe seleccionar un libro")
            errors_count +=1
        
        if errors_count == 0:
            return True

    def edit_book(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pageQtySpinBox.value()
        page_qty_read = self.pageReadQtySpinBox.value()
        path = self.filePathLineEdit.text()
        description = self.descriptionTextedit.toPlainText()

        data = [title, category, page_qty, page_qty_read, path, description]

        if self.check_inputs():
            path_to_check = "book_files\\" + re.split("/|\\\\", path)[-1]
            result = os.path.exists(path_to_check)

            if result == False:
               data[4] = shutil.copy(path, "book_files")
               os.remove(self.old_path)
            
            if update_book(self._id, data):
                self.close()


            

