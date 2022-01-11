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
dict_bought_ships = {}
with open('data/bougth_ships') as f:
    for line in f.readlines():
        line = line.split()
        dict_bought_ships[line[0]] = line[1]
for i in dict_bought_ships.keys():
    if dict_bought_ships[i] == '2':
        space_ship_skin = f'space_ship{i}.png'
pygame.mixer.music.load('data/background.wav')
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)
bullet_sound = pygame.mixer.Sound('data/laser.wav')
bullet_sound.set_volume(0.1)


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
    global space_ship_skin, all_gayka_score, dict_bought_ships
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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                cur.rect.topleft = event.pos
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
        font_type = pygame.font.Font(load_font('font.ttf'), 37)
        text_score = font_type.render(str(all_gayka_score), True, (200, 200, 200))
        screen.blit(text_score, (37, 0))
        screen.blit(gaykaim, (1, 3))
        back_btn = draw(10, 570, 'Назад', 60, 27, font_size=20)
        if back_btn == 1:
            show_menu()
        if dict_bought_ships['1'] == '0':
            btn_1 = draw(125, 195, 'Выбрать', 140, 27, font_size=35, font_color='#000000')
            if btn_1 == 1:
                space_ship_skin = 'space_ship1.png'
                dict_bought_ships['1'] = '2'
                delete_vybran('1')
        else:
            space_ship_skin = 'space_ship1.png'
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
            btn_2 = draw(325, 195, 'Выбран', 140, 27, font_size=35, font_color='#000000')
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
            btn_3 = draw(525, 195, 'Выбрать', 140, 27, font_size=35, font_color='#000000')
            if btn_3 == 1:
                space_ship_skin = 'space_ship3.png'
                dict_bought_ships['3'] = '2'
                delete_vybran('3')
        elif dict_bought_ships['3'] == '2':
            space_ship_skin = 'space_ship3.png'
            btn_3 = draw(525, 195, 'Выбран', 140, 27, font_size=35, font_color='#000000')
        screen.blit(space_ship3, (570, 70))

        if dict_bought_ships['4'] == '1':
            btn_3 = draw(160, 445, '500', 100, 27, font_size=35, font_color='#000000')
            screen.blit(gaykaim, (235, 447))
            if btn_3 == 1 and all_gayka_score >= 500:
                with open('data/gaykascore.txt', 'w') as f:
                    f.write(str(all_gayka_score - 500))
                    all_gayka_score -= 500
                dict_bought_ships['4'] = '0'
        elif dict_bought_ships['4'] == '0':
            btn_3 = draw(125, 445, 'Выбрать', 140, 27, font_size=35, font_color='#000000')
            if btn_3 == 1:
                space_ship_skin = 'space_ship4.png'
                dict_bought_ships['4'] = '2'
                delete_vybran('4')
        elif dict_bought_ships['4'] == '2':
            space_ship_skin = 'space_ship4.png'
            btn_3 = draw(125, 445, 'Выбран', 140, 27, font_size=35, font_color='#000000')
        screen.blit(space_ship4, (165, 320))
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
        screen.blit(butn_image, (565, 327))
        start_btn = draw(600, 160, 'Начать', 120, 27)
        if start_btn == 1:
            start_game()
        record_btn = draw(600, 230, 'Рекорды', 160, 27)
        if record_btn == 1:
            pass
        store_btn = draw(600, 290, 'Магазин', 140, 27)
        if store_btn == 1:
            shop()
        quit_btn = draw(600, 350, 'Выйти', 115, 27)
        if quit_btn == 1:
            pygame.quit()
            quit()
        cur_sprites.update()
        cur_sprites.draw(screen)
        pygame.display.update()
    return


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def game_over(gayka_score):
    global score
    record = 0
    pygame.mixer.music.load('data/game_over.wav')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1)
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
    image_with_shield = load_image('spaceship_with_shield.png')
    v = 15

    def __init__(self, group):
        super().__init__(group)
        self.image = load_image(space_ship_skin)
        self.rect = self.image.get_rect()
        self.type = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = width // 2 - self.image.get_width() // 2
        self.rect.y = height - self.image.get_height() - 25

    def update(self):
        self.v = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.v = -SpaceShip.v
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.v = SpaceShip.v
        self.rect.x += self.v
        if self.rect.x > width - self.image.get_width():
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

    def shield(self):
        self.image = SpaceShip.image_with_shield
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
    AnimatedDeath(1, x, y, group)
    pygame.mixer.music.load('data/boom_spaceship.wav')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1)


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


def show_score():
    global score
    font_type = pygame.font.Font(load_font('font.ttf'), 40)
    text_score = font_type.render(str(score), True, (255, 255, 255))
    screen.blit(text_score, (1, 0))

enemys = []

def start_game():
    global running, double_bullets, time_t, score, gayka_score, all_gayka_score
    score = 0
    double_bullets = False
    gayka_rain = False
    rocket_rain = False
    rocket_rain_begin = False
    gayka_score = 0
    gaykaim = load_image('gayka.png')
    background = load_image('background.png')
    pygame.mouse.set_visible(False)
    death_ship_FPS = 60
    FPS = 50
    v = 99
    v_b = 400
    v_r = 550
    Meteor.v = 10
    pygame.mixer.init()
    clock = pygame.time.Clock()
    monster_sprites = pygame.sprite.Group()
    space_ship_sprites = pygame.sprite.Group()
    shot_sprites = pygame.sprite.Group()
    space_ship = SpaceShip(space_ship_sprites)
    bullet_sprites = pygame.sprite.Group()
    meteor_sprites = pygame.sprite.Group()
    rocket_sprites = pygame.sprite.Group()
    bonus_sprites = pygame.sprite.Group()
    boss_sprites = pygame.sprite.Group()
    astronavt_sprites = pygame.sprite.Group()
    death_sprites = pygame.sprite.Group()
    gayka_sprites = pygame.sprite.Group()
    monster_death_sprites = pygame.sprite.Group()
    death = False
    stage_of_death = 1
    time_t = True
    boss_mode = False
    boss_mode_first = False
    enemys = []
    bonuces = []
    shield_on_space_ship = False
    bonuces_on_spaceship = []
    astronavts = []
    place_for_blit_bonuces_on_spaceship = [[(1, 75), (35, 75)], [(1, 120), (35, 120)], [(1, 165), (35, 165)]]
    name_bonuces = [('bonus_2x.png', 1), ('shild.png', 2)]
    roads = [15, 100, 185, 270, 355, 440, 525, 610, 695]
    rockets_in_rocket_rain = []
    roads_rocket = []
    for i in range(9):
        x = roads[i]
        enemys.append(Monster(x, f'monster{random.randint(1, 2)}.png', monster_sprites))
    t = 1
    meteor_active = False
    font_type = pygame.font.Font(load_font('font.ttf'), 25)
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
                        shot_sprites.draw(screen)
                        shot_sprites.update(2)
                        shot_sprites.draw(screen)
                    bullet_sound.play()
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        space_ship_sprites.update()
        space_ship_sprites.draw(screen)
        if not gayka_rain:
            monster_death_sprites.update()
            monster_death_sprites.draw(screen)
        gayka_sprites.draw(screen)
        gayka_sprites.update()
        if boss_mode:
            if boss_mode_first:
                enemys.clear()
                for i in monster_sprites:
                    i.kill()
                Boss(1, v / FPS, boss_sprites)
                boss_mode_first = False
                clock.tick(FPS)
        else:
            monster_sprites.draw(screen)
            monster_sprites.update(v / FPS, gayka_score)
        bullet_sprites.draw(screen)
        bullet_sprites.update(v_b / FPS)
        if not boss_mode and not gayka_rain:
            meteor_sprites.draw(screen)
            meteor_sprites.update()
        show_score()
        show_gayka_score()
        screen.blit(gaykaim, (1, 40))
        m = list(pygame.sprite.groupcollide(monster_sprites, bullet_sprites, True, True).items())
        for i in range(len(m)):
            del enemys[enemys.index(m[i][0])]
            score += 1
            k = random.randint(0, 100)
            if not rocket_rain:
                if k != 12:
                    mon = Monster(m[i][0].ret_x(), f'monster{random.randint(1, 2)}.png', monster_sprites)
                    enemys.append(mon)
                else:
                    astr = Astronavt(m[i][0].ret_x(), astronavt_sprites)
                    astronavts.append(astr)
                if score % 5 == 0 and score != 0:
                    k = random.randint(1, 10)
                    if k != 5:
                        meteor = Meteor(random.choice(roads), meteor_sprites)
                        meteor_active = True
                    else:
                        Rocket(random.choice(roads), rocket_sprites)
                if score % 1000 == 0:
                    boss_mode = True
                    boss_mode_first = True
                if score % 10 == 0 and score != 0:
                    Gayka(random.choice(roads), gayka_sprites)
                if score % 10 == 0:
                    rocket_rain = True
        if len(enemys) == 0 and not rocket_rain_begin:
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
            print(rocket_rain_begin_t)
        if meteor_active:
            xbonus = meteor.x()
            ybonus = meteor.y()
        if pygame.sprite.groupcollide(meteor_sprites, bullet_sprites, True, True):
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
        boss_sprites.draw(screen)
        boss_sprites.update(2, v / FPS, boss_sprites)
        if shield_on_space_ship:
            if pygame.sprite.groupcollide(monster_sprites, space_ship_sprites, True, False):
                mon = Monster(random.choice(roads), f'monster{random.randint(1, 2)}.png', monster_sprites)
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
                game_over(gayka_score)
                show_menu()
        if pygame.sprite.groupcollide(gayka_sprites, space_ship_sprites, True, False):
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
            pass
        if pygame.sprite.groupcollide(bonus_sprites, space_ship_sprites, True, False):
            pass
        if pygame.sprite.groupcollide(bullet_sprites, rocket_sprites, True, False):
            pass
        for i in astronavts:
            if i.y() > height:
                mon = Monster(i.x(), f'monster{random.randint(1, 2)}.png', monster_sprites)
                enemys.append(mon)
                del astronavts[astronavts.index(i)]
        for i in astronavt_sprites:
            if pygame.sprite.collide_mask(space_ship, i):
                gayka_score += 10
                mon = Monster(i.x(), f'monster{random.randint(1, 2)}.png', monster_sprites)
                enemys.append(mon)
                i.kill()
        for i in bullet_sprites:
            for j in astronavt_sprites:
                if pygame.sprite.collide_mask(i, j):
                    game_over(gayka_score)
                    show_menu()
        for i in meteor_sprites:
            if pygame.sprite.collide_mask(space_ship, i):
                if not shield_on_space_ship:
                    space_ship.kill()
                    death = True
                    Meteor.v = 0
                    v = 0
                    ship_death(space_ship.x(), space_ship.y(), death_sprites)
        time_now = time.time()
        for i in bonuces_on_spaceship:
            if time_now - i[-1] > 15.0:
                if i[1] == 1:
                    double_bullets = False
                elif i[1] == 2:
                    space_ship.shield_off()
                    shield_on_space_ship = False
                del bonuces_on_spaceship[bonuces_on_spaceship.index(i)]
            else:
                if i[1] == 1:
                    double_bullets = True
                elif i[1] == 2:
                    shield_on_space_ship = True
                    space_ship.shield()
                elif i[1] == 3:
                    gayka_rain = True
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
                for i in range(9):
                    x = roads[i]
                    enemys.append(Monster(x, f'monster{random.randint(1, 2)}.png', monster_sprites))
                rocket_rain = False
                rocket_rain_begin = False
        clock.tick(FPS)
        pygame.display.update()
        if t == 1:
            t = 0
            pause()
            pygame.event.clear()


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
