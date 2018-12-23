import random
import pygame

SCREEN_SIZE = pygame.Rect(0,0,480,700) # 设置屏幕大小常量
FRAME_RITE = 70 # 设置帧率常量
PLANE_TIME_EVENT = pygame.USEREVENT # 敌机定时器常量
BULLENT_TIME_EVENT = pygame.USEREVENT + 1 # 子弹定时器常量


class PlaneSprites(pygame.sprite.Sprite):
    def __init__(self, image_path, seppd=1):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = seppd
        super().__init__()

    def update(self):
        self.rect.y += self.speed


class Backgroud(PlaneSprites):
    def __init__(self,is_creat=False):
        super().__init__(r"G:\01.python核心编程(共537集)\飞机大战\images\background.png")
        if is_creat is True:
            self.rect.bottom = 0

    def update(self):
        super().update()
        if self.rect.y == self.rect.height:
            self.rect.bottom = 0

class Enemy(PlaneSprites):
    def __init__(self):
        super().__init__(r"G:\01.python核心编程(共537集)\飞机大战\images\enemy1.png")
        self.speed = random.randint(1,3)
        Max_x = SCREEN_SIZE.width - self.rect.width
        self.rect.x = random.randint(0,Max_x)

    def update(self):
        super().update()

        if self.rect.y == SCREEN_SIZE.height:
            self.kill()

class Player_Plane(PlaneSprites):
    def __init__(self):
        super().__init__(r"G:\01.python核心编程(共537集)\飞机大战\images\me1.png",0)
        self.rect.centerx = SCREEN_SIZE.centerx # 初始化玩家飞机位置
        self.rect.y = SCREEN_SIZE.bottom - 120

    def update(self):
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_SIZE.width:
            self.rect.right = SCREEN_SIZE.width

class Bullet(PlaneSprites):
    def __init__(self, player_plane):
        super().__init__(r"G:\01.python核心编程(共537集)\飞机大战\images\bullet1.png",-2)
        self.rect.x = player_plane.rect.centerx
        self.rect.y = player_plane.rect.y - self.rect.height

    def update(self):
        super().update()
        if self.rect.bottom == 0:
            self.kill()















