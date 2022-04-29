# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shikimoriUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(894, 574)
        Form.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_mylist = QtWidgets.QPushButton(Form)
        self.btn_mylist.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.btn_mylist.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/library.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_mylist.setIcon(icon)
        self.btn_mylist.setObjectName("btn_mylist")
        self.verticalLayout_2.addWidget(self.btn_mylist)
        self.btn_main = QtWidgets.QPushButton(Form)
        self.btn_main.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.btn_main.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_main.setIcon(icon1)
        self.btn_main.setObjectName("btn_main")
        self.verticalLayout_2.addWidget(self.btn_main)
        self.btn_shikimori = QtWidgets.QPushButton(Form)
        self.btn_shikimori.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.btn_shikimori.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/shikimori.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_shikimori.setIcon(icon2)
        self.btn_shikimori.setObjectName("btn_shikimori")
        self.verticalLayout_2.addWidget(self.btn_shikimori)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_manga = QtWidgets.QListWidget(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 133, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 240, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 133, 62))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 240, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 240, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.list_manga.setPalette(palette)
        self.list_manga.setAutoFillBackground(False)
        self.list_manga.setObjectName("list_manga")
        self.verticalLayout.addWidget(self.list_manga)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prev_page = QtWidgets.QPushButton(Form)
        self.prev_page.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.prev_page.setObjectName("prev_page")
        self.horizontalLayout_2.addWidget(self.prev_page)
        self.label_page = QtWidgets.QLabel(Form)
        self.label_page.setTextFormat(QtCore.Qt.AutoText)
        self.label_page.setAlignment(QtCore.Qt.AlignCenter)
        self.label_page.setObjectName("label_page")
        self.horizontalLayout_2.addWidget(self.label_page)
        self.next_page = QtWidgets.QPushButton(Form)
        self.next_page.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.next_page.setObjectName("next_page")
        self.horizontalLayout_2.addWidget(self.next_page)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.b_planned = QtWidgets.QPushButton(Form)
        self.b_planned.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.b_planned.setObjectName("b_planned")
        self.verticalLayout_4.addWidget(self.b_planned)
        self.b_completed = QtWidgets.QPushButton(Form)
        self.b_completed.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.b_completed.setObjectName("b_completed")
        self.verticalLayout_4.addWidget(self.b_completed)
        self.b_watching = QtWidgets.QPushButton(Form)
        self.b_watching.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.b_watching.setObjectName("b_watching")
        self.verticalLayout_4.addWidget(self.b_watching)
        self.b_rewatching = QtWidgets.QPushButton(Form)
        self.b_rewatching.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.b_rewatching.setObjectName("b_rewatching")
        self.verticalLayout_4.addWidget(self.b_rewatching)
        self.b_on_hold = QtWidgets.QPushButton(Form)
        self.b_on_hold.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.b_on_hold.setObjectName("b_on_hold")
        self.verticalLayout_4.addWidget(self.b_on_hold)
        self.b_dropped = QtWidgets.QPushButton(Form)
        self.b_dropped.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.b_dropped.setObjectName("b_dropped")
        self.verticalLayout_4.addWidget(self.b_dropped)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.btn_auth = QtWidgets.QPushButton(Form)
        self.btn_auth.setStyleSheet("background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")
        self.btn_auth.setObjectName("btn_auth")
        self.verticalLayout_3.addWidget(self.btn_auth)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.prev_page.setText(_translate("Form", "<"))
        self.label_page.setText(_translate("Form", " Страница 1"))
        self.next_page.setText(_translate("Form", ">"))
        self.b_planned.setText(_translate("Form", "Запланировано"))
        self.b_completed.setText(_translate("Form", "Прочитано"))
        self.b_watching.setText(_translate("Form", "Читаю"))
        self.b_rewatching.setText(_translate("Form", "Перечитываю"))
        self.b_on_hold.setText(_translate("Form", "Отложено"))
        self.b_dropped.setText(_translate("Form", "Брошено"))
        self.btn_auth.setText(_translate("Form", "Войти"))
