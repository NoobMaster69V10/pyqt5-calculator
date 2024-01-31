import sys
import smtplib
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenuBar, QMenu


def send_mail(email_sender, email_password, email_receiver, email_subject, email_body, msg, acc_msg):
    if email_sender == '' and email_password == '':
        # Account Message Box
        acc_msg.exec_()
    else:
        text = f"Subject: {email_subject}\n\n{email_body}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, text)

        # Message Box
        msg.exec_()


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        # Main Window
        self.setWindowTitle("Email-Sender")
        self.setWindowIcon(QtGui.QIcon('email.png'))
        self.setGeometry(700, 300, 500, 450)
        self.m_sender = ''
        self.sender_p = ''

        # Design Elements
        self.to_input = QtWidgets.QLineEdit(self)
        self.subject_input = QtWidgets.QLineEdit(self)
        self.main_input = QtWidgets.QTextEdit(self)
        self.send_btn = QtWidgets.QPushButton(self)

        # Message Box
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Status")
        self.msg.setText("Email has been sent successfully")
        self.msg.setWindowIcon(QtGui.QIcon('email.png'))
        self.msg.setStandardButtons(QMessageBox.Ok)

        # Account Message Box
        self.acc_msg = QMessageBox()
        self.acc_msg.setWindowTitle("Account error")
        self.acc_msg.setText("You have to add account to send email")
        self.acc_msg.setWindowIcon(QtGui.QIcon('email.png'))
        self.acc_msg.setIcon(QMessageBox.Warning)
        self.acc_msg.setStandardButtons(QMessageBox.Ok)

        # Menu Bar
        self.menu_bar = QMenuBar(self)
        self.create_menu_bar()

        # Main design
        self.create_design()

        # Click Func
        self.add_function()

    def create_design(self):
        # To Input
        self.to_input.setPlaceholderText("To")
        self.to_input.resize(500, 40)
        self.to_input.move(0, 30)

        # Subject input
        self.subject_input.setPlaceholderText("Subject")
        self.subject_input.resize(500, 40)
        self.subject_input.move(0, 70)

        # Main Text
        self.main_input.resize(500, 270)
        self.main_input.move(0, 110)
        self.main_input.setPlaceholderText("Write email text")

        # Send Button
        self.send_btn.setText("Send")
        self.send_btn.move(200, 400)

    def add_function(self):
        # Main Btn Click Func
        self.send_btn.clicked.connect(
            lambda: send_mail(self.m_sender, self.sender_p, self.to_input.text(), self.subject_input.text(),
                              self.main_input.toPlainText(), self.msg, self.acc_msg))

    def create_menu_bar(self):
        # Menu Bar Create Func
        self.setMenuBar(self.menu_bar)
        connect_menu = QMenu("&Account", self)
        self.menu_bar.addMenu(connect_menu)
        connect_menu.addAction('Add Account', self.add_account)

    def add_account(self):
        # Menu Bar Func
        action = self.sender()
        if action.text() == 'Add Account':
            s, ok = QtWidgets.QInputDialog.getText(self, "Add", "Enter e-mail:")
            s_p, ok = QtWidgets.QInputDialog.getText(self, "Add", "Enter app password:")
            self.m_sender = s
            self.sender_p = s_p


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
