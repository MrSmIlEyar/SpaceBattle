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

def game_over(gayka_score):
    global score
    record = 0
    with open('data/results.txt', 'r') as f:
        s = list(map(int, f.readlines()))
        if score > s[-1]:
            record = 1
        s.append(score)
        s.sort()
    with open('data/results.txt', 'w') as f:
        for i in s:
            f.write(str(i) + '\n')

def show_menu():
    menu_bg = load_image('Menubg.jpg')
    butn_image = load_image('fonbutn.png')
    image = load_image("cursor.png")
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
            pass
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

    def update(self, v):
        self.rect.y += v
        if self.rect.y >= height - self.image.get_height():
            show_menu()

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


def show_score():
    global score
    font_type = pygame.font.Font(load_font('font.ttf'), 40)
    text_score = font_type.render(str(score), True, (255, 255, 255))
    screen.blit(text_score, (1, 0))
def start_game():
    global running,score,gayka_score, all_gayka_score
    score = 0
    gayka_score = 0
    monster_sprites = pygame.sprite.Group()
    space_ship_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    gaykaim = load_image('gayka.png')
    death_sprites = pygame.sprite.Group()
    meteor_sprites = pygame.sprite.Group()
    bonus_sprites = pygame.sprite.Group()
    space_ship = SpaceShip(space_ship_sprites)
    background = load_image('background.png')
    gayka_sprites = pygame.sprite.Group()
    score = 0
    death = False
    stage_of_death = 1
    death_ship_FPS = 60
    FPS = 50
    v = 99
    t = 1
    v_b = 400
    Meteor.v = 10
    clock = pygame.time.Clock()
    roads = [15, 100, 185, 270, 355, 440, 525, 610, 695]
    enemys = []
    bonuces = []
    shield_on_space_ship = False
    double_bullets = False
    bonuces_on_spaceship = []
    place_for_blit_bonuces_on_spaceship = [[(1, 75), (35, 75)], [(1, 120), (35, 120)], [(1, 165), (35, 165)]]
    name_bonuces = [('bonus_2x.png', 1), ('shild.png', 2)]
    meteor_active = False
    for i in range(9):
        x = roads[i]
        enemys.append(Monster(x, f'monster{random.randint(1, 2)}.png', monster_sprites))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if double_bullets:
                        Bullet((space_ship.ret_x_for_double_bullets_1(), space_ship.ret_y()), bullet_sprites)
                        Bullet((space_ship.ret_x_for_double_bullets_2(), space_ship.ret_y()), bullet_sprites)
                    else:
                        Bullet((space_ship.ret_x(), space_ship.ret_y()), bullet_sprites)
                    bullet_sound.play()
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        space_ship_sprites.update()
        space_ship_sprites.draw(screen)
        monster_sprites.update(v / FPS)
        monster_sprites.draw(screen)
        bullet_sprites.update(v_b / FPS)
        bullet_sprites.draw(screen)
        meteor_sprites.draw(screen)
        meteor_sprites.update()
        gayka_sprites.draw(screen)
        gayka_sprites.update()
        m = list(pygame.sprite.groupcollide(monster_sprites, bullet_sprites, True, True).items())
        for i in range(len(m)):
            score += 1
            Monster(m[i][0].ret_x(), f'monster{random.randint(1, 2)}.png', monster_sprites)
            if score % 10 == 0 and score != 0:
                gayka = Gayka(random.choice(roads), gayka_sprites)
        for i in monster_sprites:
            if pygame.sprite.collide_mask(i, space_ship):
                show_menu()
                break
        show_score()
        screen.blit(gaykaim, (1, 40))
        show_gayka_score()
        if pygame.sprite.groupcollide(gayka_sprites, space_ship_sprites, True, False):
            gayka_score += 1
            all_gayka_score += 1
            with open('data/gaykascore.txt', 'w') as f:
                f.write(str(all_gayka_score))
            if score % 25 == 0 and score != 0:
                meteor = Meteor(random.choice(roads), meteor_sprites)
                meteor_active = True
        if meteor_active:
            xbonus = meteor.x()
            ybonus = meteor.y()
        if pygame.sprite.groupcollide(meteor_sprites, bullet_sprites, True, True):
            name, type_b = random.choice(name_bonuces)
            bon = Bonus(xbonus + 10, ybonus + 10, name, type_b, bonus_sprites)
            meteor_active = False
            bonuces.append((bon, bon.ret_type()))
        bonus_sprites.draw(screen)
        bonus_sprites.update()
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
                    v = 0
                    ship_death(space_ship.x(), space_ship.y(), death_sprites)
                    break
        if death:
            death_sprites.draw(screen)
            death_sprites.update(stage_of_death)
            clock.tick(death_ship_FPS)
            stage_of_death += 1
            if stage_of_death == 15:
                show_menu()
        if pygame.sprite.groupcollide(bullet_sprites, meteor_sprites, True, True):
            pass
        if pygame.sprite.groupcollide(bonus_sprites, space_ship_sprites, True, False):
            pass
        for i in bonuces:
            if pygame.sprite.spritecollide(i[0], space_ship_sprites, False):
                q = time.time()
                w = [j[1] for j in bonuces_on_spaceship]
                if i[1] in w:
                    bonuces_on_spaceship[w.index(i[1])] = (i[0], i[1], q)
                else:
                    bonuces_on_spaceship.append((i[0], i[1], q))
                del bonuces[bonuces.index(i)]
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
                if i[1] == 2:
                    shield_on_space_ship = True
                    space_ship.shield()
                for j in range(len(bonuces_on_spaceship)):
                    screen.blit(bonuces_on_spaceship[j][0].ret_image(), place_for_blit_bonuces_on_spaceship[j][0])
        clock.tick(FPS)
        pygame.display.update()
        if t == 1:
            t = 0
            pause()
            pygame.event.clear()


enemys = []
pos_enemys = []


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


running = True
show_menu()
