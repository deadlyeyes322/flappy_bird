# Flappy Bird main

import pygame
import random, os, time, sys

class Bird:
    def __init__(self, x, y, color_bird):
        self.x = x
        self.y = y
        # color_bird - словарь из изображений птицы
        self.color_bird = color_bird
        self.bird_size = (50, 35)
        self.__image = None

        # Статус это то какую картинку мы ставим
        # Либо мы ставим с крыльями вверх, вниз или по середине
        # 0 - вниз, 1 - по середине, 2 - вверх
        self.status = 0

        self.jump_state = False
        self.frames = 0


    # в функции Rect получаем изображение птички
    def rect(self):
        cur_state = 'down' * (self.status % 3 == 0) + 'mid' * (self.status % 3 == 1) \
                    + 'up' * (self.status % 3 == 2)
        self.__image = pygame.image.load(resource_path(self.color_bird[cur_state]))
        self.__image = pygame.transform.scale(self.__image, self.bird_size)
        self.__image.convert_alpha()

        self.status += 1

        if self.jump_state == True:
            self.__image = pygame.transform.rotate(self.__image, 45)
        else:
            self.__image = pygame.transform.rotate(self.__image, -45)

        return self.__image.get_rect()

    # get_image - возвращает исходную ссылку на изображение
    def get_image(self):
        return self.__image

    # Проверка нужно ли совершать прыжок
    def end_jump(self):
        return self.jump_state

    # Функция осуществления прыжка
    def jump(self):
        if self.frames > 13:
            self.frames = 0
            self.jump_state = False
            pass
        else:
            self.frames += 1
            self.y -= 7
            self.jump_state = True



    # Гравитация тянущая птичку вниз\
    def gravity(self):
        self.y += 2

    # Смерть птички
    def death_bird(self):
        pass

class Wall:
    def __init__(self, wall):
        self.h1 = random.randint(155, 370)
        self.h2 = 512 - 150 - self.h1
        self.wall = wall
        self.x = WIDTH
        self.start_pos1 = 330
        self.start_pos2 = 330 - 24
        self.image = None

    def draw_down(self):
        self.image = pygame.transform.scale(self.wall, (100, 1))
        self.image.convert_alpha()

        return self.image.get_rect()

    def pos(self):
        wall_rect = self.draw_down()
        wall_rect.center = self.start_pos1, self.h1
        self.start_pos1 -= 2

        return wall_rect

    def draw_up(self):
        self.image = pygame.transform.rotate(self.wall, 180)
        self.image = pygame.transform.scale(self.image, (100, 1))
        self.image.convert_alpha()

        return self.image.get_rect()

    def pos2(self):
        wall_rect = self.draw_up()
        wall_rect.center = self.start_pos2 + 24, self.h2
        self.start_pos2 -= 2

        return wall_rect


WIDTH = 288
HEIGHT = 512
BLACK = (0, 0, 0)
FPS = 60
POS = [50, 250]

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    global POS

    # screen maker
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.display.set_caption("Flappy Bird")

    # bird maker
    player = Bird(POS[0], POS[1], bird_assets()[1])

    # созданные стены
    walls = [Wall(wall_assets()[0])]

    running = True
    while running:
        # Смотрим вызовы пользователя
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.jump_state = True

        player.gravity()
        if player.jump_state == True:
            player.jump()

        # В классе Bird вызываем rect() и получаем rect из изображения
        rect = player.rect()
        # Выстраиваем позицию изображения
        rect.center = (player.x, player.y)



        # Заполняем экран фоном
        screen.blit(backgrounds()[0], (0, 0))

        screen.blit(wall_assets()[0], walls[0].pos())
        screen.blit(wall_assets()[0], walls[0].pos2())

        # # Рисукм землю
        screen.blit(ground_assets(), (0, 400))

        # Блитуем Rect, доставая image и используя ранее созданный rect
        screen.blit(player.get_image(), rect)

        # Рисуем птичку
        pygame.draw.rect(screen, BLACK, rect, 1)

        if player.y > 400:
            screen.blit(game_over_assets(), (50, 130))

        # Обновляем экран
        pygame.display.update()
        pygame.time.Clock().tick(FPS + 60)



def game_over():
    pass


def game_over_assets():

    go_assets = pygame.image.load(resource_path('assets/sprites/gameover.png'))

    return go_assets

def ground_assets():

    ground = pygame.image.load(resource_path('assets/sprites/base.png'))

    return ground

def wall_assets():

    wall_green = pygame.image.load(resource_path('assets/sprites/pipe-green.png'))
    wall_red = pygame.image.load(resource_path('assets/sprites/pipe-red.png'))

    return wall_red, wall_green


def bird_assets():

    bird_blue = {'down': resource_path('assets/sprites/bluebird-downflap.png'),
                 'mid': resource_path('assets/sprites/bluebird-midflap.png'),
                 'up': resource_path('assets/sprites/bluebird-upflap.png')}
    red_bird = {'down': resource_path('assets/sprites/redbird-downflap.png'),
                'mid': resource_path('assets/sprites/redbird-midflap.png'),
                'up': resource_path('assets/sprites/redbird-upflap.png')}
    yellow_bird = {'down': resource_path('assets/sprites/yellowbird-downflap.png'),
                   'mid': resource_path('assets/sprites/yellowbird-midflap.png'),
                   'up': resource_path('assets/sprites/yellowbird-upflap.png')}

    return bird_blue, red_bird, yellow_bird

def backgrounds():

    day_bg = pygame.image.load(resource_path('assets/sprites/background-day.png'))
    night_bg = pygame.image.load(resource_path('assets/sprites/background-night.png'))

    return day_bg, night_bg

if __name__ == "__main__":
    main()
