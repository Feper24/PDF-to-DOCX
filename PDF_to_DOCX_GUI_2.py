#Needed for certain system path definitions we'll use in our functions
import sys
import os

#New library we use to create the GUI (graphic user interface in the .exe solution file) for the end-user in an app :)
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
#Same library we used before to convert pdf files to docx
from pdf2docx import Converter

#Need to define some classes & functions to "build" the visible window of our "app".exe solution
class PDFConverterGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    #This is the visible part, what it looks like, where are the buttons located, which functions are going to be used on those buttons
    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('PDF to DOCX Converter')

        self.input_label = QLabel('Select PDF File:', self)
        self.input_label.move(20, 20)

        self.input_button = QPushButton('Browse', self)
        self.input_button.move(300, 20)
        self.input_button.clicked.connect(self.select_input_pdf)

        self.output_label = QLabel('Select Output Location:', self)
        self.output_label.move(20, 60)

        self.output_button = QPushButton('Browse', self)
        self.output_button.move(300, 60)
        self.output_button.clicked.connect(self.select_output_location)

        self.convert_button = QPushButton('Convert', self)
        self.convert_button.move(150, 100)
        self.convert_button.clicked.connect(self.convert_pdf_to_docx)
    
    #Here we literally write what the functions actually do... previously we wrote the "visible" part and tied it to certain functions...
    #but we need to tell the code "hey, those functions do this and that"
    def select_input_pdf(self):
        self.input_path, _ = QFileDialog.getOpenFileName(self, 'Select PDF File', '', 'PDF Files (*.pdf)')
        self.input_label.setText(f'Selected PDF: {os.path.basename(self.input_path)}')

    def select_output_location(self):
        self.output_path, _ = QFileDialog.getSaveFileName(self, 'Save DOCX File', '', 'Word Files (*.docx)')
        self.output_label.setText(f'Selected Output: {os.path.basename(self.output_path)}')

    def convert_pdf_to_docx(self):
        cv = Converter(self.input_path)
        cv.convert(self.output_path, start=0, end=None)
        cv.close()
        self.input_label.setText('Select PDF File:')
        self.output_label.setText('Select Output Location:')
        self.input_path = ''
        self.output_path = ''

#Now that we have our app built, these is some generic stuff to make the app's window work properly (show when executed, exit when closed, etc)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PDFConverterGUI()
    window.show()
    sys.exit(app.exec_())