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
    menu_bg = pygame.image.load('Menubg.jpg')

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


def end_game():
    running = False
    pygame.quit()
    sys.exit()


def start_game():
    global running
    background = load_image('background.png')
    FPS = 50
    v = 1
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        clock.tick(FPS)
        where = -1
        pygame.display.update()


running = True
