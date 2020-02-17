import pygame
import random
from pygame.sprite import Sprite

class Wxr(Sprite):
    """负责管理外星人的类"""
    def __init__(self,screen,setvar):
        super().__init__()
        self.screen = screen

        # 加载外星人图像并获取外接矩形
        self.image = pygame.image.load(setvar.wxr_imgpath)  # 加载外星人图片
        self.rect = self.image.get_rect()   # 获取图像的坐标距离
        self.screen_rect = screen.get_rect()

        # 初始位置,在屏幕顶端的一个随机位置
        self.rect.x = self.screen_rect.right-random.randint(0,self.screen_rect.right)
        self.rect.y = self.screen_rect.top

        self.speed = setvar.wxr_speed

    def update(self):
        """位置不断的向下移动"""
        print(self.rect.top)
        self.rect.top += self.speed


    def draw_wxr(self):
        """让外星人显示出来"""
        self.screen.blit(self.image,self.rect)

