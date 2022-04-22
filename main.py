from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtSql import *
import sys

from ClientList import Ui_WindowListClients
from AddClient import Ui_AddClient
from AllClientVisit import Ui_WindowAllVisitClient
from EditClient import Ui_MainWindow


class Connect:
	def __init__(self, server, dbname, username, password):
		self.server = server
		self.dbname = dbname
		self.username = username
		self.password = password

	def get_connect(self):
		db = QSqlDatabase.addDatabase('QODBC')
		db.setDatabaseName(f'Driver={{SQL SERVER}}; '
						   f'Server={self.server}; '
						   f'Database={self.dbname}; '
						   f'UID={self.username}; '
						   f'PWD={self.password}')
		return db


app = QtWidgets.QApplication(sys.argv)

WindowListClients = QtWidgets.QMainWindow()
ui = Ui_WindowListClients()
ui.setupUi(WindowListClients)
WindowListClients.show()


def openAddClient():
	global AddClient
	AddClient = QtWidgets.QMainWindow()
	ui = Ui_AddClient()
	ui.setupUi(AddClient)
	AddClient.show()


ui.butClientVisit_2.clicked.connect(openAddClient)  #





class ClientCistZero(QtWidgets.QWidget):  ##################
	def __init__(self, FirstName, LastName, Patronymic, Birthday, RegistrationDate, Email, Phone, GenderCode,
				 PhotoPath):
		self.FirstName = FirstName
		self.LastName = LastName
		self.Patronymic = Patronymic
		self.Birthday = Birthday
		self.RegistrationDate = RegistrationDate
		self.Email = Email
		self.Phone = Phone
		self.GenderCode = GenderCode
		self.PhotoPath = PhotoPath
		QtWidgets.QWidget.__init__(self)
		self.picture = QtWidgets.QLabel()

	def ch_click(self):
		application.button_ch_min.setVisible(True)
		if self.check.isChecked():
			self.isCheck = True
			pass
		else:
			self.isCheck = False  #########################


def openEditClient():
	global MainWindow
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()


ui.butClientVisit_3.clicked.connect(openEditClient)


def openEditClient():
	global WindowAllVisitClient
	WindowAllVisitClient = QtWidgets.QMainWindow()
	ui = Ui_WindowAllVisitClient()
	ui.setupUi(WindowAllVisitClient)
	WindowAllVisitClient.show()


ui.butClientVisit.clicked.connect(openEditClient)

sys.exit(app.exec_())
