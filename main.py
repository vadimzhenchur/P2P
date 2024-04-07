import json

from PyQt5.QtWidgets import *

from Kvaluty import change_kvaluta_window
from Valuty import change_valuta_window

app =  QApplication([])



window = QWidget()
window.resize(100, 100)

app.setStyleSheet("""     QWidget {
        background: #fcd5fb;     }
     QPushButton {        background: #e9edf2;
        border-style: outset;        min-height: 30px;
        min-width: 100px;     }
     QListWidget {         background: #ccdbd5;
     }     QTextEdit { 
        background: #e1ede8;     }
      QPushButton {
        color: #14d5fb;        font-size: 15px;
        font-family: Impact;        border-width: 2px;
        border-color: red;        border-radius: 5px;
     }
      QLabel {
        color: #79d5fb;        font-size: 100px;
        font-family: Impact;        border-width: 2px;
        border-color: red;        border-radius: 5px;
     }
      
 """)

ObminKruptu = QPushButton("ОБМІНЯТИ КРИПТО-ВАЛЮТУ")
Pitannya = QLabel("ВАЛЮТИ")

ObminValut = QPushButton("ОБМІНЯТИ ВАЛЮТУ")


Liniya = QVBoxLayout()

Liniya.addWidget(Pitannya)

Liniya2 = QHBoxLayout()
Liniya2.addWidget(ObminKruptu)
Liniya2.addWidget(ObminValut)
ObminValut.clicked.connect(change_valuta_window)
ObminKruptu.clicked.connect(change_kvaluta_window)
Liniya.addLayout(Liniya2)

window.setLayout(Liniya)


window.show()
app.exec()