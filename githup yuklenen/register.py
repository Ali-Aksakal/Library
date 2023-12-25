from PyQt5.QtWidgets import *
from registerpage import Ui_registerpage
import sqlite3

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.registerform = Ui_registerpage()
        self.registerform.setupUi(self)
        self.kullanici_vt()
        self.registerform.pushButton_kayit.clicked.connect(self.kullanici_kayit)


    def kullanici_vt(self):
        with sqlite3.connect("users.db") as vt:
            im = vt.cursor()
            im.execute("CREATE TABLE IF NOT EXISTS users(kullaniciId integer PRIMARY KEY ,kullanici_adi text, sifre text, mail_adresi text)")

            vt.commit()

    def kullanici_kayit(self):
        user    = self.registerform.lineEdit_kullaniciadi.text()
        pasword = self.registerform.lineEdit_sifre.text()
        mail    = self.registerform.lineEdit_mailadresi.text()

        with sqlite3.connect("users.db") as vt:
            im = vt.cursor()

            im.execute("INSERT INTO users('kullanici_adi', 'sifre', 'mail_adresi') VALUES (?,?,?)",
                        (user, pasword, mail))

            vt.commit()
            self.hide()






