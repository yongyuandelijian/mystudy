class Settings():
    """存储游戏的所有设置类"""
    def __init__(self):
        """初始化游戏设置"""

        # 屏幕的一些设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(128,120,112)   # 设置游戏背景颜色 # RGB颜色0-255  三个换着255分别颜色是红绿蓝

        # 飞船的一些设置
        self.ship_speed = 1.5  # 飞船的移动速度
        self.ship_imgpath="../images/ship.png"  # 飞船的图片路径

        # 初始化子弹的设置
        self.zd_speed=0.1   # 子弹的速度比飞船稍微低一些
        self.zd_width=5   # 宽度为3个像素
        self.zd_height=10 # 高度为10个像素
        self.zd_yanse=(60,60,60)  # 子弹颜色

        # 外星人设置
        self.wxr_imgpath="../images/wxr_ez.png" # 外星人的图片位置
        self.wxr_speed=0.1  # 外星人移动速度




