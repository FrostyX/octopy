from octopy.view.home import HomeView
from octopy.model.user import User
from . import Controller


class HomeController(Controller):
	view = None

	def __init__(self):
		self.view = HomeView()
		self.view.assign("user", User('frostyx'))
		self.view.display()
