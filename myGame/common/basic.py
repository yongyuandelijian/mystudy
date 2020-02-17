import sys
import pygame
from pygame.sprite import Group


from common.Settings import Settings
from common.ship import Ship
from common.zidan import Zidan
from common.wxr import Wxr


def check_event(ship,setvar,screen,zidans):
    """捕捉键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_q:
                sys.exit()
            if event.key == pygame.K_RIGHT:
                ship.move_right=True
            elif event.key==pygame.K_LEFT:
                ship.move_left =True
            elif event.key==pygame.K_UP:
                ship.move_up=True
            elif event.key==pygame.K_DOWN:
                ship.move_down=True
            # 支持移动方向的同时也开火
            if event.key==pygame.K_SPACE:
                new_zidan=Zidan(ship,setvar,screen)
                zidans.add(new_zidan)
        elif event.type == pygame.KEYUP:
            ship.move_right=False
            ship.move_left=False
            ship.move_up=False
            ship.move_down=False


def update_screen(ship,screen,setvar,zidans,wxrs):
    """更新屏幕显示"""
    # 每次循环时都重新绘制屏幕
    screen.fill(setvar.bg_color)  # 方法只接受一个参数,一种颜色
    ship.blitme()  # 绘制飞船
    wxrs.draw(screen) # 调用编组的绘制方法,会绘制每个外星人

    for zidan in zidans.sprites():
        zidan.draw_zidan() # 调动每个子弹的绘制方法

    # 让绘制的屏幕可见
    pygame.display.flip()

def update_zidan(zidans):
    """更新子弹位置并删除飞出界面的子弹"""
    zidans.update()  # 更新整个子弹编组
    # 删除子弹
    for zidan in zidans:
        # print(zidan.rect.bottom)   从位置可以看到,为0进行删除
        if zidan.rect.top <= 0:
            zidans.remove(zidan)

def update_wxr(wxrs):
    """更新外星人的位置"""
    wxrs.update()
    # 删除击中或者到达了屏幕底部的外星人
    for wxr in wxrs:
        print(111)
        print(wxr.rect.top)
        if wxr.rect.bottom<=0:
            wxrs.remove(wxr)

def create_wxrq(setvar,screen,wxrs):
    """创建外星人群"""
    # 计算最多可以一行放几个外星人,然后生成一队随机整数的外星人





def run_ganme():
    """运行游戏的主方法"""
    setvar = Settings()  # 初始化参数
    pygame.init()  # 初始化背景设置
    screen = pygame.display.set_mode((setvar.screen_width, setvar.screen_height))  # 创建显示窗口
    pygame.display.set_caption("最炫酷的游戏(按Q退出)")
    ship = Ship(screen,setvar)  #初始化一个主角对象
    # wxr=Wxr(screen,setvar)
    # 创建一个用于存储子弹的编组
    zidans=Group()
    wxrs=Group()  # 创建外星人编组
    create_wxrq(setvar,screen,wxrs)

    # 开始游戏的主循环
    while True:

        '''监视键盘和鼠标事件'''
        check_event(ship,setvar,screen,zidans)

        ship.update()  # 根据键盘事件更新位置

        update_zidan(zidans) # 更新子弹

        # update_wxr(wxrs) # 更新外星人位置

        update_screen(ship, screen, setvar, zidans,wxrs)  # 更新屏幕显示

if __name__ == '__main__':
    run_ganme()