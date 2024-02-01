import sys
import requests
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenu, QMenuBar


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Message sender name
        self.m_sender = ''

        # Create UI
        self.create_ui()
        self.show()

        self.send_btn_clicked()

    def create_ui(self):
        self.setWindowIcon(QtGui.QIcon('message.png'))
        self.setWindowTitle("Message app")
        self.setGeometry(700, 200, 500, 700)
        # Receiver name input
        self.receiver_input = QtWidgets.QLineEdit(self)
        self.receiver_input.setPlaceholderText("Send To...")
        self.receiver_input.resize(500, 40)
        self.receiver_input.move(0, 590)

        # Message text
        self.message_text = QtWidgets.QTextEdit(self)
        self.message_text.setPlaceholderText("Enter message...")
        self.message_text.resize(400, 70)
        self.message_text.move(0, 630)

        # Send button
        self.send_btn = QtWidgets.QPushButton(self)
        self.send_btn.setText("Send")
        self.send_btn.resize(100, 70)
        self.send_btn.move(400, 630)

        # Messages
        self.message_box_1 = QtWidgets.QLabel(self)
        self.message_box_1.setText("Loading...")
        self.message_box_1.resize(500, 100)
        self.message_box_1.move(0, 30)
        self.message_box_1.setAlignment(QtCore.Qt.AlignTop)
        self.message_box_1.setStyleSheet('border: 1px solid #000;')

        self.message_box_2 = QtWidgets.QLabel(self)
        self.message_box_2.setText("Loading...")
        self.message_box_2.resize(500, 100)
        self.message_box_2.move(0, 130)
        self.message_box_2.setAlignment(QtCore.Qt.AlignTop)
        self.message_box_2.setStyleSheet('border: 1px solid #000;')

        self.message_box_3 = QtWidgets.QLabel(self)
        self.message_box_3.setText("Loading...")
        self.message_box_3.resize(500, 100)
        self.message_box_3.move(0, 230)
        self.message_box_3.setAlignment(QtCore.Qt.AlignTop)
        self.message_box_3.setStyleSheet('border: 1px solid #000;')

        self.message_box_4 = QtWidgets.QLabel(self)
        self.message_box_4.setText("Loading...")
        self.message_box_4.resize(500, 100)
        self.message_box_4.move(0, 330)
        self.message_box_4.setAlignment(QtCore.Qt.AlignTop)
        self.message_box_4.setStyleSheet('border: 1px solid #000;')

        self.message_box_5 = QtWidgets.QLabel(self)
        self.message_box_5.setText("Loading...")
        self.message_box_5.resize(500, 100)
        self.message_box_5.move(0, 430)
        self.message_box_5.setAlignment(QtCore.Qt.AlignTop)
        self.message_box_5.setStyleSheet('border: 1px solid #000;')

        # Message display and refresh
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.display_messages)
        self.timer.start(10000)

        # Message box
        self.succ_send = QMessageBox()
        self.succ_send.setWindowTitle("Status")
        self.succ_send.setText("Message sent successfully")
        self.succ_send.setWindowIcon(QtGui.QIcon('message.png'))
        self.succ_send.setStandardButtons(QMessageBox.Ok)

        self.error = QMessageBox()
        self.error.setWindowTitle("Status")
        self.error.setText("To send and receive messages you have to add account name! ")
        self.error.setWindowIcon(QtGui.QIcon('message.png'))
        self.error.setIcon(QMessageBox.Warning)
        self.error.setStandardButtons(QMessageBox.Ok)

        # Menu bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        account_menu = QMenu('&Account', self)
        self.menu_bar.addMenu(account_menu)
        account_menu.addAction('Add', self.add_account)

    def display_messages(self):
        # Message display func
        url = f'https://chatapp.pythonanywhere.com/get_info/t=genajgiriakaroche/who={self.m_sender}'
        response = requests.get(url=url).json()
        if self.m_sender == "":
            self.error.exec_()
        elif len(response) == 0:
            self.message_box_1.setText(f"You have no messages")
            self.message_box_2.setText(f"You have no messages")
            self.message_box_3.setText(f"You have no messages")
            self.message_box_4.setText(f"You have no messages")
            self.message_box_5.setText(f"You have no messages")
        else:
            messages = sorted(response, key=lambda d: d['id'])
            if len(messages) >= 5:
                self.message_box_1.setText(f"From: {messages[-1]['sender']} \n{messages[-1]['message']}")
                self.message_box_2.setText(f"From: {messages[-2]['sender']} \n{messages[-2]['message']}")
                self.message_box_3.setText(f"From: {messages[-3]['sender']} \n{messages[-3]['message']}")
                self.message_box_4.setText(f"From: {messages[-4]['sender']} \n{messages[-4]['message']}")
                self.message_box_5.setText(f"From: {messages[-5]['sender']} \n{messages[-5]['message']}")
            elif len(messages) == 1:
                self.message_box_1.setText(f"From: {messages[-1]['sender']} \n{messages[-1]['message']}")
            elif len(messages) == 2:
                self.message_box_1.setText(f"From: {messages[-1]['sender']} \n{messages[-1]['message']}")
                self.message_box_2.setText(f"From: {messages[-2]['sender']} \n{messages[-2]['message']}")
            elif len(messages) == 3:
                self.message_box_1.setText(f"From: {messages[-1]['sender']} \n{messages[-1]['message']}")
                self.message_box_2.setText(f"From: {messages[-2]['sender']} \n{messages[-2]['message']}")
                self.message_box_3.setText(f"From: {messages[-3]['sender']} \n{messages[-3]['message']}")
                self.message_box_4.setText(f"From: {messages[-4]['sender']} \n{messages[-4]['message']}")
            elif len(messages) == 4:
                self.message_box_1.setText(f"From: {messages[-1]['sender']} \n{messages[-1]['message']}")
                self.message_box_2.setText(f"From: {messages[-2]['sender']} \n{messages[-2]['message']}")
                self.message_box_3.setText(f"From: {messages[-3]['sender']} \n{messages[-3]['message']}")
                self.message_box_4.setText(f"From: {messages[-4]['sender']} \n{messages[-4]['message']}")

        self.update()

    def send_message(self, sender, receiver, message):
        # Message send func
        if self.m_sender == "":
            self.error.exec_()
        else:
            url = f'https://chatapp.pythonanywhere.com/add/t=genajgiriakaroche'
            requests.post(json={'sender': sender,
                                'receiver': receiver,
                                'message': message}, url=url)
            self.succ_send.exec_()

    def send_btn_clicked(self):
        # Send button click func
        self.send_btn.clicked.connect(lambda: self.send_message(self.m_sender,
                                                                self.receiver_input.text(),
                                                                self.message_text.toPlainText()))

    def add_account(self):
        # Account add func
        action = self.sender()
        if action.text() == "Add":
            n, s = QtWidgets.QInputDialog.getText(self, "Add", "Enter your name:")
            self.m_sender = n


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
