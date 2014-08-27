from PySide.QtGui import QWidget


class Arguments(object):
	pass


class View(QWidget):
	args = Arguments()

	def assign(self, key, value):
		self.args.__dict__[key] = value
