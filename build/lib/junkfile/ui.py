#!/usr/bin/env python3

import sys
from PySide2.QtWidgets import QApplication, QDialog, QGridLayout
from PySide2.QtWidgets import QFileDialog, QMessageBox
from PySide2.QtWidgets import QLineEdit, QPushButton, QLabel, QCheckBox
from PySide2.QtCore import Qt
import junkfile

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Create widgets
        self.title = QLabel("Junkfile", self)
        self.title.setStyleSheet("color:#072120; font-weight: bold; font-size: 16px;")
        self.title.setAlignment(Qt.AlignCenter | Qt.AlignCenter) 

        self.instruction = QLabel("Choose a directory folder:", self)

        self.edit = QLineEdit("Path...")
        self.edit.setReadOnly(True)

        self.button = QPushButton("Open ...")

        self.copy = QCheckBox("Would you like to make a copy?")

        self.arrange = QPushButton("Arrange")

        # Create layout
        layout = QGridLayout()
        layout.setColumnMinimumWidth(0, 400)
        # add widgets
        layout.addWidget(self.title, 0, 0, 1, 0, Qt.AlignCenter)
        layout.addWidget(self.instruction, 1, 0)
        layout.addWidget(self.edit, 2, 0)
        layout.addWidget(self.button, 2, 1)
        layout.addWidget(self.copy, 3, 0)
        layout.addWidget(self.arrange, 3, 1)

        # Set dialog layout
        self.setLayout(layout)

        # Add button to get directory path
        self.button.clicked.connect(self.openDirectoryDialog)

        # add button to execute Junkfile
        self.arrange.clicked.connect(self.runJunkfile)




    # Oepn file directory
    def openDirectoryDialog(self):
        print ("Hello %s" % self.edit.text())

        open_dialog = QFileDialog()
        if not self.edit.text():
            init_path = str(Path.home())
        else:
            init_path = self.edit.text()

        temp_path = open_dialog.getExistingDirectory(
            self, "Select directory folder", init_path
        )
        if temp_path:
            self.edit.setText(temp_path)


    def runJunkfile(self):
        path=self.edit.text()
        copy=self.copy.isChecked()

        try:
            # set cursor to busy
            QApplication.setOverrideCursor(Qt.WaitCursor)

            # execute junk file
            result = junkfile.run(path_folder=path, create_copy=copy)

            # do lengthy process
            QApplication.restoreOverrideCursor()

            if result:
                self.messageBox(icon=QMessageBox.Information, title="Success", message="Folder arranged with successful!")    

        except Exception as e:
            self.messageBox(message=str(e))
            return False



    def messageBox(self, icon=QMessageBox.Warning, title="Warning", message=""):
        msgboxwarning = QMessageBox()
        msgboxwarning.setText(title)
        msgboxwarning.setInformativeText(message)
        msgboxwarning.setIcon(icon)
        msgboxwarning.setStandardButtons(QMessageBox.Close)
        msgboxwarning.exec_()


if __name__ == '__main__':
    
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the form
    form = Form()
   
    #show window
    form.show()

    # Run the main Qt loop
    sys.exit(app.exec_())
    