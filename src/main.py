from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_main import Ui_MainWindow
import pandas as pd
import matplotlib.pyplot as plt
import os


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.submitBtn.clicked.connect(self.fileUpload)
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
            self.ui.inputText.setText(f"File uploaded:\n{files}")
            self.genPlot(files)
        self.dragLeaveEvent(event)

    def fileUpload(self):
        file_path, _ = QFileDialog.getOpenFileNames(
            self,
            "Select a files to upload",
            "",
            "Excel Files (*.xlsx *.xls);;CSV Files (*.csv);;All Files (*)",
        )

        if file_path:
            print("Selected file:", file_path)
            self.genPlot(file_path)
        else:
            print("No file selected")

    def genPlot(self, file_paths):
        try:

            for file in file_paths:

                df = pd.read_excel(file)

                mili = df["Milliseconds"]
                value = df["Value"]

                plt.figure()
                plt.plot(mili, value, color="orange")
                plt.xlabel("Milisecond")
                plt.ylabel("Value")
                plt.title(f"CNC plot - {os.path.basename(file)}")
                plt.show()
        except Exception as e:
            self.ui.inputText.setText(f"Error reading file: {str(e)}")
            print(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication([])
    widget = UI()
    widget.resize(500, 500)
    widget.show()
    app.exec()
