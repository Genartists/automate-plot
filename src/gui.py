from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow
import pandas as pd
import matplotlib.pyplot as plt
import os


class MyUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.submitBtn.clicked.connect(self.genPlot)

    def genPlot(self):
        # get text from input text object to form file name
        file = self.ui.inputText.text() + ".xlsx"

        if not os.path.exists(file):
            QMessageBox.warning(
                self,
                "File Not Found",
                "File doesn't exist! Please type the correct file name.",
            )

        else:
            try:
                df = pd.read_excel(file)

                mili = df["Milliseconds"]
                value = df["Value"]

                plt.plot(mili, value, color="orange")

                plt.xlabel("Milisecond")
                plt.ylabel("Value")
                plt.title("Laser CNC plot")

                plt.show()
            except Exception as e:
                self.ui.inputText.setText(f"Error reading file: {str(e)}")
                print(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication([])
    widget = MyUI()
    widget.resize(800, 800)
    widget.show()
    app.exec()
