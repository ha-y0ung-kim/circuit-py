from PyQt5.QtWidgets import QApplication, QFrame, QMainWindow

app = QApplication([])
frm = QFrame()
win = QMainWindow()
win.setCentralWidget(frm)
win.resize(1000,500)
win.show()
app.exec_()