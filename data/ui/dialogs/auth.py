# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(337, 348)
        Dialog.setStyleSheet(u"")
        Dialog.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.catalog_frame = QFrame(Dialog)
        self.catalog_frame.setObjectName(u"catalog_frame")
        self.catalog_frame.setFrameShape(QFrame.StyledPanel)
        self.catalog_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.catalog_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.catalog_label = QLabel(self.catalog_frame)
        self.catalog_label.setObjectName(u"catalog_label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.catalog_label.setFont(font)

        self.horizontalLayout.addWidget(self.catalog_label)


        self.verticalLayout_2.addWidget(self.catalog_frame)

        self.one_frame = QFrame(Dialog)
        self.one_frame.setObjectName(u"one_frame")
        self.one_frame.setStyleSheet(u"")
        self.one_frame.setFrameShape(QFrame.StyledPanel)
        self.one_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.one_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.auth_code_line = QLineEdit(self.one_frame)
        self.auth_code_line.setObjectName(u"auth_code_line")

        self.horizontalLayout_2.addWidget(self.auth_code_line)

        self.label = QLabel(self.one_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.get_code_btn = QPushButton(self.one_frame)
        self.get_code_btn.setObjectName(u"get_code_btn")
        self.get_code_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.get_code_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.one_frame)

        self.two_frame = QFrame(Dialog)
        self.two_frame.setObjectName(u"two_frame")
        self.two_frame.setFrameShape(QFrame.StyledPanel)
        self.two_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.two_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.login_line = QLineEdit(self.two_frame)
        self.login_line.setObjectName(u"login_line")

        self.horizontalLayout_5.addWidget(self.login_line)

        self.label_2 = QLabel(self.two_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.password_line = QLineEdit(self.two_frame)
        self.password_line.setObjectName(u"password_line")

        self.horizontalLayout_6.addWidget(self.password_line)

        self.label_3 = QLabel(self.two_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addWidget(self.two_frame)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.auth_btn = QPushButton(self.frame)
        self.auth_btn.setObjectName(u"auth_btn")
        self.auth_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.auth_btn)

        self.horizontalSpacer_2 = QSpacerItem(254, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.catalog_label.setText(QCoreApplication.translate("Dialog", u"Shikimori", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Authorization code", None))
        self.get_code_btn.setText(QCoreApplication.translate("Dialog", u"Get code", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.auth_btn.setText(QCoreApplication.translate("Dialog", u"Sign in", None))
    # retranslateUi

