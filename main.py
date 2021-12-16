import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.setGeometry(100, 100, 1080, 920)
window.show()

app.exec()
