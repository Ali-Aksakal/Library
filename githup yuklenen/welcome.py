from PyQt5.QtWidgets import *
from welcomepage import Ui_welcomepage
from register import Register
from login import Login

class Welcome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.welcomeform = Ui_welcomepage()
        self.welcomeform.setupUi(self)
        self.loginpageopen = Login()
        self.registerpageopen = Register()
        self.welcomeform.pushButton.clicked.connect(self.GiriseGit)
        self.welcomeform.pushButton_2.clicked.connect(self.KaydaGit)

    def GiriseGit(self):
        self.loginpageopen.show()

    def KaydaGit(self):
        self.registerpageopen.show()



