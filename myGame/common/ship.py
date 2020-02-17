import pygame

class Ship():
    """负责管理飞船的大部分动作"""
    def __init__(self,screen,setvar):
        """初始化飛船並設置初始位置"""
        self.screen=screen

        # 加载飞船图像并获取外接矩形
        self.image=pygame.image.load(setvar.ship_imgpath)
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        # 将飞船图像放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        # 是否持续移动标志
        self.move_right=False
        self.move_left=False
        self.move_up=False
        self.move_down=False

        self.speed=setvar.ship_speed



    def update(self):
        # 这个rect的上下左右是指飞船的左侧和右侧距分别离屏幕左侧的位置,而不是图像距离屏幕左侧和右侧的位置,top和bottom非别是上面和下面距离屏幕顶部的距离
        # print("飞船的left是{left},right是{right},top是{top},down是{down}".format(left=self.rect.left,right=self.rect.right,top=self.rect.top,down=self.rect.bottom))
        # 屏幕也是同理,左右分别指左右距离屏幕左侧的距离,上下分别指上下距离顶部的距离 屏幕的left是0,right是1200,top是0,down是800
        # print("屏幕的left是{left},right是{right},top是{top},down是{down}".format(left=self.screen_rect.left, right=self.screen_rect.right,top=self.screen_rect.top, down=self.screen_rect.bottom))
        if self.move_right and self.rect.right<self.screen_rect.right:   # 距离左侧的距离小于屏幕的宽度
            # print(self.screen_rect.right,self.rect.right)  # 分别是屏幕最右侧距离,距离屏幕左侧的距离
            self.rect.centerx +=self.speed
        elif self.move_left and self.rect.left>self.screen_rect.left:   # 距离左侧大于0即可
            # print(self.rect.left,self.screen_rect.left)  # 分别为距离屏幕左侧的像素,屏幕最左侧像素
            self.rect.centerx -=self.speed
        elif self.move_up and self.rect.top>self.screen_rect.top:
            self.rect.centery -= self.speed
        elif self.move_down and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery += self.speed

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)