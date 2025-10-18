from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui_main import Ui_MainWindow
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import os

# Set style for plot
plt.style.use(["science", "notebook", "grid"])


class UI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = (
            Ui_MainWindow()
        )  # set up UI from ui main by making object for mainwindow class
        self.ui.setupUi(self)
        self.ui.submitBtn.clicked.connect(self.fileBrowse)  # Handle click event Pyside6
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

    # Choose a file from local system
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
            # Each file uploaded will be read with pandas
            for file in filePaths:
                if file.lower().endswith(".csv"):
                    df = pd.read_csv(file)
                elif file.lower().endswith(".xlsx"):
                    df = pd.read_excel(file)
                else:
                    continue

                df.columns = df.columns.str.strip()

                mili = df["Milliseconds"]
                value = df["Value"]

                # Create plot with two column inside the files
                plt.plot(mili, value, label=f"{os.path.basename(file)}")

            # Create annotation and allow on hover effect for graphs
            cursor = mplcursors.cursor(
                highlight=True,
                hover=mplcursors.HoverMode.Transient,
                # Customize highlight attribute
                highlight_kwargs=dict(
                    color="#E7E7E7",
                    linewidth=2,
                    alpha=0.5,
                ),
            )

            # Customize annotation with connect function
            @cursor.connect("add")
            def _(sel):
                sel.annotation.get_bbox_patch().set(fc="#253342")
                sel.annotation.set_text(
                    f"{sel.artist.get_label()}\n{df.columns[1]} = {sel.target[0]:.0f}\nForce (KN) = {sel.target[1]:.2f}"
                )

            # Show and naming plot
            plt.xlabel("Milliseconds")
            plt.ylabel("Force (KN)")
            plt.title(f"Bushing Push in Data")
            plt.legend().set_draggable(True)
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
