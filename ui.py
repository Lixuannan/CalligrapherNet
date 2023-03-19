# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(559, 557)
        self.verticalLayout = QVBoxLayout(Window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.photo_view = QLabel(Window)
        self.photo_view.setObjectName(u"photo_view")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photo_view.sizePolicy().hasHeightForWidth())
        self.photo_view.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.photo_view.setFont(font)
        self.photo_view.setLayoutDirection(Qt.LeftToRight)
        self.photo_view.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.photo_view)

        self.widget = QWidget(Window)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.result_lable = QLabel(self.widget)
        self.result_lable.setObjectName(u"result_lable")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.result_lable.sizePolicy().hasHeightForWidth())
        self.result_lable.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(17)
        self.result_lable.setFont(font1)

        self.horizontalLayout.addWidget(self.result_lable)

        self.choose_photo_button = QPushButton(self.widget)
        self.choose_photo_button.setObjectName(u"choose_photo_button")
        font2 = QFont()
        font2.setPointSize(16)
        self.choose_photo_button.setFont(font2)

        self.horizontalLayout.addWidget(self.choose_photo_button)

        self.run_button = QPushButton(self.widget)
        self.run_button.setObjectName(u"run_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy3)
        self.run_button.setFont(font2)
        self.run_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.run_button)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"CalligrapherGui", None))
        self.photo_view.setText(QCoreApplication.translate("Window", u"\u8bf7\u9009\u62e9\u56fe\u7247", None))
        self.result_lable.setText(QCoreApplication.translate("Window", u"\u8ba1\u7b97\u7ed3\u679c\uff1a", None))
        self.choose_photo_button.setText(QCoreApplication.translate("Window", u"\u9009\u62e9\u56fe\u7247", None))
        self.run_button.setText(QCoreApplication.translate("Window", u"\u5f00\u59cb", None))
    # retranslateUi

