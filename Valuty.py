import json

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from datetime import date


def change_valuta_window():
    window = QDialog()
    window.resize(100, 100)
    window.setStyleSheet("""     
    QWidget {
        background-color: rgba(204, 255, 229, .9);    
    }
        
     QPushButton {        
        background: #e9edf2;
        border-style: outset;        
        min-height: 30px;
        min-width: 100px;     }
        
     QListWidget {         
     background: #ccdbd5;
     }
          QTextEdit { 
        background: #e1ede8;     }
        
      QPushButton {
        color: red;        
        font-size: 10px;
        font-family: Impact;        
        border-width: 2px;
        border-color: red;        
        border-radius: 5px;
     }
      QLabel {
        color: ;        
        font-size: 20px;
        font-family: Impact;        
        border-width: 2px;
        border-color: red;        
        border-radius: 5px;
     }
      
 """)

    valuti = QLabel("ВАЛЮТИ")
    date = QLabel("ДАТА (приклад: 12022024)")
    lineEdit = QDateEdit()
    valyuty = QLabel("ВИБІР ВАЛЮТИ (приклад: PLN")
    lineEdit2 = QLineEdit()
    konvert = QPushButton("КОНВЕРТ")
    lineEdit3 = QLineEdit()
    lineEdit4 = QLineEdit()
    qwerty = QLabel("В ЯКУ:")
    lineEdit5 = QLineEdit()




    skin111 = QLabel("Kartina")
    skin111_img = QPixmap("pngegg.png")
    skin111_img = skin111_img.scaledToWidth(20)
    skin111.setPixmap(skin111_img)

    skin2 = QLabel("Kartina")
    skin2_img = QPixmap("free-icon-currency-exchange-2722070.png")
    skin2_img = skin2_img.scaledToWidth(50)
    skin2.setPixmap(skin2_img)

    skin3 = QLabel("Kartina")
    skin3_img = QPixmap("klipartz.com.png")
    skin3_img = skin3_img.scaledToWidth(50)
    skin3.setPixmap(skin3_img)

    Liniya = QVBoxLayout()

    Liniya2 = QHBoxLayout()

    Liniya2.addWidget(skin2)
    Liniya2.addWidget(valuti)
    Liniya2.addWidget(skin3)

    Liniya3 = QHBoxLayout()
    Liniya3.addWidget(date)
    Liniya3.addWidget(lineEdit)


    Liniya4 = QHBoxLayout()
    Liniya4.addWidget(valyuty)
    Liniya4.addWidget(lineEdit2)
    Liniya4.addWidget(qwerty)
    Liniya4.addWidget(lineEdit5)

    Liniya5 = QHBoxLayout()

    Liniya5.addWidget(lineEdit3)
    Liniya5.addWidget(skin111)
    Liniya5.addWidget(lineEdit4)

    Liniya6 = QHBoxLayout()

    Liniya6.addWidget(konvert)

    Liniya.addLayout(Liniya2)
    Liniya.addLayout(Liniya3)
    Liniya.addLayout(Liniya4)
    Liniya.addLayout(Liniya5)
    Liniya.addLayout(Liniya6)
    window.setLayout(Liniya)



    def obmin_valut():
        date = lineEdit.date().toString("yyyyMMdd")
        a = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json&date={date}")
        if a.status_code == 200:
            date = lineEdit.text()
            data = a.json()
            from_currency = lineEdit5.text()
            to_currency = lineEdit2.text()
            amount = float(lineEdit3.text())

            if from_currency == 'UAH':
                from_rate = 1
            else:
                from_rate = next(item for item in data if item["cc"] == from_currency)["rate"]

            if to_currency == 'UAH':
                from_rate = 1
            else:
                to_rate = next(item for item in data if item["cc"] == to_currency)["rate"]


            result = amount / from_rate * to_rate


            lineEdit4.setText(str(result))

    konvert.clicked.connect(obmin_valut)
    window.show()
    window.exec()