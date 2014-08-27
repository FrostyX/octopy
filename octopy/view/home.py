from . import View
from PySide.QtGui import QListWidget,\
	QHBoxLayout,\
	QLabel


class HomeView(View):

	def display(self):
		layout = QHBoxLayout()
		layout.setSpacing(10)

		# Left panel - repositories
		qlistWidget = QListWidget()
		for repo in self.args.user.repositories():
			qlistWidget.addItem(repo.name)
		layout.addWidget (qlistWidget)


		# Middle panel - commits
		commitsLabel = QLabel("There will be the commits")
		layout.addWidget (commitsLabel)

		# Something
		somethingLabel = QLabel("There will be something")
		layout.addWidget (somethingLabel)

		self.setLayout(layout)
		self.show()
