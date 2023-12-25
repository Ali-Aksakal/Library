from PyQt5.QtWidgets import QApplication
from welcome import Welcome


app = QApplication([])
window = Welcome()
window.show()
app.exec_()