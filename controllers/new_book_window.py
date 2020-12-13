from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from views.new_book_window import NewBookForm
from db.books import insert_book, select_book_by_id
import shutil
import os


class NewBookWindow(QWidget, NewBookForm):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.addButton.clicked.connect(self.add_book)
        self.selectFileButton.clicked.connect(self.select_file)
        self.cancelButton.clicked.connect(self.close)
    
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
            print("El campo categoria es obligatorio")
            errors_count +=1
        if page_qty == 0:
            print("El campo cantidad de paginas es obligatorio")
            errors_count +=1
        if path == "":
            print("Debe seleccionar un libro")
            errors_count +=1
        
        return (errors_count == 0)
            
        
    def add_book(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pageQtySpinBox.value()
        path = self.filePathLineEdit.text()
        description = self.descriptionTextedit.toPlainText()

        if self.check_inputs():
            new_path = shutil.copy(path, "book_files")
            data = (title, category, page_qty, new_path, description)
            if insert_book(data):
                self.clean_inputs()
                self.parent.refresh_table_from_child_window()
            else:
                self.filePathLineEdit.setText(new_path)
                self.undo()

    def clean_inputs(self):
        self.titleLineEdit.clear()
        self.categoryLineEdit.clear()
        self.pageQtySpinBox.setValue(0)
        self.filePathLineEdit.clear()
        self.descriptionTextedit.clear()

    def select_file(self):
        file_path = QFileDialog.getOpenFileName()[0]
        self.filePathLineEdit.setText(file_path)

    def undo(self):
        file_path = self.filePathLineEdit.text()

        if file_path != "":
            os.remove(file_path)



        
