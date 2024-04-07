import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


cryptocurrency = {
    "BTC":65636.77,
    "ETH":3400.78,
    "SOL":176.933,
    "DOGE":0.173339,
    "TON":4.9549,
    "KAVA":0.9182
}

def change_kvaluta_window():

    window = QDialog()
    window.resize(100, 100)

    valuti = QLabel("КРИПТОВАЛЮТИ")
    valyuty = QLabel("ВИБІР ВАЛЮТИ (приклад: BTH")
    lineEdit2 = QLineEdit()
    konvert = QPushButton("КОНВЕРТ")
    lineEdit3 = QLineEdit()
    lineEdit4 = QLineEdit()
    qwerty = QLabel("В ЯКУ:")
    lineEdit5 = QLineEdit()

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

    skin111 = QLabel("Kartina")
    skin111_img = QPixmap("pngegg.png")
    skin111_img = skin111_img.scaledToWidth(20)
    skin111.setPixmap(skin111_img)

    skin2 = QLabel("Kartina")
    skin2_img = QPixmap("pngwing.com (11).png")
    skin2_img = skin2_img.scaledToWidth(50)
    skin2.setPixmap(skin2_img)

    skin3 = QLabel("Kartina")
    skin3_img = QPixmap("pngwing.com (12).png")
    skin3_img = skin3_img.scaledToWidth(50)
    skin3.setPixmap(skin3_img)

    Liniya = QVBoxLayout()

    Liniya2 = QHBoxLayout()

    Liniya2.addWidget(skin2)
    Liniya2.addWidget(valuti)
    Liniya2.addWidget(skin3)

    Liniya3 = QHBoxLayout()



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
        input_currency = lineEdit2.text().upper()
        output_currency = lineEdit5.text().upper()
        kilkict = lineEdit3.text().upper()
        if input_currency in cryptocurrency and output_currency  in cryptocurrency:
            a = cryptocurrency[input_currency]
            b = cryptocurrency[output_currency]


            converted_amount = a * int(kilkict)/b
            lineEdit4.setText(str(converted_amount))

    konvert.clicked.connect(obmin_valut)

    window.show()
    window.exec()