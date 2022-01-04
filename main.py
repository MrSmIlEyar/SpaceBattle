import random
import time
import pygame
import os
import sys

pygame.init()

size = width, height = 801, 601
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Battle")


def draw(x, y, message, width, height, font_size=35):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        print_text(message, x, y, font_color=(50, 50, 50), font_size=font_size)

        if click[0] == 1:
            return 1
    else:
        print_text(message, x, y, font_size=font_size)
    return 0


def print_text(message, x, y, font_color=(0, 0, 0), font_size=30):
    font_type = pygame.font.Font(pygame.font.get_default_font(), font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


def show_menu():
    menu_bg = load_image('Menubg.jpg')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(menu_bg, (0, 0))
        start_btn = draw(600, 170, 'Начать', 80, 27)
        if start_btn == 1:
            start_game()
        record_btn = draw(600, 230, 'Рекорды', 160, 27)
        if record_btn == 1:
            pass
        store_btn = draw(600, 290, 'Магазин', 160, 27)
        if store_btn == 1:
            pass
        quit_btn = draw(600, 350, 'Выйти', 70, 27)
        if quit_btn == 1:
            pygame.quit()
            quit()
        pygame.display.update()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class SpaceShip(pygame.sprite.Sprite):
    image = load_image('spaceship.png')
    v = 10

    def __init__(self, group):
        super().__init__(group)
        self.image = SpaceShip.image
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.image.get_width() // 2
        self.rect.y = height - self.image.get_height() - 25

    def update(self):
        self.v = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.v = -SpaceShip.v
        if keystate[pygame.K_RIGHT]:
            self.v = SpaceShip.v
        self.rect.x += self.v
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

    def ret_x(self):
        return self.rect.x + self.image.get_width() // 2 - 7

    def ret_y(self):
        return self.rect.y - 25



class Monster(pygame.sprite.Sprite):

    def __init__(self, pos_x, name, group):
        super().__init__(group)
        image = load_image(name)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        for i in enemys:
            if self.rect.x <= i.rect.x < self.rect.x + self.image.get_width():
                while self.rect.x <= i.rect.x < self.rect.x + self.image.get_width():
                    self.rect.x = random.randint(0, 800 - self.image.get_width() // 2)
        self.rect.y = 0

    def update(self, v):
        self.rect.y += v
        if self.rect.y >= height - self.image.get_height():
            end_game()


class Bullet(pygame.sprite.Sprite):
    image = load_image('bullet.png')

    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, v):
        self.rect.y -= v


def end_game():
    running = False
    pygame.quit()
    sys.exit()


def start_game():
    global running
    monster_sprites = pygame.sprite.Group()
    space_ship_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    space_ship = SpaceShip(space_ship_sprites)
    background = load_image('background.png')
    FPS = 50
    v = 99
    v_b = 400
    clock = pygame.time.Clock()
    roads = [15, 100, 185, 270, 355, 440, 525, 610, 695]
    enemys = []
    for i in range(9):
        x = roads[i]
        enemys.append(Monster(x, f'monster{random.randint(1, 2)}.png', monster_sprites))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Bullet((space_ship.ret_x(), space_ship.ret_y()), bullet_sprites)
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        space_ship_sprites.update()
        space_ship_sprites.draw(screen)
        monster_sprites.draw(screen)
        monster_sprites.update(v / FPS)
        bullet_sprites.update(v_b / FPS)
        bullet_sprites.draw(screen)
        clock.tick(FPS)
        pygame.display.update()


enemys = []
pos_enemys = []

running = True
show_menu()