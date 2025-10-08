# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'box.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.submitBtn = QPushButton(self.centralwidget)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(320, 320, 131, 51))
        self.inputText = QLineEdit(self.centralwidget)
        self.inputText.setObjectName(u"inputText")
        self.inputText.setGeometry(QRect(210, 220, 371, 41))
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(240, 90, 301, 91))
        font = QFont()
        font.setFamilies([u"SF Pro Display"])
        font.setPointSize(22)
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.title.setFont(font)
        self.title.setMouseTracking(False)
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(140, 70, 531, 381))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.frame.setFont(font1)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(10)
        self.frame.setMidLineWidth(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.submitBtn.raise_()
        self.inputText.raise_()
        self.title.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.submitBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.inputText.setInputMask("")
        self.inputText.setText("")
        self.inputText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your file name", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Automating Plot", None))
    # retranslateUi

