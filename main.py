import pygame
from Plane_Sprites import *

class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE.size)
        pygame.display.set_caption("Planes battle  Ver 1.0 by 几把战")
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(PLANE_TIME_EVENT, 1000) # 设置子弹和敌机的定时器事件
        pygame.time.set_timer(BULLENT_TIME_EVENT, 500)
        self.__creat__sprite()  # 初始化精灵组

    def __creat__sprite(self):
        self.plane = Player_Plane()
        backgroud1 = Backgroud()
        backgroud2 = Backgroud(is_creat=True)
        self.backgroud_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.plane_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.backgroud_group.add(backgroud1,backgroud2)
        self.plane_group.add(self.plane)

    def start_game(self):

        while True:
            self.clock.tick(FRAME_RITE)
            self.__check_event() # 监听事件
            self.__collision_event() # 碰撞检测
            self.__update_group()  # 更新精灵组
            self.__game_over() # 根据游戏事件结束游戏
            pygame.display.update()

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    exit()


    def __check_event(self):
        for events in pygame.event.get():
            if events.type == PLANE_TIME_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif events.type == BULLENT_TIME_EVENT:
                bullet = Bullet(self.plane) #
                self.bullet_group.add(bullet)

        key_tuple = pygame.key.get_pressed()
        if key_tuple[pygame.K_RIGHT]:
            self.plane.speed = 2
        elif key_tuple[pygame.K_LEFT]:
            self.plane.speed = -2
        else:
            self.plane.speed = 0

    def __collision_event(self):
        pass


    def __update_group(self):
        self.backgroud_group.update()
        self.backgroud_group.draw(self.screen)
        self.plane_group.update()
        self.plane_group.draw(self.screen)
        self.bullet_group.update()
        self.bullet_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)


    @staticmethod
    def __game_over():
        pass

if __name__ == '__main__':
    pygame.init()
    game = PlaneGame()
    game.start_game()
    













