import sys
from qt.layout import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('test')
        self.setCentralWidget(QLabel("centralWidget"))
        # self._createMenu()
        self._createToolBar()
        # self._createStatusBar()

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Ui_MainWindow()
    #win.resize(1000, 500)
    win.show()
    sys.exit(app.exec_())

# window.setWindowTitle('test')

#window.resize(1000, 500)
# window.show()
# sys.exit(app.exec_())
