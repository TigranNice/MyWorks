import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QComboBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

import sqlite3

#создание основного окна
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 500, 500, 400)
        self.setWindowTitle('Интернет магазин - MegaAvto')

        self.label = QLabel(self)
        self.label.setText('''
Здравствуйте, вас приветствует MegaAvto,
лучший рынок для покупки и продажи машины.

Здесь вы можете любую машину на ваш вкус
или же продать ваш старый автомобиль''')
        self.label.move(80, 30)

        self.label2 = QLabel(self)
        self.label2.setText('''Выберите одну из кнопок, чтобы перейти на нужную страницу''')
        self.label2.move(80, 200)

        self.btn1 = QPushButton('Продажа', self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.move(100, 250)
        self.btn1.clicked.connect(self.prodazha)
        
        self.btn2 = QPushButton('Покупка', self)
        self.btn2.resize(self.btn2.sizeHint())
        self.btn2.move(300, 250)
        self.btn2.clicked.connect(self.pokupka)

    def prodazha(self):
        self.prodazha = InfoSeller(self)
        self.prodazha.show()

            
    def pokupka(self):
        self.pokupka = PokupkaMachine(self)
        self.pokupka.show()

#взятие контактных данных у пользователя
class InfoSeller(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("Pokupka1.ui", self)
        self.pushButton.clicked.connect(self.prod)
        self.modified = {}
        self.titles = None

    def prod(self):
        seller = self.lineEdit.text()
        location = self.lineEdit_2.text()
        telephone = self.lineEdit_3.text()
        
        if not seller or not location or not telephone:
            self.letter2 = Letter2(self)
            self.letter2.show()
        else:
            con = sqlite3.connect('MegaAvtoBase.db')
            cur = con.cursor()
            global tup
            prod = '''INSERT INTO cars(seller, location, telephone)
                        VALUES(?, ?, ?)'''
            tup = (seller, location, telephone)
            cur.execute(prod, tup)
            print(tup)
            
            con.commit()
            con.close()
            
            self.letter1 = ProdazhaMachine(self)
            self.letter1.show()
        

#взятие данных об автомобиле        
class ProdazhaMachine(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Продажа')

        self.label3 = QLabel(self)
        self.label3.setText('Введите данные вашего автомобиля')
        self.label3.move(30, 30)

        self.label31 = QLabel(self)
        self.label31.setText('Марка')
        self.label31.move(20, 90)

        self.inf1 = QLineEdit(self)
        self.inf1.move(120, 90)
        self.inf1.resize(220, 25)
        
        self.label32 = QLabel(self)
        self.label32.setText('Модель')
        self.label32.move(20, 140)

        self.inf2 = QLineEdit(self)
        self.inf2.move(120, 140)
        self.inf2.resize(220, 25)

        self.label33 = QLabel(self)
        self.label33.setText('Цвет')
        self.label33.move(20, 190)
        
        self.inf3 = QLineEdit(self)
        self.inf3.move(120, 190)
        self.inf3.resize(220, 25)

        self.label34 = QLabel(self)
        self.label34.setText('Дата сборки')
        self.label34.move(20, 240)

        self.inf4 = QLineEdit(self)
        self.inf4.move(120, 240)
        self.inf4.resize(220, 25)

        self.label35 = QLabel(self)
        self.label35.setText('Стоимость')
        self.label35.move(20, 290)

        self.inf5 = QLineEdit(self)
        self.inf5.move(120, 290)
        self.inf5.resize(220, 25)

        self.let = QPushButton('Отправить заявку', self)
        self.let.resize(self.let.sizeHint())
        self.let.move(150, 340)
        self.let.clicked.connect(self.letter)

    def letter(self):
        global tup
        print(tup)
        mark = self.inf1.text()
        model = self.inf2.text()
        colour = self.inf3.text()
        data = self.inf4.text()
        cost = self.inf5.text()
        #проверка на наличие всех аргументов
        if not mark or not model or not colour or not data or not cost:
            self.letter2 = Letter2(self)
            self.letter2.show()
        else:
            con = sqlite3.connect('MegaAvtoBase.db')
            cur = con.cursor()
            idl = cur.execute('SELECT id FROM cars WHERE seller=? and location=? and telephone=?',
                              (item_seller := tup[0], item_location := tup[1], item_telephone := tup[2])).fetchall()
            idl = list(idl[0])
            prod = '''INSERT INTO maintable1(id, mark, model, colour, data, cost)
                        VALUES(?, ?, ?, ?, ?, ?)'''
            tup = (idl[0], mark, model, colour, data, cost)
            cur.execute(prod, tup)
            con.commit()
            con.close()
            
            self.end = End(self)
            self.end.show()

#окно всплывающее при отсутствии одного из аргументов
class Letter2(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(150, 300, 300, 150)
        self.setWindowTitle('MegaAvto')
        
        self.lab = QLabel(self)
        self.lab.setText('''Пожалуйста, введите все данные
(для продолжения работы закройте окно)''')
        self.lab.move(20, 50)

#выбор автомобиля
class PokupkaMachine(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("TablEofMegaAvto.ui", self)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.modified = {}
        self.titles = None
        
        con = sqlite3.connect('MegaAvtoBase.db')
        cur = con.cursor()
        mark = cur.execute('SELECT DISTINCT mark FROM maintable1').fetchall()
        con.commit()
        con.close()
        markf = []
        for i in range(len(mark)):
            markf.append(mark[i][0])
        self.comboBox.addItems(markf)
        self.comboBox.activated[str].connect(self.model)
        self.comboBox_2.activated[str].connect(self.colour)
        self.comboBox_3.activated[str].connect(self.update_result)
        
        self.pushButton.clicked.connect(self.cont)

    def model(self, text):
        global markf
        markf = text
        
        con = sqlite3.connect('MegaAvtoBase.db')
        cur = con.cursor()
        model = cur.execute('SELECT DISTINCT model FROM maintable1 WHERE mark=:text', {'text': text}).fetchall()
        con.commit()
        con.close()

        modelf = []
        for i in range(len(model)):
            modelf.append(model[i][0])
        
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.comboBox_2.addItems(modelf)

    def colour(self, text):
        global modelf
        modelf = text
        
        con = sqlite3.connect('MegaAvtoBase.db')
        cur = con.cursor()
        colour = cur.execute('SELECT DISTINCT colour FROM maintable1 WHERE model=:text', {'text': text}).fetchall()
        con.commit()
        con.close()

        colourf = []
        for i in range(len(colour)):
            colourf.append(colour[i][0])
        
        self.comboBox_3.clear()
        self.comboBox_3.addItems(colourf)
    #создание таблицы
    def update_result(self, text):
        global markf, modelf, colourf
        colourf = text
        con = sqlite3.connect('MegaAvtoBase.db')
        cur = con.cursor()

        result = cur.execute("SELECT * FROM maintable1 WHERE mark=? and model=? and colour=?",
                             (item_mark := markf, item_model := modelf, item_colour := colourf)).fetchall()

        self.tableWidget.setRowCount(len(result))        
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def cont(self):
        global markf, modelf, colourf
        con = sqlite3.connect('MegaAvtoBase.db')
        cur = con.cursor()
        result1 = cur.execute("SELECT id FROM maintable1 WHERE mark=? and model=? and colour=?",
                              (item_mark := markf, item_model := modelf, item_colour := colourf)).fetchall()
        self.cont = Cont(self, result1)
        self.cont.show()

#вывод данных про контакты продавца автомобиля
class Cont(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("InfoSel.ui", self)
        self.tableWidget.itemChanged.connect(self.item_changed)
        con = sqlite3.connect("MegaAvtoBase.db")
        cur = con.cursor()
        self.modified = {}
        self.titles = None
        result3 = args[-1]
        result = []
        for i in result3:
            res = cur.execute("SELECT * FROM cars WHERE id=?",
                              (item_id := i)).fetchall()
            result.append(res[0])
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}
        self.pushButton.clicked.connect(self.end)

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def end(self):
        self.end = End(self)
        self.end.show()

#конченое окно, сплывающее после покупки или продажи автомобиля
class End(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("end.ui", self)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
