from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox, QTableWidget
from PyQt6.QtGui import QIcon, QFont, QPixmap
from Client import Client
from pathlib import Path

import sys


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None

        self.setWindowTitle("Ozon-Stocks")
        self.setWindowIcon(QIcon("images/1c_ozon.jpg"))

        self.start = QPushButton(self)
        self.about_us = QPushButton(self)
        self.end = QPushButton(self)

        self.widget = QLabel(self)
        self.widget.setPixmap(QPixmap("images/1c_ozon.jpg"))
        self.widget.setScaledContents(True)
        self.widget.move(480, 50)
        self.widget.resize(QPixmap("images/1c_ozon.jpg").width() - 100, QPixmap("images/1c_ozon.jpg").height() - 100)

        self.start.setText("Начать")
        self.about_us.setText("О нас")
        self.end.setText("Закрыть")

        self.start.clicked.connect(self.start_button)
        self.about_us.clicked.connect(self.about_us_button)
        self.end.clicked.connect(self.end_button)

        self.start.move(700, 650)
        self.about_us.move(700, 700)
        self.end.move(1430, 5)

    def start_button(self):
        print('Pressed Start')
        self.w = SignUp()
        self.w.showMaximized()
        self.close()

    def about_us_button(self):
        print("Pressed Us")
        self.w = AboutUs()
        self.w.show()

    def end_button(self):
        print("End")
        self.close()


# noinspection PyUnresolvedReferences
class SignUp(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None

        self.setWindowTitle("Ozon-Stocks")

        self.text_label1 = QLabel(self)
        self.text_label1.move(10, 25)
        self.text_label1.setText("Введите данные")
        self.text_label1.setFont(QFont('Arial', 30))

        self.client_id_label = QLabel(self)
        self.client_id_label.move(10, 105)
        self.client_id_label.setText("Введите Client Id:")
        self.client_id_label.setFont(QFont('Arial', 30))

        self.client_id_edit = QLineEdit(self)
        self.client_id_edit.move(380, 105)
        self.client_id_edit.setFont(QFont('Arial', 25))

        self.api_key_label = QLabel(self)
        self.api_key_label.move(10, 260)
        self.api_key_label.setText("Введите Api Key:")
        self.api_key_label.setFont(QFont('Arial', 30))

        self.api_key_edit = QLineEdit(self)
        self.api_key_edit.move(380, 260)
        self.api_key_edit.setFont(QFont('Arial', 25))

        self.send = QPushButton(self)
        self.send.setText("Отправить")
        self.send.setFont(QFont('Arial', 25))
        self.send.move(520, 400)
        self.send.clicked.connect(self.send_button)

    # Написать проверку данных
    def send_button(self):
        client = Client(self.client_id_edit.text(), self.api_key_edit.text())
        print(self.client_id_edit.text())
        print(self.api_key_edit.text())
        response = client.connect()
        # Идиотская ошибка, озон уроды
        if response.status_code == 200 or response.status_code == 404:
            print("Connected, code =", response.status_code)
            information = QMessageBox.information(self, "Принято", "Данные корректны")

            if information == QMessageBox.StandardButton.Ok:
                print("Ok!")
            else:
                print("No!")

            self.w = Options(client)
            self.w.showMaximized()

            self.close()

        else:
            print("Didn't connect, code =", response.status_code)
            s = "Ошибка " + str(response.status_code)
            information = QMessageBox.information(self, "Ошибка", s)

            if information == QMessageBox.StandardButton.Ok:
                print("Ok!")
            else:
                print("No!")


# noinspection PyUnresolvedReferences
class Options(QWidget):
    def __init__(self, client):
        super().__init__()
        self.w = None
        self.client = client

        self.setWindowTitle("Ozon-Stocks")

        self.choice_label = QLabel(self)
        self.choice_label.move(5, 5)
        self.choice_label.setText("Выберите опцию")
        self.choice_label.setFont(QFont('Arial', 20))

        self.start = QPushButton(self)
        self.back = QPushButton(self)

        self.start.setText("Обновить остатки")
        self.start.setFont(QFont('Arial', 15))
        self.back.setText("Назад")
        self.back.setFont(QFont('Arial', 15))

        self.start.move(10, 60)
        self.back.move(10, 700)

        self.start.clicked.connect(self.start_button)
        self.back.clicked.connect(self.back_button)

    def start_button(self):
        self.w = GetData(self.client)
        self.w.showMaximized()

        self.close()

    def back_button(self):
        self.w = SignUp()
        self.w.showMaximized()

        self.close()


class GetData(QWidget):
    def __init__(self, client):
        super().__init__()
        self.w = None

        self.client = client

        self.path_ozon_label = QLabel(self)
        self.path_1c_label = QLabel(self)
        self.path_exception_label = QLabel(self)

        self.path_ozon_label.setText("Напишите путь до файла со всеми товарами в платформе Ozon")
        self.path_ozon_label.setFont(QFont('Arial', 20))
        self.path_1c_label.setText("Напишите путь до файла со всеми товарами в платформе 1C")
        self.path_1c_label.setFont(QFont('Arial', 20))
        self.path_exception_label.setText("Напишите путь до файла со всеми товарами, которые не надо изменять")
        self.path_exception_label.setFont(QFont('Arial', 20))

        self.path_ozon = QLineEdit(self)
        self.path_ozon.setFont(QFont('Arial', 20))

        self.path_1c = QLineEdit(self)
        self.path_1c.setFont(QFont('Arial', 20))

        self.path_exception = QLineEdit(self)
        self.path_exception.setFont(QFont('Arial', 20))

        self.path_ozon_button = QPushButton(self)
        self.path_ozon_button.setText("Выберите")
        self.path_ozon_button.setFont(QFont('Arial', 20))

        self.path_1c_button = QPushButton(self)
        self.path_1c_button.setText("Выберите")
        self.path_1c_button.setFont(QFont('Arial', 20))

        self.path_exception_button = QPushButton(self)
        self.path_exception_button.setText("Выберите")
        self.path_exception_button.setFont(QFont('Arial', 20))

        self.next = QPushButton(self)
        self.next.setText("Продолжить")
        self.next.setFont(QFont('Arial', 20))

        self.next.move(15, 700)

        self.path_ozon_label.move(10, 10)
        self.path_ozon.move(15, 70)
        self.path_ozon_button.move(300, 70)

        self.path_1c_label.move(10, 130)
        self.path_1c.move(15, 190)
        self.path_1c_button.move(300, 190)

        self.path_exception_label.move(10, 250)
        self.path_exception.move(15, 310)
        self.path_exception_button.move(300, 310)

        self.path_ozon_button.clicked.connect(self.showDialog_ozon)
        self.path_1c_button.clicked.connect(self.showDialog_1c)
        self.path_exception_button.clicked.connect(self.showDialog_exception)
        self.next.clicked.connect(self.next_func)

    def showDialog_ozon(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            self.path_ozon.setText(fname[0])
            self.client.set_path_ozon(fname[0])

    def showDialog_1c(self):
        home_dir = str(Path.home())
        filename = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if filename[0]:
            self.path_1c.setText(filename[0])
            self.client.set_path_1c(filename[0])

    def showDialog_exception(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            self.path_exception.setText(fname[0])
            self.client.set_path_exception(fname[0])

    def next_func(self):
        if self.client.path_ozon and self.path_1c:
            self.w = UpdateStocks(self.client)
            self.w.showMaximized()

            self.close()
        else:
            s = "Вы не ввели все данные"
            information = QMessageBox.information(self, "Ошибка", s)

            if information == QMessageBox.StandardButton.Ok:
                print("Ok!")
            else:
                print("No!")


class UpdateStocks(QWidget):
    def __init__(self, client):
        super().__init__()
        self.client = client

        self.notice = QLabel(self)
        self.notice.setText("Напишите кол-во остатков для всех товаров")
        self.notice.setFont(QFont('Arial', 20))
        self.notice.move(10, 10)

        self.count = QLineEdit(self)
        self.count.setFont(QFont('Arial', 20))
        self.count.move(15, 70)

        self.start = QPushButton(self)
        self.start.setText("Начать")
        self.start.setFont(QFont('Arial', 20))
        self.start.move(25, 130)

        self.result_label = QLabel(self)
        self.result_label.setText("Результат")
        self.result_label.setFont(QFont('Arial', 20))
        self.result_label.move(20, 190)

        self.table = QTableWidget(self)
        self.table.move(15, 240)
        self.table.resize(800, 500)

        self.start.clicked.connect(self.start_button)

    def start_button(self):
        information = self.client.start_work()


# noinspection PyUnresolvedReferences
class AboutUs(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle("Ozon-Stocks")

        self.inf_label = QLabel(self)
        self.inf_label.setText("Здесь должна быть информация он нас.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cl = Client('', '')
    ex = MainWindow()
    ex.showMaximized()
    sys.exit(app.exec())
