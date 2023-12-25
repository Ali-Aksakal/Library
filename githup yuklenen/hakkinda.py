from PyQt5.QtWidgets import *
from hakkindapg import Ui_hakkinda

class HakkindaPage(QWidget):
    def __init__(self):
        super().__init__()
        self.hakkindaform = Ui_hakkinda()
        self.hakkindaform.setupUi(self)

