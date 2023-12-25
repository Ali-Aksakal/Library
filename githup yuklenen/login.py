from PyQt5.QtWidgets import *
from loginpage import Ui_loginpage
from addbook import AddBook
import sqlite3

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.loginform = Ui_loginpage()
        self.loginform.setupUi(self)
        self.loginform.pushButton_giris.clicked.connect(self.girisYap)
        self.addbookopen = AddBook()

    def girisYap(self):
        with sqlite3.connect("users.db") as vt:
            self.im = vt.cursor()
            kullanici_adi = self.loginform.lineEdit_kullaniciadi.text()
            sifre = self.loginform.lineEdit_sifre.text()
            self.im.execute("SELECT kullanici_adi,sifre FROM users WHERE kullanici_adi=?", (kullanici_adi,))

            veriler = self.im.fetchall()
            for veri in veriler:
                user = veri[0]
                pasword = veri[1]
                if user == kullanici_adi and pasword == sifre:
                    self.hide()
                    self.addbookopen.show()
            vt.commit()



