import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from addbookpage import Ui_addbook
from hakkinda import HakkindaPage
import sqlite3

class AddBook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.addbookform = Ui_addbook()
        self.addbookform.setupUi(self)
        self.hakkindaform = HakkindaPage()
        self.kitaplik_vt()
        self.listele()
        self.addbookform.pushButton_kaydet.clicked.connect(self.kitap_kayit)
        self.addbookform.pushButton_listele.clicked.connect(self.listele)
        self.addbookform.tableWidget.itemSelectionChanged.connect(self.Doldur)
        self.addbookform.pushButton_ara.clicked.connect(self.arama)
        self.addbookform.pushButton_guncelle.clicked.connect(self.Guncelle)
        self.addbookform.pushButton_sil.clicked.connect(self.sil)
        self.addbookform.pushButton_temizle.clicked.connect(self.temizle)
        self.addbookform.hakkinda.triggered.connect(self.Hakkinda)
        self.addbookform.pushButton_exit.clicked.connect(self.cikis)

    def kitaplik_vt(self):
        with sqlite3.connect("kitap.db") as vt:
            im = vt.cursor()
            im.execute("""CREATE TABLE IF NOT EXISTS kitap(kitapid integer PRIMARY KEY, kitap_adi text,Turu text, 
            Yazar text,Dil text, Cevirmen text, BasimYili text, BaskiSayisi text,Yayinevi text,KtpHk text,YzrHk text)""")
            vt.commit()

    def kitap_kayit(self):
        book_name = self.addbookform.lineEdit_kitabinadi.text()
        gender = self.addbookform.comboBox_kitabinturu.currentText()
        author = self.addbookform.lineEdit_yazar.text()
        language = self.addbookform.lineEdit_dili.text()
        interpreter = self.addbookform.lineEdit_cevirmen.text()
        publish_year = self.addbookform.dateEdit_basimyili.date().year()
        publish_num = self.addbookform.lineEdit_baskisayisi.text()
        publisher = self.addbookform.lineEdit_yayinevi.text()
        about_book = self.addbookform.textEdit_kitaphk.toPlainText()
        about_author = self.addbookform.textEdit_yazarhk.toPlainText()

        with sqlite3.connect("kitap.db") as vt:
            im = vt.cursor()
            im.execute("""INSERT INTO kitap(kitap_adi,Turu,Yazar,Dil,Cevirmen,BasimYili,BaskiSayisi,Yayinevi,
            KtpHk,YzrHk) VALUES (?,?,?,?,?,?,?,?,?,?)""", (book_name, gender, author, language, interpreter, publish_year,
                                                           publish_num, publisher, about_book, about_author,))
            vt.commit()
            self.addbookform.statusbar.showMessage("KAYIT EKLEME BAŞARILI", 5000)
            self.listele()

    def temizle(self):
        self.addbookform.lineEdit_kitabinadi.clear()
        self.addbookform.comboBox_kitabinturu.clear()
        self.addbookform.lineEdit_yazar.clear()
        self.addbookform.lineEdit_dili.clear()
        self.addbookform.lineEdit_cevirmen.clear()
        self.addbookform.dateEdit_basimyili.clear()
        self.addbookform.lineEdit_baskisayisi.clear()
        self.addbookform.lineEdit_yayinevi.clear()
        self.addbookform.textEdit_kitaphk.clear()
        self.addbookform.textEdit_yazarhk.clear()

    def listele(self):
        self.addbookform.tableWidget.setHorizontalHeaderLabels(('Kayıt No', 'Kitap Adı', 'Türü', 'Yazarı',
                                                               'Orjinal Dili','Cevirmeni', 'Basım Yılı', 'Baskı Sayısı',
                                                               'Yayın Evi','Kitap Hakkında', 'Yazar Hakkında'))
        self.addbookform.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        with sqlite3.connect("kitap.db") as vt:
            im = vt.cursor()
            im.execute("SELECT * FROM kitap")

            for indexSatir, kayitNumarasi in enumerate(im):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    self.addbookform.tableWidget.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

            self.addbookform.lineEdit_kitabinadi.clear()
            self.addbookform.comboBox_kitabinturu.setCurrentIndex(-1)
            self.addbookform.lineEdit_yazar.clear()
            self.addbookform.lineEdit_dili.clear()
            self.addbookform.lineEdit_cevirmen.clear()
            self.addbookform.dateEdit_basimyili.setCurrentSection(-1)
            self.addbookform.lineEdit_baskisayisi.clear()
            self.addbookform.lineEdit_yayinevi.clear()
            self.addbookform.textEdit_kitaphk.clear()
            self.addbookform.textEdit_yazarhk.clear()

            im.execute("SELECT COUNT(*) FROM kitap")
            kayitSayisi = im.fetchone()
            self.addbookform.label_kytsayisi.setText(str(kayitSayisi[0]))

    def Doldur(self):
        secili = self.addbookform.tableWidget.selectedItems()
        self.addbookform.lineEdit_kitabinadi.setText(secili[1].text())
        self.addbookform.comboBox_kitabinturu.setCurrentText(secili[2].text())
        self.addbookform.lineEdit_yazar.setText(secili[3].text())
        self.addbookform.lineEdit_dili.setText(secili[4].text())
        self.addbookform.lineEdit_cevirmen.setText(secili[5].text())
        self.addbookform.dateEdit_basimyili.setDate(QtCore.QDate.fromString(secili[6].text(), 'yyyy'))
        self.addbookform.lineEdit_baskisayisi.setText(secili[7].text())
        self.addbookform.lineEdit_yayinevi.setText(secili[8].text())
        self.addbookform.textEdit_kitaphk.setPlainText(secili[9].text())
        self.addbookform.textEdit_yazarhk.setPlainText(secili[10].text())

    def arama(self):
        self.temizle()
        book_name = self.addbookform.lineEdit_ara.text()
        gender = self.addbookform.lineEdit_ara.text()
        author = self.addbookform.lineEdit_ara.text()
        publisher = self.addbookform.lineEdit_ara.text()

        with sqlite3.connect("kitap.db") as vt:
            im = vt.cursor()
            im.execute("""SELECT * FROM kitap WHERE kitap_adi=? or Turu=? or Yazar=? or Yayinevi=?""",
                       (book_name, gender, author, publisher,))
            self.addbookform.tableWidget.clear()
            self.addbookform.tableWidget.setHorizontalHeaderLabels(('Kayıt No', 'Kitap Adı', 'Türü', 'Yazarı',
                                                                    'Orjinal Dili','Cevirmeni', 'Basım Yılı',
                                                                    'Baskı Sayısı', 'Yayın Evi','Kitap Hakkında',
                                                                    'Yazar Hakkında'))
            self.addbookform.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            for indexSatir, kayitNumarasi in enumerate(im):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    self.addbookform.tableWidget.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
        self.addbookform.lineEdit_ara.clear()

    def Guncelle(self):
        mesaj = QMessageBox.question(self, "GÜNCELLEME ONAYI", "Güncellemek İstediğinizden Eminmisiniz?",
                                     QMessageBox.Yes | QMessageBox.No)
        if mesaj == QMessageBox.Yes:
            try:
                secilen_kayit = self.addbookform.tableWidget.selectedItems()
                secili_id = int(secilen_kayit[0].text())
                book_name = self.addbookform.lineEdit_kitabinadi.text()
                gender = self.addbookform.comboBox_kitabinturu.currentText()
                author = self.addbookform.lineEdit_yazar.text()
                language = self.addbookform.lineEdit_dili.text()
                interpreter = self.addbookform.lineEdit_cevirmen.text()
                publish_year = self.addbookform.dateEdit_basimyili.date().year()
                publish_num = self.addbookform.lineEdit_baskisayisi.text()
                publisher = self.addbookform.lineEdit_yayinevi.text()
                about_book = self.addbookform.textEdit_kitaphk.toPlainText()
                about_author = self.addbookform.textEdit_yazarhk.toPlainText()

                with sqlite3.connect("kitap.db") as vt:
                    im = vt.cursor()
                    im.execute("""UPDATE kitap SET kitap_adi=?,Turu=?,Yazar=?,Dil=?,Cevirmen=?,BasimYili=?,
                       BaskiSayisi=?,Yayinevi=?,KtpHk=?,YzrHk=? WHERE kitapid=?""",
                                (book_name, gender, author, language, interpreter, publish_year, publish_num,
                                 publisher, about_book, about_author, secili_id))
                    vt.commit()
                    self.listele()
            except sqlite3.Error as e:
                self.addbookform.statusbar.showMessage(f"KAYIT GÜNCELLEME HATASI: {e}", 5000)
        else:
            pass

    def sil(self):
        mesaj = QMessageBox.warning(self, "SİLME ONAYI", "Silmek İstediğinizden Eminmisiniz?",
                                     QMessageBox.Yes | QMessageBox.No)
        if mesaj == QMessageBox.Yes:
            try:
                secilen_kayit = self.addbookform.tableWidget.selectedItems()
                secili_id = int(secilen_kayit[0].text())

                with sqlite3.connect("kitap.db") as vt:
                    im = vt.cursor()
                    im.execute("""DELETE FROM kitap WHERE kitapid=?""", (secili_id,))
                    vt.commit()
                    self.listele()
                    self.addbookform.statusbar.showMessage("KAYIT SİLİNDİ", 5000)
            except sqlite3.Error as e:
                self.addbookform.statusbar.showMessage(f"KAYIT SİLME HATASI: {e}", 5000)
        else:
            pass

    def Hakkinda(self):
        self.hakkindaform.show()

    def cikis(self):
        sys.exit()

















