# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditClient.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(335, 413)
        MainWindow.setStyleSheet("background-color: rgb(255, 223, 194)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 141, 20))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 80, 141, 20))
        self.lineEdit_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 120, 141, 20))
        self.lineEdit_3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 160, 141, 20))
        self.lineEdit_4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 200, 141, 20))
        self.lineEdit_5.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(130, 240, 141, 22))
        self.dateEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 320, 141, 22))
        self.comboBox.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(130, 280, 141, 20))
        self.lineEdit_7.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 360, 75, 23))
        self.pushButton.setStyleSheet("background-color:rgb(208, 219, 255)")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 280, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 320, 47, 13))
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 360, 75, 23))
        self.pushButton_2.setStyleSheet("background-color:rgb(208, 219, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактирование клиента"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.label_3.setText(_translate("MainWindow", "Отчество"))
        self.label_4.setText(_translate("MainWindow", "Почта"))
        self.label_5.setText(_translate("MainWindow", "Телефон"))
        self.label_6.setText(_translate("MainWindow", "День рождения"))
        self.label_7.setText(_translate("MainWindow", "Фото"))
        self.label_8.setText(_translate("MainWindow", "Пол"))
        self.pushButton_2.setText(_translate("MainWindow", "Отмена"))



