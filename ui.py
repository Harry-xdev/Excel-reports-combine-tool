from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.setGeometry(100, 200, 400, 300)

		self.setStyleSheet("""
			background-color: #f2f2f2;
			color: #333333
			""")
		button = QPushButton('Submit', self)
		button.setStyleSheet("""
			background-color : grey;
			color: white;
			border: none;
			padding: 10px 20px;
			""")
		button.move(50, 50)
		button.clicked.connect(self.on_button_clicked)

	def on_button_clicked(self):
		print('button clicked.')

if __name__ == '__main__':
	app = QApplication([])
	window = MainWindow()
	window.show()
	app.exec()