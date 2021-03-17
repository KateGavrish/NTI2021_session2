from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QFont
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox, QMainWindow
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import sys
from PyQt5 import QtCore

from data.__all_models import *
from data import db_session
from data.comission import Comission
from data.direction import Direction
from data.education import EducationStudent
from data.users_students import UserStudent
from data.info_about_student import InfoStudent


db_session.global_init(f"db/project.sqlite")
SEX = {'male': 1, 'female': 0, 'Мужской': 1, 'Женский': 0, 1: 'Мужской', 0: 'Женский'}

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

        self.MainWin = Session3()

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

    def open_list(self):
        self.MainWin.__init__()
        self.MainWin.show()
        self.close()

    def log_in_system(self):
        session = db_session.create_session()
        f = session.query(Comission).filter(Comission.login == self.login_line_edit.text()).first()
        f1 = session.query(Comission).filter(Comission.password == self.password_line_edit.text()).first()
        if f and f1:
            self.open_list()
        else:
            self.info_label.show()

    def closing(self):
        UiLoginWindow.close(self)

class Ui_Session3(object):
    def setupUi(self, Session3):
        Session3.setObjectName("Session3")
        Session3.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Session3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 351, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(16)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 741, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(30, 510, 151, 51))
        self.run.setObjectName("run")
        self.close_ = QtWidgets.QPushButton(self.centralwidget)
        self.close_.setGeometry(QtCore.QRect(190, 510, 141, 51))
        self.close_.setObjectName("close")
        Session3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Session3)
        self.statusbar.setObjectName("statusbar")
        Session3.setStatusBar(self.statusbar)

        self.state = QComboBox(self)
        self.state.setGeometry(QtCore.QRect(400, 10, 221, 31))
        self.state.setObjectName("state")

        self.retranslateUi(Session3)
        QtCore.QMetaObject.connectSlotsByName(Session3)

    def retranslateUi(self, Session3):
        _translate = QtCore.QCoreApplication.translate
        Session3.setWindowTitle(_translate("Session2", "Session3"))
        self.label.setText(_translate("Session3", "Список абитуриентов"))
        self.run.setText(_translate("Session3", "Выбрать"))
        self.close_.setText(_translate("Session3", "Закрыть"))


class Session3(QMainWindow, Ui_Session3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.size_table = 0

        self.run.clicked.connect(self.choose)
        self.close_.clicked.connect(self.close_win)

        session = db_session.create_session()
        self.students = []
        d = session.query(InfoStudent).all()

        for x in d:
            f = session.query(UserStudent).filter(UserStudent.email == x.email).first()
            f1 = session.query(EducationStudent).filter(EducationStudent.id == x.id).first()
            if not f.step1 and not f.step2:
                status = 'Новый'
            elif f.step1 and not f.step2:
                status = 'В работе'
            elif not f1.is_original:
                status = 'Комплект без оригинала'
            elif f1.is_original:
                status = 'Полный комплект'
            else:
                status = 'В работе'
            self.students.append([f.surname + ' ' + f.name + ' ' + f.middle_name, SEX[SEX[x.sex]], x.email, x.phone, status])

        self.info_output()


    def choose(self):
        print(self.state.currentIndex())
        print(self.students[self.state.currentIndex()])

        session = db_session.create_session()

    def info_output(self):
        """Вывод информации в таблицу"""
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(self.students))
        self.size_table = len(self.students)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ФИО"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Пол"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("E-mail"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Телефон"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Cтатус"))
        i = 1
        for items in self.students:
            self.tableWidget.setRowCount(i)
            for j in range(len(items)):
                itm = QTableWidgetItem(f'{items[j]}')
                itm.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i - 1, j, itm)
            i += 1

        self.tableWidget.resizeColumnsToContents()
        self.table_Rows_size = i - 1
        i = 1
        for t in self.students:
            self.state.addItem(str(i) + ' ' + str(t[0]))

        self.tableWidget.resizeColumnsToContents()

    def close_win(self):
        """Закрытие программы"""
        self.close()

    def read_table(self):
        """ эта функция возвращает данные таблицы
            список состоит из списков,  вот так:
            [["комплектющее", "серийный номер", "количество"]]"""

        info_table = []
        for i in range(self.size_table):
            a = []
            for j in range(3):
                a.append(self.tableWidget.item(i, j).text())
            info_table.append(a)
        return info_table


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = Session3()
    LogWindow = UiLoginWindow()
    LogWindow.show()
    sys.exit(app.exec())
