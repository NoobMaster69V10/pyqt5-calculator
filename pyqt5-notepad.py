from PyQt5 import QtWidgets, QtCore

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QMessageBox
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Notepad")
        self.setGeometry(600, 200, 800, 600)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        file_menu = QMenu("&File", self)
        self.menu_bar.addMenu(file_menu)

        file_menu.addAction('Open', self.action_clicked)
        file_menu.addAction('Save', self.action_clicked)
        file_menu.addAction('Save as', self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Open":
            try:
                self.fname = QFileDialog.getOpenFileName(self)[0]
                with open(self.fname, 'r') as f1:
                    text = f1.read()
                    self.text_edit.setText(text)
                    f1.close()
            except Exception as e:
                error = QMessageBox()
                error.setWindowTitle("Error Window")
                error.setText("File not found")
                error.setIcon(QMessageBox.Warning)
                error.standardButton(QMessageBox.Ok | QMessageBox.Cancel)
                error.setDefaultButton(QMessageBox.Cancel)
                error.SetDetailedText(e)

                error.exec_()

        elif action.text() == "Save":
            with open(self.fname, 'w') as f2:
                f2.write(self.text_edit.toPlainText())
                f2.close()

        elif action.text() == "Save as":
            self.fname = QFileDialog.getSaveFileName(self)[0]
            with open(self.fname, 'w') as f2:
                f2.write(self.text_edit.toPlainText())
                f2.close()


def applicaton():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    applicaton()
