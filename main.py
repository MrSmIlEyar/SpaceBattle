import math
import random
import time
import pygame
import os
import sys

pygame.init()

size = width, height = 801, 601
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Battle")
space_ship_skin = 'space_ship1.png'
spaceship_with_shield_skin = 'spaceship_with_shield1.png'
dict_bought_ships = {}
with open('data/bougth_ships') as f:
    for line in f.readlines():
        line = line.split()
        dict_bought_ships[line[0]] = line[1]
for i in dict_bought_ships.keys():
    if dict_bought_ships[i] == '2':
        space_ship_skin = f'space_ship{i}.png'
        spaceship_with_shield_skin = f'spaceship_with_shield{i}.png'
bullet_sound = pygame.mixer.Sound('data/laser.wav')
bullet_sound.set_volume(0.1)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_font(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с шрифтом '{fullname}' не найден")
        sys.exit()
    return fullname


def draw(x, y, message, width, height, font_size=35, font_color=(255, 255, 255)):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        print_text(message, x, y, font_color=(50, 50, 50), font_size=font_size)

        if click[0] == 1:
            return 1
    else:
        print_text(message, x, y, font_size=font_size, font_color=font_color)
    return 0


score = 0
gayka_score = 0
with open('data/gaykascore.txt') as f:
    all_gayka_score = int(f.readline())
print(all_gayka_score)


def show_gayka_score():
    global gayka_score
    font_type = pygame.font.Font(load_font('font.ttf'), 35)
    text_score = font_type.render(str(gayka_score), True, (200, 200, 200))
    screen.blit(text_score, (37, 38))


def print_text(message, x, y, font_color=('#DAF4EC'), font_size=35):
    font_type = pygame.font.Font(load_font('font.ttf'), font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


def shop():
    global space_ship_skin, all_gayka_score, dict_bought_ships, spaceship_with_shield_skin, box_open
    bgshop_image = load_image('ShopBg.jpg')
    image = load_image("cursor.png")
    defolt_space_ship = load_image('space_ship1.png')
    gaykaim = load_image('gayka.png')
    cur_sprites = pygame.sprite.Group()
    cur = pygame.sprite.Sprite(cur_sprites)
    cur.image = image
    cur.rect = cur.image.get_rect()
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    space_ship2 = load_image('space_ship2.png')
    space_ship3 = load_image('space_ship3.png')
    space_ship4 = load_image('space_ship4.png')
    space_ship5 = load_image('space_ship5.png')
    space_ship6 = load_image('space_ship6.png')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                cur.rect.topleft = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_menu()
        with open('data/bougth_ships') as f:
            for line in f.readlines():
                line = line.split()
                dict_bought_ships[line[0]] = line[1]
        color = pygame.Color('#C0F56E')
        screen.fill((0, 0, 0))
        screen.blit(bgshop_image, (0, 0))
        for x in range(120, 521, 200):
            color = pygame.Color('#C0F56E')
            if dict_bought_ships[str(x // 200 + 1)] == '2':
                color = pygame.Color('#8EEB00')
            pygame.draw.rect(screen, color, (x, 50, 160, 200), border_radius=12)
        if dict_bought_ships['4'] == '2':
            color = pygame.Color('#8EEB00')
        else:
            color = pygame.Color('#C0F56E')
        pygame.draw.rect(screen, color, (120, 300, 160, 200), border_radius=12)
        if dict_bought_ships['5'] == '2':
            color = pygame.Color('#8EEB00')
        else:
            color = pygame.Color('#C0F56E')
        pygame.draw.rect(screen, color, (320, 300, 160, 200), border_radius=12)
        if dict_bought_ships['6'] == '2':
            color = pygame.Color('#EB6A97')
        else:
            color = pygame.Color('#B253D6')
        pygame.draw.rect(screen, color, (520, 300, 160, 200), border_radius=12)
        font_type = pygame.font.Font(load_font('font.ttf'), 37)
        text_score = font_type.render(str(all_gayka_score), True, (200, 200, 200))
        screen.blit(text_score, (37, 0))
        screen.blit(gaykaim, (1, 3))
        back_btn = draw(10, 570, 'Назад [ESC]', 60, 27, font_size=20)
        if back_btn == 1:
            show_menu()
        if dict_bought_ships['1'] == '0':
            btn_1 = draw(125, 195, 'Выбрать', 140, 27, font_size=35, font_color='#000000')
            if btn_1 == 1:
                space_ship_skin = 'space_ship1.png'
                spaceship_with_shield_skin = 'spaceship_with_shield1.png'
                dict_bought_ships['1'] = '2'
                delete_vybran('1')
        else:
            space_ship_skin = 'space_ship1.png'
            spaceship_with_shield_skin = 'spaceship_with_shield1.png'
            btn_1 = draw(125, 195, 'Выбран', 140, 27, font_size=35, font_color='#000000')
        screen.blit(defolt_space_ship, (165, 70))
        if dict_bought_ships['2'] == '1':
            btn_2 = draw(360, 195, '150', 100, 27, font_size=35, font_color='#000000')
            screen.blit(gaykaim, (430, 197))
            if btn_2 == 1 and all_gayka_score >= 150:
                with open('data/gaykascore.txt', 'w') as f:
                    f.write(str(all_gayka_score - 150))
                    all_gayka_score -= 150
                dict_bought_ships['2'] = '0'
        elif dict_bought_ships['2'] == '0':
            btn_2 = draw(325, 195, 'Выбрать', 140, 27, font_size=35, font_color='#000000')
            if btn_2 == 1:
                space_ship_skin = 'space_ship2.png'
                dict_bought_ships['2'] = '2'
                delete_vybran('2')
        elif dict_bought_ships['2'] == '2':
            space_ship_skin = 'space_ship2.png'
            spaceship_with_shield_skin = 'spaceship_with_shield2.png'
            btn_2 = draw(325, 195, 'Выбран', 140, 27, font_size=35,font_color='#000000')
        screen.blit(space_ship2, (370, 70))

        if dict_bought_ships['3'] == '1':
            btn_3 = draw(555, 195, '300', 100, 27, font_size=35, font_color='#000000')
            screen.blit(gaykaim, (630, 197))
            if btn_3 == 1 and all_gayka_score >= 300:
                with open('data/gaykascore.txt', 'w') as f:
                    f.write(str(all_gayka_score - 300))
                    all_gayka_score -= 300
                dict_bought_ships['3'] = '0'
        elif dict_bought_ships['3'] == '0':
            btn_3 = draw(525, 195, 'Выбрать', 140, 27, font_size=35,font_color='#000000')
            if btn_3 == 1:
                space_ship_skin = 'space_ship3.png'
                spaceship_with_shield_skin = 'spaceship_with_shield3.png'
                dict_bought_ships['3'] = '2'
                delete_vybran('3')
        elif dict_bought_ships['3'] == '2':
            space_ship_skin = 'space_ship3.png'
            spaceship_with_shield_skin = 'spaceship_with_shield3.png'
            btn_3 = draw(525, 195, 'Выбран', 140, 27, font_size=35,font_color='#000000')
        screen.blit(space_ship3, (570, 70))

        if dict_bought_ships['4'] == '1':
            btn_4 = draw(160, 445, '500', 100, 27, font_size=35,font_color='#000000')
            screen.blit(gaykaim, (235, 447))
            if btn_4 == 1 and all_gayka_score >= 500:
                with open('data/gaykascore.txt', 'w') as f:
                    f.write(str(all_gayka_score - 500))
                    all_gayka_score -= 500
                dict_bought_ships['4'] = '0'
        elif dict_bought_ships['4'] == '0':
            btn_4 = draw(125, 445, 'Выбрать', 140, 27, font_size=35,font_color='#000000')
            if btn_4 == 1:
                space_ship_skin = 'space_ship4.png'
                spaceship_with_shield_skin = 'spaceship_with_shield4.png'
                dict_bought_ships['4'] = '2'
                delete_vybran('4')
        elif dict_bought_ships['4'] == '2':
            space_ship_skin = 'space_ship4.png'
            spaceship_with_shield_skin = 'spaceship_with_shield4.png'
            btn_4 = draw(125, 445, 'Выбран', 140, 27, font_size=35,font_color='#000000')
        screen.blit(space_ship4, (165, 320))
        if dict_bought_ships['5'] == '1':
            btn_5 = draw(325, 445, 'Недоступен', 170, 27, font_size=24,font_color='#000000')
            if btn_5 == 1:
                if box_open:  # проверка на то, что выполнены все миссии
                    space_ship_skin = 'space_ship5.png'
                    spaceship_with_shield_skin = 'spaceship_with_shield5.png'
                    dict_bought_ships['5'] = '2'
                    delete_vybran('5')
                elif dict_bought_ships['4'] == '2':
                    space_ship_skin = 'space_ship4.png'
                    spaceship_with_shield_skin = 'spaceship_with_shield4.png'
                    btn_4 = draw(125, 445, 'Выбран', 140, 27, font_size=35, font_color='#000000')
        elif dict_bought_ships['6'] == '0':
            btn_5 = draw(325, 445, 'Выбрать', 140, 27, font_size=35,font_color='#000000')
            if btn_5 == 1:
                space_ship_skin = 'space_ship5.png'
                spaceship_with_shield_skin = 'spaceship_with_shield5.png'
                dict_bought_ships['5'] = '2'
                delete_vybran('5')
        elif dict_bought_ships['5'] == '2':
            space_ship_skin = 'space_ship5.png'
            spaceship_with_shield_skin = 'spaceship_with_shield5.png'
            btn_5 = draw(325, 445, 'Выбран', 140, 27, font_size=35,font_color='#000000')
        screen.blit(space_ship5, (365, 320))

        if dict_bought_ships['6'] == '1':
            btn_6 = draw(525, 445, '', 170, 27, font_size=35,font_color='#000000')
            screen.blit(pygame.transform.scale(load_image('artefact1.png'), (40, 40)),(535,445))
            screen.blit(pygame.transform.scale(load_image('artefact2.png'), (50, 42)), (575, 443))
            screen.blit(pygame.transform.scale(load_image('artefact3.png'), (47, 40)), (622, 443))
            if btn_6 == 1:
                with open('data/artefact_done', 'r') as f:
                    line = f.readline().split()
                if line == ['2', '2', '2']:
                    space_ship_skin = 'space_ship6.png'
                    spaceship_with_shield_skin = 'spaceship_with_shield6.png'
                    dict_bought_ships['6'] = '2'
                    delete_vybran('6')
        elif dict_bought_ships['6'] == '0':
            btn_6 = draw(525, 445, 'Выбрать', 140, 27, font_size=35,font_color='#000000')
            if btn_6 == 1:
                space_ship_skin = 'space_ship6.png'
                spaceship_with_shield_skin = 'spaceship_with_shield6.png'
                dict_bought_ships['6'] = '2'
                delete_vybran('6')
        elif dict_bought_ships['6'] == '2':
            space_ship_skin = 'space_ship6.png'
            spaceship_with_shield_skin = 'spaceship_with_shield6.png'
            btn_6 = draw(525, 445, 'Выбран', 140, 27, font_size=35,font_color='#000000')
        screen.blit(space_ship6, (565, 320))
        with open('data/bougth_ships', 'w') as f1:
            for k in dict_bought_ships.keys():
                f1.write(f'{k} {dict_bought_ships[k]}' + '\n')

        cur_sprites.draw(screen)
        pygame.display.update()


def delete_vybran(n):
    global dict_bought_ships
    for i in dict_bought_ships.keys():
        if i != n:
            if dict_bought_ships[i] == '2':
                dict_bought_ships[i] = '0'


def show_menu():
    pygame.event.clear()
    menu_bg = load_image('Menubg.jpg')
    butn_image = load_image('fonbutn.png')
    image = load_image("cursor.png")
    cur_sprites = pygame.sprite.Group()
    cur = pygame.sprite.Sprite(cur_sprites)
    cur.image = image
    cur.rect = cur.image.get_rect()
    screen.blit(cur.image, (450, 120))
    pygame.mouse.set_visible(False)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                cur.rect.topleft = event.pos
        screen.blit(menu_bg, (0, 0))
        screen.blit(butn_image, (565, 135))
        screen.blit(butn_image, (565, 202))
        screen.blit(butn_image, (565, 265))
        screen.blit(butn_image, (565, 328))
        screen.blit(butn_image, (565, 391))
        start_btn = draw(600, 160, 'Начать', 120, 27)
        if start_btn == 1:
            start_game()
        record_btn = draw(600, 225, 'Данные', 128, 27)
        if record_btn == 1:
            statistick()
        store_btn = draw(600, 290, 'Магазин', 140, 27)
        if store_btn == 1:
            shop()
        store_btn = draw(600, 351, 'Миссии', 140, 27)
        if store_btn == 1:
            missions()
        quit_btn = draw(600, 414, 'Выйти', 115, 27)
        if quit_btn == 1:
            pygame.quit()
            quit()
        pravila_btn = draw(3, 0, 'Правила', 115, 28, font_size=25)
        if pravila_btn == 1:
            pravila()
        cur_sprites.update()
        cur_sprites.draw(screen)
        pygame.display.update()
    return


with open('data/missions.txt') as f:
    m = list(map(int, f.readline().split(',')))
    stage_of_mission = m[0]
    mission1, mission2, mission3, mission4 = m[1], m[2], m[3], m[4]
    missions_complete = int(f.readline())

type_of_missions = [['Убить 500 монстров в одной игре.', mission1],
                    ['Подобрать 15 астронавтов в одной игре.', mission2],
                    ['Пройти 30 ракетных дождей.', mission3],
                    ['Разбить 30 метеоритов.', mission4],
                    ['Пройти игру.', False]]

missions_complete_1 = [500, 15, 30, 30]

screen_rect = (0, 0, width, height)


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    part = [load_image("gayka.png")]
    for scale in (5, 10, 20):
        part.append(pygame.transform.scale(part[0], (scale, scale)))

    def __init__(self, pos, dx, dy, group):
        super().__init__(group)
        self.image = random.choice(self.part)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость - это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой
        self.gravity = 0.25

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position, sprites_of_particles):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers), sprites_of_particles)


box_open = False


def missions():
    global stage_of_mission, mission1, mission2, mission3, mission4, missions_complete, type_of_missions, all_gayka_score, box_open
    bgmission_image = load_image('mission_bg.jpg')
    image = load_image("cursor.png")
    cur_sprites = pygame.sprite.Group()
    cur = pygame.sprite.Sprite(cur_sprites)
    cur.image = image
    cur.rect = cur.image.get_rect()
    pygame.mouse.set_visible(False)
    font_type = pygame.font.Font(load_font('font.ttf'), 40)
    label = font_type.render('Миссии', True, (255, 255, 255))
    screen.blit(label, (width // 2 - label.get_width() // 2, 0))
    stage_of_open_box = 1
    sprites_of_particles = pygame.sprite.Group()
    clock = pygame.time.Clock()
    FPS = 60
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.MOUSEMOTION:
                cur.rect.topleft = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 250 <= pos[0] <= 400 and 250 <= pos[1] <= 400:
                    stage_of_open_box += 1
                    if stage_of_open_box == 3:
                        create_particles(pos, sprites_of_particles)
        screen.fill((0, 0, 0))
        screen.blit(bgmission_image, (0, 0))
        if missions_complete != 5:
            screen.blit(load_image(os.path.join('progress_bar', f'progress_bar_{stage_of_mission}.png')), (245, 150))
            screen.blit(load_image(os.path.join('box', 'box1.png')), (495, 125))
            screen.blit(load_image(os.path.join('box', 'box1.png')), (495, 125))
            screen.blit(label, (width // 2 - label.get_width() // 2, 0))
            mission = font_type.render(type_of_missions[stage_of_mission - 1][0], True, (255, 255, 255))
            try:
                mission_counter = font_type.render(
                    str(eval(f'mission{stage_of_mission}')) + '/' + str(missions_complete_1[stage_of_mission - 1]),
                    True,
                    (255, 255, 255))
                screen.blit(mission_counter, (width // 2 - mission_counter.get_width() // 2, 350))
            except Exception:
                pass
            if mission.get_width() > width:
                font_type = pygame.font.Font(load_font('font.ttf'), 30)
                mission = font_type.render(type_of_missions[stage_of_mission - 1][0], True, (255, 255, 255))
                font_type = pygame.font.Font(load_font('font.ttf'), 40)
            screen.blit(mission, (width // 2 - mission.get_width() // 2, 275))
        else:
            with open('data/missions_complete.txt') as f:
                flag = int(f.readline())
            if flag == 0:
                if stage_of_open_box < 4:
                    screen.blit(
                        pygame.transform.scale(load_image(os.path.join('box', f'box{stage_of_open_box}.png')),
                                               (150, 150)),
                        (width // 2 - 75, height // 2 - 75))
                else:
                    with open('data/missions_complete.txt', 'w') as f:
                        f.write('1')
                    with open('data/gaykascore.txt', 'w') as f:
                        all_gayka_score += 50
                        f.write(str(all_gayka_score))
                    box_open = True
            else:
                font_type = pygame.font.Font(load_font('font.ttf'), 40)
                l = font_type.render('Миссии выполнены!', True, (255, 255, 255))
                screen.blit(l, (width // 2 - l.get_width() // 2, 250))
        sprites_of_particles.draw(screen)
        sprites_of_particles.update()
        clock.tick(FPS)
        cur_sprites.draw(screen)
        pygame.display.update()


def statistick():
    bgstatistick_image = load_image('statistickFon.jpg')
    image = load_image("cursor.png")
    defolt_space_ship = load_image('space_ship1.png')
    gaykaim = load_image('gayka.png')
    cur_sprites = pygame.sprite.Group()
    cur = pygame.sprite.Sprite(cur_sprites)
    cur.image = image
    cur.rect = cur.image.get_rect()
    pygame.mouse.set_visible(False)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                cur.rect.topleft = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_menu()
        screen.fill((0, 0, 0))
        screen.blit(bgstatistick_image, (0, 0))
        back_btn = draw(10, 570, 'Назад [ESC]', 60, 27, font_size=20)
        if back_btn == 1:
            show_menu()
        font_type = pygame.font.Font(load_font('font.ttf'), 65)
        label = font_type.render('Ваши результаты', True, (255, 255, 255))
        screen.blit(label, (110, 5))
        font_type = pygame.font.Font(load_font('font.ttf'), 30)
        label = font_type.render('Максимально очков набрано:', True, (255, 255, 255))
        screen.blit(label, (40, 130))
        s = []
        with open('data/results.txt') as f:
            for line in f.readlines():
                s.append(int(line.strip()))
        label = font_type.render(f'{max(s)}', True, (255, 255, 255))
        screen.blit(label, (512, 130))

        label = font_type.render('Всего убито врагов:', True, (255, 255, 255))
        screen.blit(label, (40, 190))
        label = font_type.render(f'{sum(s)}', True, (255, 255, 255))
        screen.blit(label, (355, 190))

        with open('data/astronavt_score.txt') as f1:
            k = f1.readline().strip()
        label = font_type.render('Всего спасено астронавтов:', True, (255, 255, 255))
        screen.blit(label, (40, 250))
        label = font_type.render(str(k), True, (255, 255, 255))
        screen.blit(label, (500, 250))

        with open('data/game_done', 'r') as f2:
            q = f2.readline().strip()
        label = font_type.render('Ваши награды:', True, (255, 255, 255))
        screen.blit(label, (40, 310))
        if q == '1':
            screen.blit(load_image('trofey.png'),(280,300))


        cur_sprites.draw(screen)
        pygame.display.update()


pygame.display.set_icon(load_image('icon.png'))


def game_over(gayka_score):
    global score
    record = 0
    pygame.mixer.music.load('data/game_over.wav')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    with open('data/results.txt', 'r') as f:
        s = list(map(int, f.readlines()))
        if score > s[-1]:
            record = 1
        s.append(score)
        s.sort()
    with open('data/results.txt', 'w') as f:
        for i in s:
            f.write(str(i) + '\n')

    image = load_image('bg_for_game_over.png')
    rect = image.get_rect()
    rect.x = -image.get_width()
    image2 = load_image(space_ship_skin)
    rect2 = image2.get_rect()
    rect2.y = -image2.get_height()
    rect2.x = width // 2 - image2.get_width() // 2
    v1 = 150
    v3 = 200
    v2 = -200
    font_type = pygame.font.Font(load_font('font.ttf'), 50)
    message = f'Гаек собрано: {gayka_score}'
    text = font_type.render(message, True, '#ffffff')
    rect_t = text.get_rect()
    rect_t.x = width
    rect_t.y = 250
    message2 = f'Очков набрано: {score}'
    text2 = font_type.render(message2, True, '#ffffff')
    rect_t2 = text.get_rect()
    rect_t2.x = -text2.get_width()
    rect_t2.y = 325
    if record:
        message3 = f'Новый рекорд!'
        text3 = font_type.render(message3, True, '#ffffff')
        rect_t3 = text3.get_rect()
        rect_t3.x = width // 2 - text3.get_width() // 2
        rect_t3.y = text3.get_height() + height
        v4 = -250
    FPS = 50
    score = 0
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.KEYDOWN:
                if v3 != 0 or v2 != 0 or v1 != 0:
                    v3 = v2 = v1 = v4 = 0
                    rect2.y = 150
                    rect_t.x = width // 2 - text.get_width() // 2
                    rect_t2.x = width // 2 - text2.get_width() // 2
                    if record:
                        rect_t3.y = 400
                else:
                    show_menu()
        screen.fill((0, 0, 0))
        screen.blit(image, (0, 0))
        rect2.y += v1 / FPS
        screen.blit(image2, (rect2.x, rect2.y))
        if rect2.y >= 100:
            v1 = 0
        rect_t.x += v2 / FPS
        screen.blit(text, (rect_t.x, rect_t.y))
        if rect_t.x <= width // 2 - text.get_width() // 2:
            v2 = 0
        rect_t2.x += v3 / FPS
        screen.blit(text2, (rect_t2.x, rect_t2.y))
        if rect_t2.x >= (width // 2 - text2.get_width() // 2):
            v3 = 0
        if record:
            rect_t3.y += v4 / FPS
            screen.blit(text3, (rect_t3.x, rect_t3.y))
            if rect_t3.y <= 400:
                v4 = 0
        pygame.display.update()
        clock.tick(FPS)


class Meteor(pygame.sprite.Sprite):
    image = load_image('meteor.png')
    v = 1

    def __init__(self, x, group):
        super().__init__(group)
        self.image = Meteor.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

    def update(self):
        self.rect.y += Meteor.v

    def x(self):
        return int(self.rect.x)

    def y(self):
        return int(self.rect.y)


class Bonus(pygame.sprite.Sprite):
    v = 10

    def __init__(self, x, y, name, type, group):
        super().__init__(group)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.timing = 0

    def update(self):
        self.rect.y += Bonus.v

    def ret_type(self):
        return int(self.type)

    def get_timing(self, other):
        self.timing = other

    def ret_timing(self):
        return self.timing

    def ret_image(self):
        return pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))


class Gayka(pygame.sprite.Sprite):
    image = load_image('gayka.png')
    v = 1

    def __init__(self, x, group):
        super().__init__(group)
        self.image = Gayka.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

    def update(self):
        self.rect.y += Gayka.v

    def x(self):
        return int(self.rect.x)

    def y(self):
        return int(self.rect.y)


class SpaceShip(pygame.sprite.Sprite):
    v = 15

    def __init__(self, group):

        super().__init__(group)
        self.image_with_shield = load_image(spaceship_with_shield_skin)
        self.image = load_image(space_ship_skin)
        self.rect = self.image.get_rect()
        self.type = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = width // 2 - self.image.get_width() // 2
        self.rect.y = height - self.image.get_height() - 25

    def update(self, v):
        self.rect.x += v
        if self.rect.x + self.image.get_width() > width:
            self.rect.x = width - self.image.get_width()
        if self.rect.x < 0:
            self.rect.x = 0

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

    def ret_x(self):
        return self.rect.x + self.image.get_width() // 2 - 7

    def ret_y(self):
        return self.rect.y - 25

    def ret_x_for_double_bullets_1(self):
        if self.type == 1:
            return self.rect.x + 5
        return self.rect.x + 25

    def ret_x_for_double_bullets_2(self):
        if self.type == 1:
            return self.rect.x + self.image.get_width() - 20
        return self.rect.x + self.image.get_width() - 40

    def ret_x_for_fire(self):
        return self.rect.x + 29

    def shield(self):
        self.image = self.image_with_shield
        self.type = 2

    def shield_off(self):
        self.image = load_image(space_ship_skin)
        self.type = 1


class Monster(pygame.sprite.Sprite):

    def __init__(self, pos_x, name, group):
        super().__init__(group)
        image = load_image(name)
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        for i in enemys:
            if self.rect.x <= i.rect.x < self.rect.x + self.image.get_width():
                while self.rect.x <= i.rect.x < self.rect.x + self.image.get_width():
                    self.rect.x = random.randint(0, 800 - self.image.get_width() // 2)
        self.rect.y = 0

    def update(self, v, gayka_score):
        self.rect.y += v
        if self.rect.y >= height - self.image.get_height():
            game_over(gayka_score)
            score = 0

    def ret_x(self):
        return self.rect.x


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
    pygame.quit()
    sys.exit()


def ship_death(x, y, group):
    pygame.mixer.music.load('data/boom_spaceship.wav')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    AnimatedDeath(1, x, y, group)


class AnimatedDeath(pygame.sprite.Sprite):
    def __init__(self, stage, x, y, group):
        super().__init__(group)
        name = os.path.join('animate_ship_death', f'animate_death_{stage}.png')
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, stage):
        name = os.path.join('animate_ship_death', f'animate_death_{stage}.png')
        self.image = load_image(name)


class Astronavt(pygame.sprite.Sprite):
    image = load_image('astronavt.png')

    def __init__(self, x, group):
        super().__init__(group)
        self.image = Astronavt.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

    def update(self, v):
        self.rect.y += v

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y


class Rocket(pygame.sprite.Sprite):
    image = load_image('rocket.png')

    def __init__(self, x, group):
        super().__init__(group)
        self.image = Rocket.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

    def update(self, v):
        self.rect.y += v

    def y(self):
        return self.rect.y

    def x(self):
        return self.rect.x


def pravila():
    bgpravila = load_image('pravilabg.jpg')
    image = load_image("cursor.png")
    defolt_space_ship = load_image('space_ship1.png')
    gaykaim = load_image('gayka.png')
    astonavt = load_image('astronavt.png')
    duble_bonus = load_image('bonus_2x.png')
    shield = load_image('shild.png')
    bon_gayka = load_image('bonus_gayka.png')
    cur_sprites = pygame.sprite.Group()
    cur = pygame.sprite.Sprite(cur_sprites)
    cur.image = image
    cur.rect = cur.image.get_rect()
    pygame.mouse.set_visible(False)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                cur.rect.topleft = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_menu()
        screen.fill((0, 0, 0))
        screen.blit(bgpravila, (0, 0))
        back_btn = draw(10, 570, 'Назад [ESC]', 60, 27, font_size=20)
        if back_btn == 1:
            show_menu()
        font_type = pygame.font.Font(load_font('font.ttf'), 65)
        label = font_type.render('Правила', True, (255, 255, 255))
        screen.blit(label, (250, 5))

        font_type = pygame.font.Font(load_font('font.ttf'), 22)
        label = font_type.render('В этой игре вам, в роли космического корабля предстоит ', True, (255, 255, 255))
        screen.blit(label, (15, 90))

        label = font_type.render(
            'сражаться с иноземными существами. Во время битвы сверху', True,
            (255, 255, 255))
        screen.blit(label, (15, 125))

        label = font_type.render(
            'будут падать различные бонусы, гайки', True,
            (255, 255, 255))
        screen.blit(label, (15, 160))
        screen.blit(gaykaim, (480, 157))

        label = font_type.render(
            '- валюта, за которую', True,
            (255, 255, 255))
        screen.blit(label, (515, 160))

        label = font_type.render(
            'можно покупать скины в магазине.', True,
            (255, 255, 255))
        screen.blit(label, (15, 195))

        label = font_type.render(
            'Также при сражение может', True,
            (255, 255, 255))
        screen.blit(label, (435, 195))

        label = font_type.render(
            'пролетать астронавт, которого не надо убивать. За его поимку ты получаешь 10 гаек.', True,
            (255, 255, 255))
        screen.blit(label, (15, 230))

        label = font_type.render(
            'получаешь 10 гаек. Во время игры сверху могут падать ракеты или', True,
            (255, 255, 255))
        screen.blit(label, (15, 265))

        label = font_type.render(
            'даже ракетный дождь, стрелять в ракеты бесмысленно, от них', True,
            (255, 255, 255))
        screen.blit(label, (15, 300))

        label = font_type.render(
            'можно только уворачиваться. В определенный момент времени', True,
            (255, 255, 255))
        screen.blit(label, (15, 335))

        label = font_type.render(
            'вам придется сражаться с боссами, разной сложности.', True,
            (255, 255, 255))
        screen.blit(label, (15, 370))

        label = font_type.render(
            'Бонусы выпадают при попадании в метеорит. Виды бонусов:', True,
            (255, 255, 255))
        screen.blit(label, (15, 405))
        screen.blit(duble_bonus, (15, 440))

        label = font_type.render(
            '- удваивания пуль.', True,
            (255, 255, 255))
        screen.blit(label, (70, 450))

        screen.blit(shield, (15, 500))
        label = font_type.render(
            '- щит, при соприкасании убивает вражескую цель.', True,
            (255, 255, 255))
        screen.blit(label, (70, 510))

        screen.blit(bon_gayka, (310, 440))
        label = font_type.render(
            '- удваивания получаемых гаек.', True,
            (255, 255, 255))
        screen.blit(label, (365, 450))

        cur_sprites.draw(screen)
        pygame.display.update()


class BossBullet(pygame.sprite.Sprite):
    image = load_image('boss1_bullet.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = BossBullet.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y


class EnemyBullet(pygame.sprite.Sprite):
    image = load_image('boss1_bullet.png')

    def __init__(self, pos, group, x_move):
        super().__init__(group)
        self.image = pygame.transform.rotate(load_image('boss1_bullet.png'), int(x_move * 5))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.x_move = x_move

    def update(self, v):
        self.rect.y += v
        self.rect.x += self.x_move


class Boss(pygame.sprite.Sprite):
    bullet1 = load_image('boss1_bullet.png')

    def __init__(self, hard, group, image):
        super().__init__(group)
        self.image = image
        if hard == 1:
            self.image = pygame.transform.scale(self.image, (110, 79))
            self.hp = 10
        elif hard == 2:
            self.hp = 25
        else:
            self.hp = 10
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.image.get_width() // 2
        self.rect.y = 100
        self.update()

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y

    def height(self):
        return self.image.get_height()

    def bullet_hit(self):
        if self.hp == 0:
            return 1
        self.hp -= 1
        return 0


def boss_fight(gayka_score, bonuces_on_spaceship, meteor_score, astronavt_score, rocket_rain_score,
               world_number=1):
    global mission1, mission2, mission3, mission4, stage_of_mission, type_of_missions, missions_complete
    bg = load_image(f'background{world_number}.png')
    print(score)
    font_type = pygame.font.Font(load_font('font.ttf'), 40)
    label = font_type.render(
        'Сражение с боссом!', True,
        (255, 255, 255))
    boss_sprites = pygame.sprite.Group()
    boss_image = load_image(f'boss{world_number}.png')
    boss = Boss(world_number, boss_sprites, boss_image)
    rect_t = label.get_rect()
    rect_t.x = -label.get_width()
    rect_t.y = 250
    FPS = 50
    v2 = 300
    clock = pygame.time.Clock()
    t = True
    while t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        rect_t.x += v2 / FPS
        screen.blit(label, (rect_t.x, rect_t.y))
        if rect_t.x > width:
            t = False
        pygame.display.update()
        clock.tick(FPS)
    death_ship_FPS = 60
    FPS = 50
    v = 50
    v_b = 400
    shield_on_space_ship = False
    place_for_blit_bonuces_on_spaceship = [[(1, 75), (35, 75)], [(1, 120), (35, 120)], [(1, 165), (35, 165)]]
    name_bonuces = [('bonus_2x.png', 1), ('shild.png', 2), ('bonus_gayka.png', 3)]
    boss_heard = load_image('boss_heart.png')
    pygame.mixer.init()
    bullet_sound = pygame.mixer.Sound('data/laser.wav')
    bullet_sound.set_volume(0.1)
    space_ship_sprites = pygame.sprite.Group()
    shot_sprites = pygame.sprite.Group()
    enemy_bullet_sprites = pygame.sprite.Group()
    space_ship = SpaceShip(space_ship_sprites)
    death_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    death_sprites = pygame.sprite.Group()
    death = False
    running = True
    start_time = time.time()
    stage_of_death = 1
    start_timecenter = time.time()
    font_type = pygame.font.Font(load_font('font.ttf'), 30)
    double_bullets = False
    gaykaim = load_image('gayka.png')
    stage = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.KEYDOWN and not death:
                if event.key == pygame.K_SPACE:
                    if double_bullets:
                        Bullet((space_ship.ret_x_for_double_bullets_1(), space_ship.ret_y()), bullet_sprites)
                        Bullet((space_ship.ret_x_for_double_bullets_2(), space_ship.ret_y()), bullet_sprites)
                    else:
                        Bullet((space_ship.ret_x(), space_ship.ret_y()), bullet_sprites)
                    bullet_sound.play()
                elif event.key == pygame.K_ESCAPE:
                    pause_in_game()
                    t = 1

        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            space_ship_sprites.update(-50 * 15 / FPS)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            space_ship_sprites.update(50 * 15 / FPS)
        if not death:
            screen.blit(load_image(os.path.join('anim_fire', f'fire_anim_{stage}.png')),
                        (space_ship.ret_x_for_fire(), 567))
        space_ship_sprites.draw(screen)
        if stage == 2:
            stage = 1
        else:
            stage = 2
        show_gayka_score()
        screen.blit(gaykaim, (1, 40))
        bullet_sprites.draw(screen)
        bullet_sprites.update(v_b / FPS)
        enemy_bullet_sprites.draw(screen)
        enemy_bullet_sprites.update(v_b / FPS)
        boss_sprites.update()
        boss_sprites.draw(screen)
        death_sprites.draw(screen)
        death_sprites.update(stage_of_death)

        label = font_type.render(f'{boss.hp}', True, (255, 255, 255))
        screen.blit(label, (boss.rect.x + 15, boss.rect.y - 30))
        screen.blit(boss_heard, (boss.rect.x + 50, boss.rect.y - 30))
        if shield_on_space_ship:
            if pygame.sprite.groupcollide(space_ship_sprites, enemy_bullet_sprites, False, True):
                pass
        else:
            for i in enemy_bullet_sprites:
                if pygame.sprite.collide_mask(space_ship, i):
                    i.kill()
                    death = True
                    ship_death(space_ship.x(), space_ship.y(), death_sprites)
                    space_ship.kill()
                    break

        if pygame.sprite.groupcollide(boss_sprites, bullet_sprites, False, True):
            boss.bullet_hit()
        if boss.hp == 0:
            boss.kill()
            stage_of_death = 2
            FPS = 25
            clock = pygame.time.Clock()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        end_game()
                screen.fill((0, 0, 0))
                screen.blit(bg, (0, 0))
                space_ship_sprites.draw(screen)
                screen.blit(pygame.transform.scale(
                    load_image(f'animate_ship_death/animate_death_{stage_of_death}.png'), (90, 90)),
                    (boss.x(), boss.y()))
                stage_of_death += 1
                if stage_of_death == 15:
                    if missions_complete == 5:
                        if world_number == 3:
                            stage_of_mission += 1
                            missions_complete += 1
                            m = [str(stage_of_mission), '500', '15', '30', '30', '1']
                            with open('data/missions.txt', 'w') as f:
                                f.write(','.join(m) + '\n' + str(missions_complete))
                    break
                clock.tick(FPS)
                pygame.display.update()
            screen.blit(load_image(f'background{world_number}.png'), (0, 0))
            space_ship = SpaceShip(space_ship_sprites)
            portal = load_image('portal.png')
            rect = portal.get_rect()
            rect.x = -portal.get_width()
            rect.y = 0
            FPS = 50
            v1 = 150
            if world_number == 3:
                if random.randint(1, 100) == 1:
                    t_art = True
                else:
                    t_art = False
                ret_y = -100
                color = pygame.Color('#9966cc')
                qw = True
                if t_art:
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                end_game()
                        screen.fill((0, 0, 0))
                        screen.blit(load_image('background3.png'), (0, 0))
                        with open('data/artefact_done', 'r') as f:
                            line = f.readline().split()
                            line[world_number - 1] = '2'
                            aretf = ' '.join(line)
                            with open('data/artefact_done', 'w') as f1:
                                f1.write(aretf)
                        pygame.draw.rect(screen, color, (330, ret_y, 120, 70))
                        screen.blit(load_image(f'artefact{world_number}.png'), (360, ret_y + 20))
                        if ret_y == 0:
                            qw = False
                        if qw:
                            ret_y += 0.5
                        else:
                            ret_y -= 0.5
                        if ret_y < -100:
                            break

                        rect.x += v1 / FPS
                        clock.tick(FPS)
                        pygame.display.update()
                with open('data/game_done', 'w') as f:
                    f.write(str(1))
                font_type = pygame.font.Font(load_font('font.ttf'), 40)
                label = font_type.render(
                    'Вы прошли игру!', True, '#D44EA4')
                screen.blit(label, (200, 170))
                label = font_type.render(
                    'Вы получаете награду ', True, '#D44EA4')
                screen.blit(label, (140, 230))
                screen.blit(load_image('trofey.png'), (620, 220))
                pygame.display.update()
                time.sleep(4)
                show_menu()
            else:
                if random.randint(1, 100) == 1:
                    t_art = True
                else:
                    t_art = False
                ret_y = -100
                color = pygame.Color('#9966cc')
                qw = True
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            end_game()
                    screen.fill((0, 0, 0))
                    screen.blit(bg, (0, 0))
                    boss_sprites.draw(screen)
                    space_ship_sprites.draw(screen)
                    screen.blit(portal, (rect.x, rect.y))
                    if t_art:
                        with open('data/artefact_done', 'r') as f:
                            line = f.readline().split()
                            line[world_number - 1] = '2'
                            aretf = ' '.join(line)
                            with open('data/artefact_done', 'w') as f1:
                                f1.write(aretf)
                        pygame.draw.rect(screen, color, (330, ret_y, 120, 70))
                        screen.blit(load_image(f'artefact{world_number}.png'), (360, ret_y + 20))
                        if ret_y == 0:
                            qw = False
                        if qw:
                            ret_y += 0.5
                        else:
                            ret_y -= 0.5

                    rect.x += v1 / FPS
                    clock.tick(FPS)
                    pygame.display.update()
                    if rect.x >= 0:
                        time.sleep(1)
                        break
                t_art = False
                start_game(world=True, world_number=world_number)

        if time.time() - start_time > 1.3 / world_number:
            start_time = time.time()
            r = space_ship.y() - boss.y() - boss.height()
            t = round(r / v_b * FPS)
            pos_sp_sh = space_ship.x() + load_image(space_ship_skin).get_width() // 2
            center = round(width / 2)
            r2 = -1 * (center - pos_sp_sh)
            dop_r2 = math.sin(math.atan(r2 / r))
            r2 -= dop_r2
            dop_r = math.cos(math.atan(r2 / r))
            r -= dop_r
            v_x = round(r2 / t)
            EnemyBullet((width // 2 - 28, boss.rect.y + boss.image.get_height() // 2), enemy_bullet_sprites, v_x)
        if time.time() - start_timecenter > 1.3 / world_number:
            start_timecenter = time.time()
            EnemyBullet((width // 2 - 28, boss.rect.y + boss.image.get_height() // 2), enemy_bullet_sprites, 0)
        if pygame.sprite.groupcollide(bullet_sprites, enemy_bullet_sprites, True, False):
            pass
        if death:
            death_sprites.draw(screen)
            death_sprites.update(stage_of_death)
            clock.tick(death_ship_FPS)
            stage_of_death += 1
            if stage_of_death == 15:
                if score > mission1 and missions_complete == 0:
                    mission1 = score
                    if mission1 >= 500:
                        stage_of_mission += 1
                        m = [str(stage_of_mission), '500', '0', '0', '0', '0']
                        missions_complete += 1
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))
                    else:
                        m = [str(stage_of_mission), str(score), '0', '0', '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))

                if astronavt_score > mission2 and missions_complete == 1:
                    mission2 = astronavt_score
                    print(mission2)
                    if mission2 >= 15:
                        missions_complete += 1
                        stage_of_mission += 1
                        m = [str(stage_of_mission), '500', '15', '0', '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))
                    else:
                        print(astronavt_score)
                        m = [str(stage_of_mission), '500', str(astronavt_score), '0', '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))

                if missions_complete == 2:
                    if mission3 >= 30:
                        stage_of_mission += 1
                        missions_complete += 1
                        m = [str(stage_of_mission), '500', '15', '30', '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))
                    else:
                        m = [str(stage_of_mission), '500', '15', str(rocket_rain_score), '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))

                if missions_complete == 3:
                    if mission3 >= 30:
                        stage_of_mission += 1
                        missions_complete += 1
                        m = [str(stage_of_mission), '500', '15', '30', '30', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))
                    else:
                        m = [str(stage_of_mission), '500', '15', '30', str(meteor_score), '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))

                game_over(gayka_score)
                show_menu()
        time_now = time.time()
        for i in bonuces_on_spaceship:
            if time_now - i[-1] > 15.0:
                if i[1] == 1:
                    double_bullets = False
                elif i[1] == 2:
                    space_ship.shield_off()
                    shield_on_space_ship = False
                else:
                    double_gayka = False
                del bonuces_on_spaceship[bonuces_on_spaceship.index(i)]
            else:
                if i[1] == 1:
                    double_bullets = True
                if i[1] == 2:
                    shield_on_space_ship = True
                    space_ship.shield()
                if i[1] == 3:
                    double_gayka = True
                font_type = pygame.font.Font(load_font('font.ttf'), 25)
                for j in range(len(bonuces_on_spaceship)):
                    time_bonus = font_type.render(str(15 - int(time_now - bonuces_on_spaceship[j][-1])), True,
                                                  (255, 255, 255))
                    screen.blit(bonuces_on_spaceship[j][0].ret_image(), place_for_blit_bonuces_on_spaceship[j][0])
                    screen.blit(time_bonus, place_for_blit_bonuces_on_spaceship[j][1])

        clock.tick(FPS)
        pygame.display.update()


class AnimFire(pygame.sprite.Sprite):
    anim = [os.path.join('anim_fire', 'fire_anim_2.png'), os.path.join('anim_fire', 'fire_anim_1.png')]

    def __init__(self, x, group):
        super().__init__(group)
        self.anim = AnimFire.anim
        self.stage = 1
        self.image = load_image(self.anim[self.stage])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 790

    def update(self, x):
        self.stage = abs(self.stage - 1)
        self.image = load_image(self.anim[self.stage])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 790


def show_score():
    global score
    font_type = pygame.font.Font(load_font('font.ttf'), 40)
    text_score = font_type.render(str(score), True, (255, 255, 255))
    screen.blit(text_score, (1, 0))


enemys = []


def start_game(world=False, world_number=1):
    global running, score, gayka_score, all_gayka_score, mission1, mission2, mission3, mission4, stage_of_mission, missions_complete
    score = score
    print(score)
    double_bullets = False
    rocket_rain = False
    rocket_rain_begin = False
    rocket_rain_score = 0
    meteor_score = 0
    double_gayka = False
    gayka_score = 0
    if not world:
        pygame.mixer.music.load('data/background.wav')
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play(-1)
    gaykaim = load_image('gayka.png')
    world_number = world_number
    pygame.mouse.set_visible(False)
    death_ship_FPS = 60
    FPS = 50
    v = 99
    v_b = 400
    v_r = 550
    Meteor.v = 10
    Bonus.v = 10
    pygame.mixer.init()
    clock = pygame.time.Clock()
    monster_sprites = pygame.sprite.Group()
    space_ship_sprites = pygame.sprite.Group()
    space_ship = SpaceShip(space_ship_sprites)
    bullet_sprites = pygame.sprite.Group()
    meteor_sprites = pygame.sprite.Group()
    rocket_sprites = pygame.sprite.Group()
    bonus_sprites = pygame.sprite.Group()
    boss_sprites = pygame.sprite.Group()
    astronavt_sprites = pygame.sprite.Group()
    death_sprites = pygame.sprite.Group()
    gayka_sprites = pygame.sprite.Group()
    death = False
    stage_of_death = 1
    stage = 1
    enemys = []
    bonuces = []
    shield_on_space_ship = False
    bonuces_on_spaceship = []
    astronavts = []
    place_for_blit_bonuces_on_spaceship = [[(1, 75), (35, 75)], [(1, 120), (35, 120)], [(1, 165), (35, 165)]]
    name_bonuces = [('bonus_2x.png', 1), ('shild.png', 2), ('bonus_gayka.png', 3)]
    roads = [15, 100, 185, 270, 355, 440, 525, 610, 695]
    rockets_in_rocket_rain = []
    roads_rocket = []
    t = 1
    astronavt_score = 0
    meteor_active = False
    font_type = pygame.font.Font(load_font('font.ttf'), 25)
    if world:
        world_number += 1
    for i in range(9):
        x = roads[i]
        enemys.append(
            Monster(x, f'monster{random.randint(world_number * 2 - 1, world_number * 2)}.png', monster_sprites))
    background = load_image(f'background{world_number}.png')
    if world:
        portal = load_image('portal.png')
        rect = portal.get_rect()
        rect.x = 0
        rect.y = 0
        FPS = 50
        v1 = 150
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            space_ship_sprites.draw(screen)
            monster_sprites.draw(screen)
            screen.blit(portal, (rect.x, rect.y))
            rect.x += v1 / FPS
            clock.tick(FPS)
            pygame.display.update()
            if rect.x >= width:
                break
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not death:
                if event.key == pygame.K_SPACE:
                    if double_bullets:
                        Bullet((space_ship.ret_x_for_double_bullets_1(), space_ship.ret_y()), bullet_sprites)
                        Bullet((space_ship.ret_x_for_double_bullets_2(), space_ship.ret_y()), bullet_sprites)
                    else:
                        Bullet((space_ship.ret_x(), space_ship.ret_y()), bullet_sprites)
                    bullet_sound.play()
                elif event.key == pygame.K_ESCAPE:
                    pause_in_game()
                    t = 1
                    pygame.event.clear()
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            space_ship_sprites.update(-50 * 15 / FPS)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            space_ship_sprites.update(50 * 15 / FPS)
        if not death:
            screen.blit(load_image(os.path.join('anim_fire', f'fire_anim_{stage}.png')),
                        (space_ship.ret_x_for_fire(), 567))
        space_ship_sprites.draw(screen)
        if stage == 2:
            stage = 1
        else:
            stage = 2
        gayka_sprites.draw(screen)
        gayka_sprites.update()
        if not rocket_rain:
            monster_sprites.draw(screen)
            monster_sprites.update(v / FPS, gayka_score)
        bullet_sprites.draw(screen)
        bullet_sprites.update(v_b / FPS)
        if not rocket_rain:
            meteor_sprites.draw(screen)
            meteor_sprites.update()
        show_score()
        show_gayka_score()
        screen.blit(gaykaim, (1, 40))
        m = list(pygame.sprite.groupcollide(monster_sprites, bullet_sprites, True, True).items())
        for i in range(len(m)):
            score += 1
            k = random.randint(0, 100)
            if not rocket_rain:
                if k != 12:
                    mon = Monster(m[i][0].ret_x(),
                                  f'monster{random.randint(world_number * 2 - 1, world_number * 2)}.png',
                                  monster_sprites)
                    enemys.append(mon)
                else:
                    astr = Astronavt(m[i][0].ret_x(), astronavt_sprites)
                    astronavts.append(astr)
                if score % 5 == 0 and score != 0:
                    k = random.randint(1, 20)
                    if k == 5:
                        meteor = Meteor(random.choice(roads), meteor_sprites)
                        meteor_active = True
                    else:
                        Rocket(random.choice(roads), rocket_sprites)
                if score % 10 == 0 and score != 0:
                    Gayka(random.choice(roads), gayka_sprites)
                if score % 200 == 0:
                    rocket_rain = True
                if score % 500 == 0 and score != 0:
                    boss_fight(gayka_score, bonuces_on_spaceship, meteor_score, astronavt_score, rocket_rain_score,
                               world_number)
            try:
                del enemys[enemys.index(m[i][0])]
            except Exception:
                pass
        if len(enemys) == 0 and not rocket_rain_begin:
            rocket_rain_score += 1
            print(rocket_rain_score)
            rocket_rain_begin = True
            for i in astronavts:
                i.kill()
            for i in meteor_sprites:
                i.kill()
            font_type = pygame.font.Font(load_font('font.ttf'), 70)
            label = font_type.render('Ракетный дождь!', True, (255, 255, 255))
            rect_t = label.get_rect()
            rect_t.x = -label.get_width()
            rect_t.y = height // 2 - label.get_height()
            FPS = 50
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        end_game()
                    if event.type == pygame.KEYDOWN:
                        pass
                screen.fill((0, 0, 0))
                screen.blit(background, (0, 0))
                space_ship_sprites.draw(screen)
                screen.blit(label, (rect_t.x, rect_t.y))
                rect_t.x += 10
                clock.tick(FPS)
                if rect_t.x >= width:
                    break
                pygame.display.update()
            pygame.event.clear()
            rocket_rain_begin_t = time.time()
        if meteor_active:
            xbonus = meteor.x()
            ybonus = meteor.y()
        if pygame.sprite.groupcollide(meteor_sprites, bullet_sprites, True, True):
            if stage_of_mission == 4:
                type_of_missions[stage_of_mission - 1][1] += 1
            name, type_b = random.choice(name_bonuces)
            bon = Bonus(xbonus + 10, ybonus + 10, name, type_b, bonus_sprites)
            meteor_active = False
            bonuces.append((bon, bon.ret_type()))
        rocket_sprites.update(v_r / FPS)
        rocket_sprites.draw(screen)
        for i in rocket_sprites:
            if pygame.sprite.collide_mask(i, space_ship):
                if not shield_on_space_ship:
                    i.kill()
                    space_ship.kill()
                    death = True
                    Meteor.v = 0
                    v_b = 0
                    v_r = 0
                    v = 0
                    ship_death(space_ship.x(), space_ship.y(), death_sprites)
                else:
                    space_ship.shield_off()
                    shield_on_space_ship = False
                    for j in range(len(bonuces_on_spaceship)):
                        if bonuces_on_spaceship[j][1] == 2:
                            del bonuces_on_spaceship[j]
                    i.kill()
        if not rocket_rain_begin:
            bonus_sprites.draw(screen)
            bonus_sprites.update()
            astronavt_sprites.draw(screen)
            astronavt_sprites.update(v / FPS)
        if shield_on_space_ship:
            if pygame.sprite.groupcollide(monster_sprites, space_ship_sprites, True, False):
                score += 1
                mon = Monster(random.choice(roads),
                              f'monster{random.randint(world_number * 2 - 1, world_number * 2)}.png',
                              monster_sprites)
                monster_sprites.add(mon)
        else:
            for i in monster_sprites:
                if pygame.sprite.collide_mask(i, space_ship) and not death:
                    space_ship.kill()
                    death = True
                    Meteor.v = 0
                    Bonus.v = 0
                    v_b = 0
                    v_r = 0
                    v = 0
                    ship_death(space_ship.x(), space_ship.y(), death_sprites)
                    break
        if death:
            death_sprites.draw(screen)
            death_sprites.update(stage_of_death)
            clock.tick(death_ship_FPS)
            stage_of_death += 1
            if stage_of_death == 15:
                if score > mission1 and missions_complete == 0:
                    mission1 = score
                    if mission1 >= 500:
                        stage_of_mission += 1
                        m = [str(stage_of_mission), '500', '0', '0', '0', '0']
                        missions_complete += 1
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))
                    else:
                        m = [str(stage_of_mission), str(score), '0', '0', '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))

                if astronavt_score > mission2 and missions_complete == 1:
                    mission2 = astronavt_score
                    print(mission2)
                    if mission2 >= 15:
                        missions_complete += 1
                        stage_of_mission += 1
                        m = [str(stage_of_mission), '500', '15', '0', '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))
                    else:
                        print(astronavt_score)
                        m = [str(stage_of_mission), '500', str(astronavt_score), '0', '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))

                if missions_complete == 2:
                    mission3 = rocket_rain_score
                    if mission3 >= 30:
                        stage_of_mission += 1
                        missions_complete += 1
                        m = [str(stage_of_mission), '500', '15', '30', '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))
                    else:
                        m = [str(stage_of_mission), '500', '15', str(rocket_rain_score), '0', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))

                if missions_complete == 3:
                    if mission3 >= 30:
                        stage_of_mission += 1
                        missions_complete += 1
                        m = [str(stage_of_mission), '500', '15', '30', '30', '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))
                    else:
                        m = [str(stage_of_mission), '500', '15', '30', str(meteor_score), '0']
                        with open('data/missions.txt', 'w') as f:
                            f.write(','.join(m) + '\n' + str(missions_complete))

                game_over(gayka_score)
                score = 0
                show_menu()
        if pygame.sprite.groupcollide(gayka_sprites, space_ship_sprites, True, False):
            if double_gayka:
                gayka_score += 1
                all_gayka_score += 1
            gayka_score += 1
            all_gayka_score += 1
            with open('data/gaykascore.txt', 'w') as f:
                f.write(str(all_gayka_score))
        for i in bonuces:
            if pygame.sprite.spritecollide(i[0], space_ship_sprites, False):
                q = time.time()
                w = [j[1] for j in bonuces_on_spaceship]
                if i[1] in w:
                    bonuces_on_spaceship[w.index(i[1])] = (i[0], i[1], q)
                else:
                    bonuces_on_spaceship.append((i[0], i[1], q))
                del bonuces[bonuces.index(i)]
        if pygame.sprite.groupcollide(bullet_sprites, meteor_sprites, True, True):
            meteor_score += 1
            pass
        if pygame.sprite.groupcollide(bonus_sprites, space_ship_sprites, True, False):
            pass
        if pygame.sprite.groupcollide(bullet_sprites, rocket_sprites, True, False):
            pass
        for i in astronavts:
            if i.y() > height:
                mon = Monster(i.x(), f'monster{random.randint(world_number * 2 - 1, world_number * 2)}.png',
                              monster_sprites)
                enemys.append(mon)
                del astronavts[astronavts.index(i)]
        for i in astronavt_sprites:
            if pygame.sprite.collide_mask(space_ship, i):
                gayka_score += 10
                astronavt_score += 1
                mon = Monster(i.x(), f'monster{random.randint(world_number * 2 - 1, world_number * 2)}.png',
                              monster_sprites)
                enemys.append(mon)
                i.kill()
        for i in bullet_sprites:
            for j in astronavt_sprites:
                if pygame.sprite.collide_mask(i, j):
                    game_over(gayka_score)
                    score = 0
                    show_menu()
        for i in meteor_sprites:
            if pygame.sprite.collide_mask(space_ship, i):
                if not shield_on_space_ship:
                    space_ship.kill()
                    death = True
                    Meteor.v = 0
                    Bonus.v = 0
                    v = 0
                    ship_death(space_ship.x(), space_ship.y(), death_sprites)
                else:
                    meteor_score += 1
        time_now = time.time()
        for i in bonuces_on_spaceship:
            if time_now - i[-1] > 15.0:
                if i[1] == 1:
                    double_bullets = False
                elif i[1] == 2:
                    space_ship.shield_off()
                    shield_on_space_ship = False
                else:
                    double_gayka = False
                del bonuces_on_spaceship[bonuces_on_spaceship.index(i)]
            else:
                if i[1] == 1:
                    double_bullets = True
                if i[1] == 2:
                    shield_on_space_ship = True
                    space_ship.shield()
                if i[1] == 3:
                    double_gayka = True
        for j in range(len(bonuces_on_spaceship)):
            time_bonus = font_type.render(str(15 - int(time_now - bonuces_on_spaceship[j][-1])), True,
                                          (255, 255, 255))
            screen.blit(bonuces_on_spaceship[j][0].ret_image(), place_for_blit_bonuces_on_spaceship[j][0])
            screen.blit(time_bonus, place_for_blit_bonuces_on_spaceship[j][1])
        font_type = pygame.font.Font(load_font('font.ttf'), 35)
        if rocket_rain_begin:
            if time_now - rocket_rain_begin_t < 10:
                screen.blit(font_type.render(str(10 - int(time_now - rocket_rain_begin_t)), True, (255, 255, 255)),
                            (width // 2 - 15, 0))
                if len(rockets_in_rocket_rain) < 7:
                    x = random.choice(roads)
                    if x in roads_rocket:
                        while x in roads_rocket:
                            x = random.choice(roads)
                    r = Rocket(x, rocket_sprites)
                    rockets_in_rocket_rain.append(r)
                    roads_rocket.append(x)
                for i in rockets_in_rocket_rain:
                    if i.y() >= height:
                        del rockets_in_rocket_rain[rockets_in_rocket_rain.index(i)]
                        del roads_rocket[roads_rocket.index(i.x())]
                        x = random.choice(roads)
                        if x in roads_rocket:
                            while x in roads_rocket:
                                x = random.choice(roads)
                        r = Rocket(x, rocket_sprites)
                        rockets_in_rocket_rain.append(r)
                        roads_rocket.append(x)
            else:
                score += 9
                for i in range(9):
                    x = roads[i]
                    enemys.append(
                        Monster(x, f'monster{random.randint(world_number * 2 - 1, world_number * 2)}.png',
                                monster_sprites))
                rocket_rain = False
                rocket_rain_begin = False
        clock.tick(FPS)
        pygame.display.update()
        if t == 1:
            t = 0
            pause()
            pygame.event.clear()


enemys = []
pos_enemys = []


def pause_in_game():
    t = True
    image = load_image("cursor.png")
    cur_sprites = pygame.sprite.Group()
    cur = pygame.sprite.Sprite(cur_sprites)
    cur.image = image
    cur.rect = cur.image.get_rect()
    pygame.mouse.set_visible(False)
    imagebg = load_image('bg_for_game_over.png')
    while t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                cur.rect.topleft = event.pos
        screen.blit(imagebg, (0, 0))
        color = pygame.Color('#007143')
        pygame.draw.rect(screen, color, (245, 170, 310, 260))
        butn_color = pygame.Color('#67E46F')
        pygame.draw.rect(screen, color, (245, 170, 310, 260))
        # pygame.draw.rect(screen, butn_color, (255, 255, 280, 50))
        btn_back = draw(265, 265, 'Продолжить', 270, 35, font_size=40)
        if btn_back == 1:
            t = False
        btn_menu = draw(345, 340, 'Меню', 120, 35, font_size=40)
        if btn_menu == 1:
            show_menu()
        font_type = pygame.font.Font(load_font('font.ttf'), 50)
        text_score = font_type.render('Пауза', True, (255, 255, 255))
        screen.blit(text_score, (320, 175))
        cur_sprites.draw(screen)
        pygame.display.update()


def pause():
    time_spawn = 3
    font_type = pygame.font.Font(load_font('font.ttf'), 50)
    x = width // 2 - 155
    while time_spawn > 0:
        label = font_type.render(str(time_spawn), True, (255, 255, 255))
        screen.blit(label, (x, height // 2 - 100))
        pygame.display.update()
        x += 120
        time.sleep(1)
        time_spawn -= 1
    font_type = pygame.font.Font(load_font('font.ttf'), 70)
    label = font_type.render('Начали!', True, (255, 255, 255))
    screen.blit(label, (width // 2 - 145, height // 2))
    pygame.display.update()
    time.sleep(0.5)
    pygame.event.clear()


running = True
show_menu()