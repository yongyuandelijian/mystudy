import pygame
from pygame.sprite import Sprite  # 可以讲游戏中相关的元素进行编组,也就是子弹始终从飞船的位置发出,也就是一次操作一组元素

class Zidan(Sprite):
    """对发射子弹进行管理"""

    def __init__(self,ship,setvar,screen):
        """在飞船所处的位置创建一个子弹的对象"""
        super().__init__()  # 初始化一个父类也就是精灵类
        self.screen=screen  # 子弹和飞船使用同一屏幕

        self.rect=pygame.Rect(0,0,setvar.zd_width,setvar.zd_height) # 在左上角先初始化一个子弹
        # 这个设置可以感觉到是从飞船内部中间的顶部出现
        self.rect.centerx=ship.rect.centerx # 左右距离左侧的位置和飞船保持一致
        self.rect.top=ship.rect.top # 上部位置和飞船也保持一致

        # 使用小数来存储子弹的上下位置,以方便后期进行微量调整速度
        self.y=float(self.rect.y)

        self.color=setvar.zd_yanse
        self.speed=setvar.zd_speed

    def update(self):
        """不断更新子弹的位置,也就是不断向上"""
        self.rect.y -= self.speed

    def draw_zidan(self):
        """显示子弹,也就是在屏幕上绘画子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)


