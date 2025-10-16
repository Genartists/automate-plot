from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui_main import Ui_MainWindow
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.submitBtn.clicked.connect(self.fileBrowse)
        self.setAcceptDrops(True)

    # enable drag event
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.ui.dropFrame.setStyleSheet(
                """
                QFrame#dropFrame {
                    border: 2px dashed #4CAF50;
                    border-radius: 16px;
                    background: #4CAF50;
                }
                QLabel#dropHint {
                    color: #4CAF50;
                }
            """
            )

    def dragLeaveEvent(self, event):
        # Reset back to the original style from your UI file
        self.ui.dropFrame.setStyleSheet(
            """
            QFrame#dropFrame {
                border: 2px dashed #9ca3af;
                border-radius: 16px;
                background: #f9fafb;
            }
            QLabel#dropHint {
                color: #4b5563;
            }
        """
        )

    def dropEvent(self, event):
        files = [
            url.toLocalFile() for url in event.mimeData().urls()
        ]  # search dragged file path

        if files:
            # self.ui.inputText.setText(f"File uploaded:\n{files}")
            self.generatePlot(files)
        self.dragLeaveEvent(event)

    def fileBrowse(self):
        filePath, _ = QFileDialog.getOpenFileNames(
            self,
            "Select a files to upload",
            "",
            "Excel Files (*.xlsx *.xls);;CSV Files (*.csv)",
        )

        if filePath:
            print("Selected file:", filePath)
            self.generatePlot(filePath)
        else:
            print("No file selected")

    def generatePlot(self, filePaths):

        try:
            for file in filePaths:
                if ".csv" in os.path.basename(file):
                    df = pd.read_csv(file)
                elif ".xlsx" in os.path.basename(file):
                    df = pd.read_excel(file)
                df.columns = df.columns.str.strip()

                mili = df["Milliseconds"]
                value = df["Value"]

                # print(mili)
                # print(value)
                
                plt.plot(mili, value, label=f"{os.path.basename(file)}")
                # plt.xticks(np.arange(mili.min(), mili.max()))
                # plt.yticks(np.arange(value.min(), value.max()))

            plt.xlabel("Milliseconds")
            plt.ylabel("Force (KN)")
            plt.title(f"Bushing Push in Data")
            plt.legend()
            plt.show()
        except Exception as e:
            QMessageBox.warning(
                self,
                "Error",
                "Wrong file format! Should be .csv or .xlsx",
            )
            print(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication([])
    widget = UI()
    widget.resize(500, 500)
    widget.show()
    app.exec()
