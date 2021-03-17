from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import QtCore
import sys

class UiLoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 300, 180)
        self.setWindowTitle('Вход в систему')


        self.info_label = QLabel(self)
        self.info_label.setText("Неверный логин или пароль")
        self.info_label.move(10, 90)
        self.info_label.resize(self.info_label.sizeHint())
        self.info_label.setStyleSheet('color: red')
        self.info_label.hide()

        self.login = QLabel("Логин:", self)
        self.login.move(10, 10)
        self.login.resize(self.login.sizeHint())

        self.password = QLabel("Пароль:", self)
        self.password.move(10, 40)
        self.password.resize(self.password.sizeHint())

        self.login_line_edit = QLineEdit(self)
        self.login_line_edit.move(65, 10)
        self.login_line_edit.resize(200, 20)


        self.password_line_edit = QLineEdit(self)
        self.password_line_edit.move(65, 40)
        self.password_line_edit.resize(200, 20)
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.go_in = QPushButton("Войти", self)
        self.go_in.move(60, 60)
        self.go_in.resize(100, 30)
        self.go_in.pressed.connect(self.log_in_system)

        self.back = QPushButton("Отмена", self)
        self.back.move(150, 60)
        self.back.resize(100, 30)
        self.back.pressed.connect(self.closing)


    def log_in_system(self):
        self.info_label.show()

    def closing(self):
        UiLoginWindow.close(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = UiLoginWindow()
    MainWindow.show()
    sys.exit(app.exec())