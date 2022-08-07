# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import desu_res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(451, 432)
        Form.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header_frame = QFrame(Form)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.back_btn = QPushButton(self.header_frame)
        self.back_btn.setObjectName(u"back_btn")
        icon = QIcon()
        icon.addFile(u":/icons/images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.back_btn)

        self.horizontalSpacer_2 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lib_frame = QFrame(self.header_frame)
        self.lib_frame.setObjectName(u"lib_frame")
        self.lib_frame.setFrameShape(QFrame.StyledPanel)
        self.lib_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.lib_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.lib_list_box = QComboBox(self.lib_frame)
        self.lib_list_box.setObjectName(u"lib_list_box")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lib_list_box.sizePolicy().hasHeightForWidth())
        self.lib_list_box.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lib_list_box)

        self.add_btn = QPushButton(self.lib_frame)
        self.add_btn.setObjectName(u"add_btn")

        self.horizontalLayout.addWidget(self.add_btn)


        self.verticalLayout_7.addWidget(self.lib_frame)

        self.shikimori_frame = QFrame(self.header_frame)
        self.shikimori_frame.setObjectName(u"shikimori_frame")
        self.shikimori_frame.setFrameShape(QFrame.StyledPanel)
        self.shikimori_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.shikimori_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.shikimori_btn = QPushButton(self.shikimori_frame)
        self.shikimori_btn.setObjectName(u"shikimori_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/shikimori.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shikimori_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.shikimori_btn)


        self.verticalLayout_7.addWidget(self.shikimori_frame)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addWidget(self.header_frame)

        self.manga_layout = QVBoxLayout()
        self.manga_layout.setObjectName(u"manga_layout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.image_frame = QFrame(Form)
        self.image_frame.setObjectName(u"image_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_frame.sizePolicy().hasHeightForWidth())
        self.image_frame.setSizePolicy(sizePolicy1)
        self.image_frame.setFrameShape(QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.image_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.image = QLabel(self.image_frame)
        self.image.setObjectName(u"image")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy2)
        self.image.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.image)


        self.horizontalLayout_4.addWidget(self.image_frame)

        self.title_frame = QFrame(Form)
        self.title_frame.setObjectName(u"title_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy3)
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.title_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.name_label = QLabel(self.title_frame)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.name_label)

        self.russian_label = QLabel(self.title_frame)
        self.russian_label.setObjectName(u"russian_label")
        self.russian_label.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.russian_label)

        self.verticalSpacer = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.title_frame)


        self.manga_layout.addLayout(self.horizontalLayout_4)

        self.score_frame = QFrame(Form)
        self.score_frame.setObjectName(u"score_frame")
        sizePolicy2.setHeightForWidth(self.score_frame.sizePolicy().hasHeightForWidth())
        self.score_frame.setSizePolicy(sizePolicy2)
        self.score_frame.setStyleSheet(u"QPushButton {\n"
"	padding: 5px 1px;\n"
"    background: transparent;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	font-weight: bold;\n"
"	icon-size: 24px;\n"
"}")
        self.score_frame.setFrameShape(QFrame.StyledPanel)
        self.score_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.score_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.score_label = QLabel(self.score_frame)
        self.score_label.setObjectName(u"score_label")

        self.verticalLayout_4.addWidget(self.score_label)

        self.stars_layout = QHBoxLayout()
        self.stars_layout.setObjectName(u"stars_layout")
        self.star_1 = QPushButton(self.score_frame)
        self.star_1.setObjectName(u"star_1")
        self.star_1.setEnabled(False)

        self.stars_layout.addWidget(self.star_1)

        self.star_2 = QPushButton(self.score_frame)
        self.star_2.setObjectName(u"star_2")
        self.star_2.setEnabled(False)

        self.stars_layout.addWidget(self.star_2)

        self.star_3 = QPushButton(self.score_frame)
        self.star_3.setObjectName(u"star_3")
        self.star_3.setEnabled(False)

        self.stars_layout.addWidget(self.star_3)

        self.star_4 = QPushButton(self.score_frame)
        self.star_4.setObjectName(u"star_4")
        self.star_4.setEnabled(False)

        self.stars_layout.addWidget(self.star_4)

        self.star_5 = QPushButton(self.score_frame)
        self.star_5.setObjectName(u"star_5")
        self.star_5.setEnabled(False)

        self.stars_layout.addWidget(self.star_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.stars_layout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.stars_layout)


        self.manga_layout.addWidget(self.score_frame)

        self.related_layout = QHBoxLayout()
        self.related_layout.setObjectName(u"related_layout")
        self.related_frame = QFrame(Form)
        self.related_frame.setObjectName(u"related_frame")
        self.related_frame.setFrameShape(QFrame.StyledPanel)
        self.related_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.related_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.related_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.related_list = QListWidget(self.related_frame)
        self.related_list.setObjectName(u"related_list")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.related_list.sizePolicy().hasHeightForWidth())
        self.related_list.setSizePolicy(sizePolicy4)
        self.related_list.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.related_list)


        self.related_layout.addWidget(self.related_frame)

        self.characters_frame = QFrame(Form)
        self.characters_frame.setObjectName(u"characters_frame")
        sizePolicy2.setHeightForWidth(self.characters_frame.sizePolicy().hasHeightForWidth())
        self.characters_frame.setSizePolicy(sizePolicy2)
        self.characters_frame.setMinimumSize(QSize(0, 0))
        self.characters_frame.setFrameShape(QFrame.StyledPanel)
        self.characters_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.characters_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.characters_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_11.addWidget(self.label_2)

        self.characters_list = QListWidget(self.characters_frame)
        self.characters_list.setObjectName(u"characters_list")

        self.verticalLayout_11.addWidget(self.characters_list)


        self.related_layout.addWidget(self.characters_frame)


        self.manga_layout.addLayout(self.related_layout)

        self.description_frame = QFrame(Form)
        self.description_frame.setObjectName(u"description_frame")
        self.description_frame.setFrameShape(QFrame.StyledPanel)
        self.description_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.description_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.description_text = QTextEdit(self.description_frame)
        self.description_text.setObjectName(u"description_text")
        self.description_text.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.description_text)


        self.manga_layout.addWidget(self.description_frame)


        self.verticalLayout_10.addLayout(self.manga_layout)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)

        self.items_frame = QFrame(Form)
        self.items_frame.setObjectName(u"items_frame")
        self.items_frame.setFrameShape(QFrame.StyledPanel)
        self.items_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.items_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.items_list = QListWidget(self.items_frame)
        self.items_list.setObjectName(u"items_list")
        self.items_list.setWordWrap(True)

        self.verticalLayout.addWidget(self.items_list)


        self.horizontalLayout_5.addWidget(self.items_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.back_btn.setText("")
        self.add_btn.setText("")
        self.shikimori_btn.setText("")
        self.image.setText("")
        self.name_label.setText(QCoreApplication.translate("Form", u"name", None))
        self.russian_label.setText(QCoreApplication.translate("Form", u"russian", None))
        self.score_label.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.star_1.setText("")
        self.star_2.setText("")
        self.star_3.setText("")
        self.star_4.setText("")
        self.star_5.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u0436\u0438", None))
    # retranslateUi
