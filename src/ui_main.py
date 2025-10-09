# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt, QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QStatusBar,
    QMenuBar,
    QSizePolicy,
    QSpacerItem,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 560)

        # --- Central ---
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self._root = QVBoxLayout(self.centralwidget)
        self._root.setContentsMargins(32, 28, 32, 28)
        self._root.setSpacing(18)

        # --- Title ---
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName("title")
        title_font = QFont()
        title_font.setPointSize(22)
        title_font.setBold(True)
        self.title.setFont(title_font)
        self.title.setAlignment(Qt.AlignCenter)
        self._root.addWidget(self.title)

        # --- Subtitle ---
        self.heading = QLabel(self.centralwidget)
        self.heading.setObjectName("heading")
        sub_font = QFont()
        sub_font.setPointSize(11)
        self.heading.setFont(sub_font)
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setStyleSheet("color:#6b7280;")  # neutral-500
        self._root.addWidget(self.heading)

        # spacer
        self._root.addItem(QSpacerItem(0, 4, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # --- Drop zone frame ---
        self.dropFrame = QFrame(self.centralwidget)
        self.dropFrame.setObjectName("dropFrame")
        self.dropFrame.setFrameShape(QFrame.NoFrame)
        self.dropFrame.setStyleSheet(
            """
            QFrame#dropFrame {
                border: 2px dashed #9ca3af;      /* neutral-400 */
                border-radius: 16px;
                background: #f9fafb;             /* neutral-50 */
            }
            QLabel#dropHint {
                color: #4b5563;                  /* neutral-600 */
            }
        """
        )
        drop_layout = QVBoxLayout(self.dropFrame)
        drop_layout.setContentsMargins(28, 28, 28, 28)
        drop_layout.setSpacing(10)

        # icon (keeps your original objectName "icon")
        self.icon = QLabel(self.dropFrame)
        self.icon.setObjectName("icon")
        self.icon.setAlignment(Qt.AlignCenter)
        self.icon.setPixmap(
            QPixmap("asset/upload.png").scaled(
                64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        drop_layout.addWidget(self.icon, 0, Qt.AlignHCenter)

        # drop hint
        self.dropHint = QLabel(self.dropFrame)
        self.dropHint.setObjectName("dropHint")
        hint_font = QFont()
        hint_font.setPointSize(12)
        self.dropHint.setFont(hint_font)
        self.dropHint.setAlignment(Qt.AlignCenter)
        drop_layout.addWidget(self.dropHint)

        self._root.addWidget(self.dropFrame, 1)

        # --- Path + Browse row (adds inputText + keeps submitBtn id) ---
        row = QHBoxLayout()
        row.setSpacing(10)

        self.inputText = QLineEdit(self.centralwidget)
        self.inputText.setObjectName("inputText")
        self.inputText.setPlaceholderText(
            "Select an Excel file (.xlsx, .xls) or drop it above…"
        )
        self.inputText.setClearButtonEnabled(True)
        row.addWidget(self.inputText, 1)

        self.submitBtn = QPushButton(self.centralwidget)
        self.submitBtn.setObjectName("submitBtn")
        self.submitBtn.setStyleSheet(
            "background-color: #06D6A0; color: black; font-weight: 900"
        )
        self.submitBtn.setMinimumSize(QSize(140, 36))
        row.addWidget(self.submitBtn, 0)

        self._root.addLayout(row)

        # --- Status line (optional) ---
        self.statusText = QLabel(self.centralwidget)
        self.statusText.setObjectName("statusText")
        self.statusText.setStyleSheet("color:#6b7280;")
        self.statusText.setText("")
        self._root.addWidget(self.statusText)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menu/Status bars
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.submitBtn.setDefault(True)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _t = QCoreApplication.translate
        MainWindow.setWindowTitle(_t("MainWindow", "Chart Automate CNC"))
        self.title.setText(_t("MainWindow", "Upload Excel"))
        self.heading.setText(
            _t("MainWindow", "Drop an Excel file or browse to auto-generate charts")
        )
        self.dropHint.setText(_t("MainWindow", "Drag & drop .xlsx / .xls here"))
        self.submitBtn.setText(_t("MainWindow", "Browse…"))
