import pygame, itertools
from yerrow import Rotate_blue_tank
from yerrow2 import Rotate_red_tank
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QComboBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox


class Enter(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("TankiEnter1.ui", self)

        self.pushButton.clicked.connect(self.customize)
        self.pushButton_3.clicked.connect(self.tutorial)

    def customize(self):
        self.close()
        self.cust = Customize(self)
        self.cust.show()

    def tutorial(self):
        self.close()
        self.tut = Tutorial(self)
        self.tut.show()



class Customize(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("TankiCustomize.ui", self)

        self.blue_player = 0
        self.red_player = 0
        #выбор танка
        self.pushButton.clicked.connect(self.player11)
        self.pushButton_2.clicked.connect(self.player12)
        self.pushButton_3.clicked.connect(self.player13)
        self.pushButton_9.clicked.connect(self.player21)
        self.pushButton_8.clicked.connect(self.player22)
        self.pushButton_7.clicked.connect(self.player23)
        
        self.pushButton_4.clicked.connect(self.play)
        self.pushButton_5.clicked.connect(self.enter)

    def enter(self):
        self.close()
        self.ent = Enter()
        self.ent.show()

    def player11(self):
        self.blue_player = 1

    def player12(self):
        self.blue_player = 2

    def player13(self):
        self.blue_player = 3

    def player21(self):
        self.red_player = 1

    def player22(self):
        self.red_player = 2

    def player23(self):
        self.red_player = 3

    def play(self):
        if self.blue_player != 0 and self.red_player != 0:
            self.close()
            self.pl = Play(self, self.blue_player, self.red_player)
            self.pl.show()
        elif self.blue_player != 0 and self.red_player == 0:
            self.setGeometry(422, 83, 1075, 863)
            buttonReply = QMessageBox.information(self, "Ошибка", "Вы не выбрали танк для красной команды!")
        elif self.blue_player == 0 and self.red_player != 0:
            self.setGeometry(422, 83, 1075, 863)
            buttonReply = QMessageBox.information(self, "Ошибка", "Вы не выбрали танк для синей команды!")            
        else:
            self.setGeometry(422, 83, 1075, 863)
            buttonReply = QMessageBox.information(self, "Ошибка", "Вы не выбрали танки для обоих команд!")
                
        


class Tutorial(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("TankiTutorial.ui", self)
        self.pushButton.clicked.connect(self.enter)

    def enter(self):
        self.close()
        self.ent = Enter()
        self.ent.show()
        


class Play(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi("TankiMaps.ui", self)
        #закрытие
        self.pushButton_5.clicked.connect(self.enter)
        #выбор карт
        self.pushButton_2.clicked.connect(self.city)
        self.pushButton_3.clicked.connect(self.desert)
        self.pushButton_4.clicked.connect(self.winter)
        #пуск
        self.pushButton.clicked.connect(self.start)
        
        self.blue_player = args[1]
        self.red_player = args[2]
        self.map = 0

    def enter(self):
        self.close()
        self.cust = Customize()
        self.cust.show()

    def city(self):
        self.map = 1

    def desert(self):
        self.map = 2

    def winter(self):
        self.map = 3
#сама игра
    def start(self):
        if self.map != 0:
            self.close()
            pygame.init()
            MAX_Y = 1000
            MAX_X = 1000
            screen = pygame.display.set_mode((MAX_X, MAX_Y))

            move_red1_down = False
            move_red1_up = False
            move_red1_left = False
            move_red1_right = False

            move_red2_down = False
            move_red2_up = False
            move_red2_left = False
            move_red2_right = False

            move_red3_left = False
            move_red3_right = False
            move_red3_down = False
            move_red3_up = False

            move_blue1_a = False
            move_blue1_d = False
            move_blue1_s = False
            move_blue1_w = False

            move_blue2_s = False
            move_blue2_w = False
            move_blue2_a = False
            move_blue2_d = False

            move_blue3_s = False
            move_blue3_w = False
            move_blue3_a = False
            move_blue3_d = False

            blue_player = self.blue_player
            red_player = self.red_player

            FPS = 2000
            clock = pygame.time.Clock()
            x, y = 0, 0
            x2, y2 = 1, 1

            redx1 = 920
            redy1 = 900

            redx2 = 920
            redy2 = 900

            redx3 = 920
            redy3 = 900

            bluex1 = -10
            bluey1 = 0

            bluex2 = -10
            bluey2 = 0

            bluex3 = -10
            bluey3 = 0

            if blue_player == 1:  # ----------легкий
                blue1 = pygame.image.load('blue_fast.png')
                complete_blue_tank_rotating = Rotate_blue_tank(blue1, bluex1, bluey1, '1')

            if blue_player == 2:  # ----------тяжелый
                blue2 = pygame.image.load('uuu.png')
                complete_blue_tank_rotating = Rotate_blue_tank(blue2, bluex2, bluey2, '2')

            if blue_player == 3:  # ------------мощный
                blue3 = pygame.image.load('rrr.png')
                complete_blue_tank_rotating = Rotate_blue_tank(blue3, bluex3, bluey3, '3')

            if red_player == 1:  # ---------легкий
                red1 = pygame.image.load('jiji.png')
                complete_red_tank_rotating = Rotate_red_tank(red1, redx1, redy1, '1')

            if red_player == 2:  # ---------тяжелый
                red2 = pygame.image.load('fat_red.png')
                complete_red_tank_rotating = Rotate_red_tank(red2, redx2, redy2, '2')

            if red_player == 3:  # ----------мощный
                red3 = pygame.image.load('strong_red.png')
                complete_red_tank_rotating = Rotate_red_tank(red3, redx3, redy3, '3')
            running = False
            dream = True
            state = True
            pause_text = pygame.font.SysFont('Consolas', 64).render('Pause', True, pygame.color.Color('Red'))
            while dream:
                if self.map == 1:
                    screen.fill((139, 159, 161))
                    
                    pygame.draw.rect(screen, (208, 208, 205), (1, 301, 58, 58))
            
                    pygame.draw.rect(screen, (208, 208, 205), (61, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (61, 241, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (61, 181, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (61, 121, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (61, 361, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (61, 421, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (61, 481, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (61, 541, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (61, 601, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (61, 661, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (121, 661, 58, 58))
                    
                    pygame.draw.rect(screen, (208, 208, 205), (121, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (181, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (241, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (301, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (361, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (421, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (481, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (541, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (541, 361, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (541, 421, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (541, 481, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (541, 541, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (481, 541, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (601, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (661, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (721, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (721, 241, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (781, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (781, 241, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (841, 301, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (841, 361, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (841, 421, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (841, 481, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (841, 541, 58, 58))
                    pygame.draw.rect(screen, (208, 208, 205), (901, 301, 58, 58))

                    pygame.draw.circle(screen, (0, 200, 64), (260, 149), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (280, 149), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (260, 133), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (280, 133), 13)
                    pygame.draw.line(screen, (90, 4, 18), (270, 157), (270, 180), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (140, 389), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (160, 389), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (140, 373), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (160, 373), 13)
                    pygame.draw.line(screen, (90, 4, 18), (150, 397), (150, 420), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (680, 389), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (700, 389), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (680, 373), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (700, 373), 13)
                    pygame.draw.line(screen, (90, 4, 18), (690, 397), (690, 420), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (450, 809), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (470, 809), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (450, 793), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (470, 793), 13)
                    pygame.draw.line(screen, (90, 4, 18), (460, 817), (460, 840), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (500, 759), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (520, 759), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (500, 743), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (520, 743), 13)
                    pygame.draw.line(screen, (90, 4, 18), (510, 767), (510, 790), 3)


                    pygame.draw.rect(screen, (0, 255, 255), (75, 30, 30, 90))
                    pygame.draw.polygon(screen, (0, 0, 0), ((75, 30), (90, 0), (105, 30)))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 40, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 60, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 80, 10, 10))

                    pygame.draw.rect(screen, (0, 255, 255), (735, 30, 90, 210))
                    pygame.draw.polygon(screen, (0, 0, 0), ((735, 30), (780, 0), (825, 30)))
                    pygame.draw.rect(screen, (255, 255, 255), (745, 40, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (745, 60, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (745, 80, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (745, 100, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (745, 120, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (745, 140, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (745, 160, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (745, 180, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (745, 200, 10, 10))

                    pygame.draw.rect(screen, (255, 255, 255), (775, 40, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (775, 60, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (775, 80, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (775, 100, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (775, 120, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (775, 140, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (775, 160, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (775, 180, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (775, 200, 10, 10))

                    pygame.draw.rect(screen, (255, 255, 255), (805, 40, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (805, 60, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (805, 80, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (805, 100, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (805, 120, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (805, 140, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (805, 160, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (805, 180, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (805, 200, 10, 10))
                                     
                    pygame.draw.rect(screen, (0, 255, 255), (135, 750, 30, 90))
                    pygame.draw.polygon(screen, (0, 0, 0), ((135, 750), (150, 720), (165, 750)))
                    pygame.draw.rect(screen, (255, 255, 255), (145, 760, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (145, 780, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (145, 800, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (145, 820, 10, 10))

                    pygame.draw.rect(screen, (0, 255, 255), (75, 750, 30, 150))
                    pygame.draw.polygon(screen, (0, 0, 0), ((75, 750), (90, 720), (105, 750)))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 760, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 780, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 800, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 820, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 840, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 860, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 880, 10, 10))

                    pygame.draw.rect(screen, (0, 255, 255), (855, 630, 30, 90))
                    pygame.draw.polygon(screen, (0, 0, 0), ((855, 630), (870, 600), (885, 630)))
                    pygame.draw.rect(screen, (255, 255, 255), (865, 640, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (865, 660, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (865, 680, 10, 10))
                    
                    pygame.draw.rect(screen, (0, 255, 255), (435, 520, 200, 200))
                    pygame.draw.polygon(screen, (0, 0, 0), ((435, 520), (535, 480), (635, 520)))
                    pygame.draw.rect(screen, (255, 255, 255), (445, 580, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (445, 560, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (445, 540, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (445, 600, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (445, 640, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (445, 660, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (445, 680, 10, 10))

                    pygame.draw.rect(screen, (255, 255, 255), (530, 580, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (530, 560, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (530, 540, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (530, 600, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (530, 640, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (530, 660, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (530, 680, 10, 10))

                    pygame.draw.rect(screen, (255, 255, 255), (615, 580, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (615, 560, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (615, 540, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (615, 600, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (615, 640, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (615, 660, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (615, 680, 10, 10))


                    pygame.draw.rect(screen, (0, 255, 255), (315, 460, 90, 200))
                    pygame.draw.polygon(screen, (0, 0, 0), ((315, 460), (360, 420), (405, 460)))
                    pygame.draw.rect(screen, (255, 255, 255), (340, 500, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (340, 480, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (340, 560, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (340, 580, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (340, 600, 10, 10))

                    pygame.draw.rect(screen, (255, 255, 255), (370, 500, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (370, 480, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (370, 560, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (370, 580, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (370, 600, 10, 10))         

                    pygame.draw.rect(screen, (255, 255, 255), (615, 680, 10, 10))

                    pygame.draw.rect(screen, (134, 167, 253), (1, 1, 58, 58))
                    pygame.draw.rect(screen, (253, 134, 138), (901, 901, 58, 58))
                    
                elif self.map == 2:
                    screen.fill((225, 225, 0))
                    pygame.draw.circle(screen, (0, 200, 64), (260, 133), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (280, 133), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (260, 149), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (280, 149), 13)
                    pygame.draw.line(screen, (90, 4, 18), (270, 157), (270, 180), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (140, 373), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (160, 373), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (140, 389), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (160, 389), 13)
                    pygame.draw.line(screen, (90, 4, 18), (150, 397), (150, 420), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (680, 373), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (700, 373), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (680, 389), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (700, 389), 13)
                    pygame.draw.line(screen, (90, 4, 18), (690, 397), (690, 420), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (500, 793), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (520, 793), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (500, 809), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (520, 809), 13)
                    pygame.draw.line(screen, (90, 4, 18), (510, 817), (510, 840), 3)

                    pygame.draw.line(screen, (125, 125, 125), (330, 600), (330, 660), 5)
                    pygame.draw.line(screen, (125, 125, 125), (750, 780), (750, 840), 5)
                    pygame.draw.line(screen, (125, 125, 125), (750, 840), (750, 900), 5)

                    pi = 3.14
                    pygame.draw.arc(screen, (255, 255, 0),
                            (100, 480, 280, 100),
                            0, pi, 15)
                    pygame.draw.arc(screen, (255, 255, 0),
                            (400, 70, 230, 100),
                            0, pi, 15)

                    pygame.draw.rect(screen, (134, 167, 253), (1, 1, 58, 58))
                    pygame.draw.rect(screen, (253, 134, 138), (901, 901, 58, 58))
                elif self.map == 3:
                    screen.fill((91, 225, 240))
                    pygame.draw.circle(screen, (0, 200, 64), (260, 149), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (280, 149), 13)
                    pygame.draw.circle(screen, (255, 255, 255), (260, 133), 13)
                    pygame.draw.circle(screen, (255, 255, 255), (280, 133), 13)
                    pygame.draw.line(screen, (90, 4, 18), (270, 157), (270, 180), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (140, 389), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (160, 389), 13)
                    pygame.draw.circle(screen, (255, 255, 255), (140, 373), 13)
                    pygame.draw.circle(screen, (255, 255, 255), (160, 373), 13)
                    pygame.draw.line(screen, (90, 4, 18), (150, 397), (150, 420), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (680, 389), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (700, 389), 13)
                    pygame.draw.circle(screen, (255, 255, 255), (680, 373), 13)
                    pygame.draw.circle(screen, (255, 255, 255), (700, 373), 13)
                    pygame.draw.line(screen, (90, 4, 18), (690, 397), (690, 420), 3)

                    pygame.draw.circle(screen, (0, 200, 64), (500, 809), 13)
                    pygame.draw.circle(screen, (0, 200, 64), (520, 809), 13)
                    pygame.draw.circle(screen, (255, 255, 255), (500, 793), 13)
                    pygame.draw.circle(screen, (255, 255, 255), (520, 793), 13)
                    pygame.draw.line(screen, (90, 4, 18), (510, 817), (510, 840), 3)


                    pygame.draw.rect(screen, (255, 77, 0), (75, 30, 30, 90))
                    pygame.draw.polygon(screen, (90, 4, 18), ((75, 30), (90, 0), (105, 30)))
                    pygame.draw.polygon(screen, (255, 255, 255), ((82, 15), (90, 0), (98, 15)))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 40, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 60, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (85, 80, 10, 10))

                    pygame.draw.rect(screen, (255, 77, 0), (855, 630, 30, 90))
                    pygame.draw.polygon(screen, (90, 4, 18), ((855, 630), (870, 600), (885, 630)))
                    pygame.draw.polygon(screen, (255, 255, 255), ((862, 615), (870, 600), (878, 615)))
                    pygame.draw.rect(screen, (255, 255, 255), (865, 640, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (865, 660, 10, 10))
                    pygame.draw.rect(screen, (255, 255, 255), (865, 680, 10, 10))
                            
                    pygame.draw.rect(screen, (255, 77, 0), (435, 570, 30, 27))
                    pygame.draw.polygon(screen, (90, 4, 18), ((435, 570), (450, 540), (465, 570)))
                    pygame.draw.polygon(screen, (255, 255, 255), ((442, 555), (450, 540), (458, 555)))
                    pygame.draw.rect(screen, (255, 255, 255), (445, 580, 10, 10))
                        
                    pygame.draw.polygon(screen, (161, 250, 255), ((360, 420), (420, 360), (480, 420)))
                    pygame.draw.polygon(screen, (255, 255, 255), ((380, 400), (420, 360), (460, 400)))             
                            
                    pygame.draw.polygon(screen, (161, 250, 255), ((120, 900), (180, 780), (240, 900)))
                    pygame.draw.polygon(screen, (255, 255, 255), ((140, 860), (180, 780), (220, 860)))

                    pygame.draw.circle(screen, (161, 250, 255), (660, 120), 118)

                    pygame.draw.rect(screen, (134, 167, 253), (1, 1, 58, 58))
                    pygame.draw.rect(screen, (253, 134, 138), (901, 901, 58, 58))
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        dream = False
                    elif event.type == pygame.KEYDOWN:
                        running = True
                        if event.key == pygame.K_p:
                            state = False
                        
                        elif event.key == pygame.K_o:
                            state = True

                        elif event.key == pygame.K_LEFT:
                            move_red1_left = True
                            move_red2_left = True
                            move_red3_left = True

                        elif event.key == pygame.K_RIGHT:
                            move_red1_right = True
                            move_red2_right = True
                            move_red3_right = True


                        elif event.key == pygame.K_a:
                            move_blue1_a = True
                            move_blue2_a = True
                            move_blue3_a = True

                        elif event.key == pygame.K_d:
                            move_blue1_d = True
                            move_blue2_d = True
                            move_blue3_d = True

                        elif event.key == pygame.K_w:
                            move_blue1_w = True
                            move_blue2_w = True
                            move_blue3_w = True

                        elif event.key == pygame.K_s:
                            move_blue1_s = True
                            move_blue2_s = True
                            move_blue3_s = True

                        elif event.key == pygame.K_UP:
                            move_red1_up = True
                            move_red2_up = True
                            move_red3_up = True

                        elif event.key == pygame.K_DOWN:
                            move_red1_down = True
                            move_red2_down = True
                            move_red3_down = True

                    elif event.type == pygame.KEYUP:
                        running = False
                        if event.key == pygame.K_p:
                            state = False
                        
                        elif event.key == pygame.K_o:
                            state = True
                            
                        elif event.key == pygame.K_w:
                            move_blue1_w = False
                            move_blue2_w = False
                            move_blue3_w = False

                        elif event.key == pygame.K_a:
                            move_blue1_a = False
                            move_blue2_a = False
                            move_blue3_a = False

                        elif event.key == pygame.K_s:
                            move_blue1_s = False
                            move_blue2_s = False
                            move_blue3_s = False

                        elif event.key == pygame.K_d:
                            move_blue1_d = False
                            move_blue2_d = False
                            move_blue3_d = False

                        elif event.key == pygame.K_UP:
                            move_red1_up = False
                            move_red2_up = False
                            move_red3_up = False

                        elif event.key == pygame.K_DOWN:
                            move_red1_down = False
                            move_red2_down = False
                            move_red3_down = False

                        elif event.key == pygame.K_LEFT:
                            move_red1_left = False
                            move_red2_left = False
                            move_red3_left = False

                        elif event.key == pygame.K_RIGHT:
                            move_red1_right = False
                            move_red2_right = False
                            move_red3_right = False

                else:
                    if move_red1_up:
                        complete_red_tank_rotating.forward_movement(1)

                    if move_red2_up:
                        complete_red_tank_rotating.forward_movement(2)

                    if move_red3_up:
                        complete_red_tank_rotating.forward_movement(3)



                    if move_red1_left:
                        complete_red_tank_rotating.left_movement(1)

                    if move_red2_left:
                        complete_red_tank_rotating.left_movement(2)

                    if move_red3_left:
                        complete_red_tank_rotating.left_movement(3)



                    if move_red1_right:
                        complete_red_tank_rotating.right_movement(1)

                    if move_red2_right:
                        complete_red_tank_rotating.right_movement(2)

                    if move_red3_right:
                        complete_red_tank_rotating.right_movement(3)


                    if move_red1_down:
                        complete_red_tank_rotating.back_movement(1)
                    if move_red2_down:
                        complete_red_tank_rotating.back_movement(2)
                    if move_red3_down:
                        complete_red_tank_rotating.back_movement(3)


                    if move_blue1_s:
                        complete_blue_tank_rotating.back_movement(1)

                    if move_blue2_s:
                        complete_blue_tank_rotating.back_movement(2)

                    if move_blue3_s:
                        complete_blue_tank_rotating.back_movement(3)


                    if move_blue1_w:
                        complete_blue_tank_rotating.forward_movement(1)
                    if move_blue2_w:
                        complete_blue_tank_rotating.forward_movement(2)
                    if move_blue3_w:
                        complete_blue_tank_rotating.forward_movement(3)


                    if move_blue1_d:
                        complete_blue_tank_rotating.right_movement(1)
                    if move_blue2_d:
                        complete_blue_tank_rotating.right_movement(2)
                    if move_blue3_d:
                        complete_blue_tank_rotating.right_movement(3)


                    if move_blue1_a:
                        complete_blue_tank_rotating.left_movement(1)

                    if move_blue2_a:
                        complete_blue_tank_rotating.left_movement(2)

                    if move_blue3_a:
                        complete_blue_tank_rotating.left_movement(3)
                    if state:
                        screen.blit(complete_blue_tank_rotating.blue_tank_name, complete_blue_tank_rotating.rect)
                        screen.blit(complete_red_tank_rotating.red_tank_name, complete_red_tank_rotating.rect)
                    else:
                        screen.blit(pause_text, (420, 420))
                    
                    pygame.display.flip()
                    clock.tick(FPS)
                    continue
                break
        else:
            self.setGeometry(422, 83, 1075, 863)
            buttonReply = QMessageBox.information(self, "Ошибка", "Вы не выбрали карту!")



        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Enter()
    ex.show()
    sys.exit(app.exec())
