import pygame


class Rotate_blue_tank(pygame.sprite.Sprite):
    def __init__(self, blue_tank_name, x, y, number, position=2, name=0):
        pygame.sprite.Sprite.__init__(self)
        self.blue_tank_name = blue_tank_name
        self.name = name
        self.number = number
        if self.number == '1':
            self.name = 1
        if self.number == '2':
            self.name = 2
        if self.number == '3':
            self.name = 3
        self.blue_tank_name.convert_alpha()
        self.x = x
        self.y = y
        self.position = position
        self.x = self.x + 50
        self.y = self.y + 30
        self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y)) # изменить

    def right_rotating(self, *args):
        if self.position == 0:
            self.blue_tank_name = pygame.transform.rotate(self.blue_tank_name, -90)
            self.position = 1
            if args[0] == 'up':
                self.forward_movement(self)
            if args[0] == 'right':
                self.right_movement(self)
            if args[0] == 'left':
                self.left_movement(self)
            if args[0] == 'down':
                self.back_movement(self)

        elif self.position == 1:
            self.blue_tank_name = pygame.transform.rotate(self.blue_tank_name, -90)
            self.position = 2
            if args[0] == 'up':
                self.forward_movement(self)
            if args[0] == 'right':
                self.right_movement(self)
            if args[0] == 'left':
                self.left_movement(self)
            if args[0] == 'down':
                self.back_movement(self)

        elif self.position == 2:
            self.blue_tank_name = pygame.transform.rotate(self.blue_tank_name, -90)
            self.position = 3
            if args[0] == 'up':
                self.forward_movement(self)
            if args[0] == 'right':
                self.right_movement(self)
            if args[0] == 'left':
                self.left_movement(self)
            if args[0] == 'down':
                self.back_movement(self)

        elif self.position == 3:
            if args[0] == 'left':
                self.blue_tank_name = pygame.transform.rotate(self.blue_tank_name, -90)
                self.position = 0
            else:
                self.blue_tank_name = pygame.transform.rotate(self.blue_tank_name, 90)
                self.position = 2
            if args[0] == 'up':
                self.forward_movement(self)
            if args[0] == 'right':
                self.right_movement(self)
            if args[0] == 'left':
                self.left_movement(self)
            if args[0] == 'down':
                self.back_movement(self)


    def left_rotating(self, *args):
        if self.position == 0:
            self.blue_tank_name = pygame.transform.rotate(self.blue_tank_name, 90)
            self.position = 3
            if args[0] == 'up':
                self.forward_movement(self)
            if args[0] == 'right':
                self.right_movement(self)
            if args[0] == 'left':
                self.left_movement(self)
            if args[0] == 'down':
                self.back_movement(self)
        elif self.position == 3:
            self.blue_tank_name = pygame.transform.rotate(self.blue_tank_name, 90)
            self.position = 2
            if args[0] == 'up':
                self.forward_movement(self)
            if args[0] == 'right':
                self.right_movement(self)
            if args[0] == 'left':
                self.left_movement(self)
            if args[0] == 'down':
                self.back_movement(self)
        elif self.position == 2:
            self.blue_tank_name = pygame.transform.rotate(self.blue_tank_name, 90)
            self.position = 1
            if args[0] == 'up':
                self.forward_movement(self)
            if args[0] == 'right':
                self.right_movement(self)
            if args[0] == 'left':
                self.left_movement(self)
            if args[0] == 'down':
                self.back_movement(self)
        elif self.position == 1:
            self.blue_tank_name = pygame.transform.rotate(self.blue_tank_name, 90)
            self.position = 0
            if args[0] == 'up':
                self.forward_movement(self)
            if args[0] == 'right':
                self.right_movement(self)
            if args[0] == 'left':
                self.left_movement(self)
            if args[0] == 'down':
                self.back_movement(self)


    def forward_movement(self, *args):
        if self.position == 0:
            self.right_rotating('up')

        if self.position == 1:
            if self.y - 40 <= 0:
                pass
            else:
                if self.name == 1:
                    self.y -= 0.2
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 2:
                    self.y -= 0.06
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 3:
                    self.y -= 0.08
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))

        if self.position == 2:
            self.left_rotating('up')

        if self.position == 3:
            if self.y - 40 <= 0:
                pass
            else:
                if self.name == 1:
                    self.y -= 0.05
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 2:
                    self.y -= 0.01
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 3:
                    self.y -= 0.03
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))


    def left_movement(self, *args):
        if self.position == 0:
            if self.x - 40 <= 0:
                pass
            else:
                if self.name == 1:
                    self.x = self.x - 0.2
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 2:
                    self.x = self.x - 0.06
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 3:
                    self.x = self.x - 0.08
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
        elif self.position == 1:
            self.left_rotating('left')
        elif self.position == 2:
            if self.x - 40 <= 0:
                pass
            else:
                if self.name == 1:
                    self.x = self.x - 0.05
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 2:
                    self.x = self.x - 0.01
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 3:
                    self.x = self.x - 0.03
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
        elif self.position == 3:
            self.right_rotating('left')



    def right_movement(self, *args):
        if self.position == 0:
            if self.x + 40 >= 960:
                pass
            else:
                if self.name == 1:
                    self.x = self.x + 0.05
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 2:
                    self.x = self.x + 0.01
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 3:
                    self.x = self.x + 0.03
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
        elif self.position == 1:
            self.right_rotating('right')
        elif self.position == 2:
            if self.x + 40 >= 960:
                pass
            else:
                if self.name == 1:
                    self.x = self.x + 0.2
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 2:
                    self.x = self.x + 0.06
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 3:
                    self.x = self.x + 0.08
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
        elif self.position == 3:
            self.left_rotating('right')


    def back_movement(self, *args):
        if self.position == 0:
            self.left_rotating('down')
        if self.position == 1:
            if self.y + 40 >= 940:
                pass
            else:
                if self.name == 1:
                    self.y = self.y + 0.05
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 2:
                    self.y = self.y + 0.01
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 3:
                    self.y = self.y + 0.03
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
        if self.position == 2:
            self.right_rotating('down')
        if self.position == 3:
            if self.y + 40 >= 940:
                pass
            else:
                if self.name == 1:
                    self.y = self.y + 0.2
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 2:
                    self.y = self.y + 0.08
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
                if self.name == 3:
                    self.y = self.y + 0.06
                    self.rect = self.blue_tank_name.get_rect(center=(self.x, self.y))
