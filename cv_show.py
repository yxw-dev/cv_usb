# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cv_show.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1509, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_cam = QtWidgets.QPushButton(self.centralwidget)
        self.open_cam.setGeometry(QtCore.QRect(30, 40, 112, 34))
        self.open_cam.setObjectName("open_cam")
        self.close_cam = QtWidgets.QPushButton(self.centralwidget)
        self.close_cam.setGeometry(QtCore.QRect(30, 130, 112, 34))
        self.close_cam.setObjectName("close_cam")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 37, 561, 481))
        self.label.setObjectName("label")
        self.open_cam_2 = QtWidgets.QPushButton(self.centralwidget)
        self.open_cam_2.setGeometry(QtCore.QRect(30, 80, 112, 34))
        self.open_cam_2.setObjectName("open_cam_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 20, 561, 481))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1509, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_cam.setText(_translate("MainWindow", "打开相机1"))
        self.close_cam.setText(_translate("MainWindow", "关闭相机"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.open_cam_2.setText(_translate("MainWindow", "打开相机2"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))

