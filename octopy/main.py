import sys
from PySide.QtGui import QApplication

from octopy.controller.home import HomeController

app = QApplication(sys.argv)
controller = HomeController()
view = controller.view
sys.exit(app.exec_())
