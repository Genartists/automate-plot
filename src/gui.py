from PyQt5.QtWidgets import QApplication, QLabel, QInputDialog

app = QApplication([])

intput = QInputDialog.getText('Input', 'Enter your name:')

label = QLabel("")
label.setText(input)
label.show()
app.exec_()