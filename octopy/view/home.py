from PySide.QtGui import QListWidget, QGridLayout
from . import View


class HomeView(View):

	def display(self):
		grid = QGridLayout()
		grid.setSpacing(10)

		qlistWidget = QListWidget()

		for repo in self.args.user.repositories():
			qlistWidget.addItem(repo.name)

		grid.addWidget(qlistWidget)

		self.setLayout(grid)
		self.show()
