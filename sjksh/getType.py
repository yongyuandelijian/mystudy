'''
1 功能说明:传入参数 “行业”，从业人员，资产总额，收入,获取企业规模
2   列顺序: 行业名称	指标名称	计量 单位	大型	中型	小型	微型
    A 农、林、牧、渔业
        营业收入(Y)	万元	Y≥20000	 500≤Y＜20000	 50≤Y＜500	Y＜50
    工业 工业包括采矿业 B，制造业 C，电力、热力、燃气及水生产和供应业 D
        从业人员(X)	人	X≥1000	300≤X＜1000	 20≤X＜300	X＜20
        营业收入(Y)	万元	Y≥40000	2000≤Y＜40000	 300≤Y＜2000	Y＜300
    E 建筑业
        营业收入(Y)	万元	Y≥80000	6000≤Y＜80000	 300≤Y＜6000	Y＜300
        资产总额(Z)	万元	Z≥80000	5000≤Z＜80000	 300≤Z＜5000	Z＜300
    F 51
        批发业	从业人员(X)	人	X≥200	20≤X＜200	 5≤X＜20	X＜5
        营业收入(Y)	万元	Y≥40000	5000≤Y＜40000	1000≤Y＜5000	Y＜1000
    F 52 零售业
        从业人员(X)	人	X≥300	50≤X＜300	10≤X＜50 	X＜10
        营业收入(Y)	万元	Y≥20000	 500≤Y＜20000	100≤Y＜500 	Y＜100
    交通运输业 交通运输业包括 道路运输业 54，水上运输业 55，航空运输业 56，管道运输业 57，多式联运和运输代理业、装卸搬运 58，不包括铁路运输业
        从业人员(X)	人	X≥1000	300≤X＜1000	 20≤X＜300	X＜20
        营业收入(Y)	万元	Y≥30000	3000≤Y＜30000	 200≤Y＜3000	Y＜200
    G 59 仓储业
        从业人员(X)	人	X≥200	100≤X＜200	 20≤X＜100	X＜20
        营业收入(Y)	万元	Y≥30000	1000≤Y＜30000	 100≤Y＜1000	Y＜100
    G 60 邮政业
        从业人员(X)	人	X≥1000	300≤X＜1000	 20≤X＜300	X＜20
        营业收入(Y)	万元	Y≥30000	2000≤Y＜30000	 100≤Y＜2000	Y＜100
    G 61 住宿业
        从业人员(X)	人	X≥300	100≤X＜300 	 10≤X＜100	X＜10
        营业收入(Y)	万元	Y≥10000	2000≤Y＜10000	 100≤Y＜2000	Y＜100
    G 62 餐饮业
        从业人员(X)	人	X≥300	100≤X＜300 	 10≤X＜100	X＜10
        营业收入(Y)	万元	Y≥10000	2000≤Y＜10000	 100≤Y＜2000	Y＜100
    信息传输业 信息传输业包括电信、广播电视和卫星传输服务 63 ，互联网和相关服务 64
        从业人员(X)	人	X≥2000	100≤X＜2000	 10≤X＜100	X＜10
        营业收入(Y)	万元	Y≥100000	 1000≤Y＜100000	 100≤Y＜1000	Y＜100
    65 软件和信息技术服务业
        从业人员(X)	人	X≥300	100≤X＜300 	 10≤X＜100	X＜10
        营业收入(Y)	万元	Y≥10000	1000≤Y＜10000	  50≤Y＜1000	Y＜50
    7010 房地产开发经营
        营业收入(Y)	万元	Y≥200000	 1000≤Y＜200000	 100≤Y＜1000	Y＜100
        资产总额(Z)	万元	Z≥10000	5000≤Z＜10000	2000≤Z＜5000   	Z＜2000
    702 物业管理
        从业人员(X)	人	X≥1000	300≤X＜1000	100≤X＜300 	X＜100
        营业收入(Y)	万元	Y≥5000	1000≤Y＜5000 	 500≤Y＜1000	Y＜500
    L 租赁和商务服务业
        从业人员(X)	人	X≥300	100≤X＜300 	 10≤X＜100	X＜10
        资产总额(Z)	万元	Z≥120000	 8000≤Z＜120000	 100≤Z＜8000	Z＜100
    其他未列明行业 其他未列明行业包括科学研究和技术服务业 M，水利、环境和公共设施管理业 N，居民服务、修理和其他服务业 O，社会工作 Q，文化、体育和娱乐业 R，
    以及房地产中介服务 703，其他房地产业 709 等，不包括自有房地产经营活动
        从业人员(X)	人	X≥300	100≤X＜300 	 10≤X＜100	X＜10
3 同一行业内的指标为并且的关系,从大型到微型判断,如果其中一个指标满足了上一个类型,但是因为不满足其他指标到了下一层,那么这个指标则不在判断,防止漏掉部分数据
4 1.大型、中型和小型企业须同时满足所列指标的下限，否则下划一档；微型企业只须满足所列指标中的一项即可。
5 如果是行业大类或者中类支持模糊判断(当然这样选择也会造成传入不在行业代码表中的代码错误判断,但是这种可能性很低,所以暂时不考虑,后期可以调整)
Author:aaa
Date:20200213
'''


def getType(hy, cyrs=0, zcze=0, yysr=0):  # 参数列表:行业,从业人数,资产总额,营业收入,后面的参数如果没有输入则认为是0,第一个必须输入
    qylx = ''  # 企业类型
    zb1 = 9  # 默认为9从大型到微型一次为1234 如果指标值小于当前等级数字就认为已经审核过
    zb2 = 9

    if hy == "A":
        if yysr >= 20000:
            qylx = "大"
        elif yysr >= 500 and yysr < 20000:
            qylx = "中"
        elif yysr >= 50 and yysr < 500:
            qylx = "小"
        elif yysr < 50:
            qylx = "微"
        return qylx
    elif hy in ("B", "C", "D"):
        # 判断第一个指标
        if cyrs >= 1000:
            zb1 = 1
        elif cyrs >= 300 and cyrs < 1000:
            zb1 = 2
        elif cyrs >= 20 and cyrs < 300:
            zb1 = 3
        elif cyrs < 20:
            zb1 = 4

        # 判断第二个指标
        if yysr >= 40000:
            zb2 = 1
        elif yysr >= 2000 and yysr < 40000:
            zb2 = 2
        elif yysr >= 300 and yysr < 2000:
            zb2 = 3
        elif yysr < 300:
            zb2 = 4
        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx
    elif hy == "E":
        if yysr >= 80000:
            zb1 = 1
        elif yysr >= 6000 and yysr < 80000:
            zb1 = 2
        elif yysr >= 300 and yysr < 6000:
            zb1 = 3
        elif yysr < 300:
            zb1 = 4

        if zcze >= 80000:
            zb2 = 1
        elif zcze >= 5000 and zcze < 80000:
            zb2 = 2
        elif zcze >= 300 and zcze < 5000:
            zb2 = 3
        elif zcze < 300:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx

    elif hy[:2] == "51":
        if cyrs >= 200:
            zb1 = 1
        elif cyrs >= 20 and cyrs < 200:
            zb1 = 2
        elif cyrs >= 5 and cyrs < 20:
            zb1 = 3
        elif cyrs < 5:
            zb1 = 4

        if yysr >= 40000:
            zb2 = 1
        elif yysr >= 5000 and yysr < 40000:
            zb2 = 2
        elif yysr >= 1000 and yysr < 5000:
            zb2 = 3
        elif yysr < 1000:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx

    elif hy[:2] == "52":  # 零售
        if cyrs >= 300:
            zb1 = 1
        elif cyrs >= 50 and cyrs < 300:
            zb1 = 2
        elif cyrs >= 10 and cyrs < 50:
            zb1 = 3
        elif cyrs < 10:
            zb1 = 4

        if yysr >= 20000:
            zb2 = 1
        elif yysr >= 500 and yysr < 20000:
            zb2 = 2
        elif yysr >= 100 and yysr < 500:
            zb2 = 3
        elif yysr < 100:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx
    elif hy[:2] in ("54", "55", "56", "57", "58"):  # 交通运输
        if cyrs >= 1000:
            zb1 = 1
        elif cyrs >= 300 and cyrs < 1000:
            zb1 = 2
        elif cyrs >= 20 and cyrs < 300:
            zb1 = 3
        elif cyrs < 20:
            zb1 = 4

        if yysr >= 30000:
            zb2 = 1
        elif yysr >= 3000 and yysr < 30000:
            zb2 = 2
        elif yysr >= 200 and yysr < 3000:
            zb2 = 3
        elif yysr < 200:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx

    elif hy[:2] == "59":  # 仓储
        if cyrs >= 200:
            zb1 = 1
        elif cyrs >= 200 and cyrs < 300:
            zb1 = 2
        elif cyrs >= 20 and cyrs < 200:
            zb1 = 3
        elif cyrs < 20:
            zb1 = 4

        if yysr >= 30000:
            zb2 = 1
        elif yysr >= 1000 and yysr < 30000:
            zb2 = 2
        elif yysr >= 100 and yysr < 1000:
            zb2 = 3
        elif yysr < 100:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx

    elif hy[:2] == "60":  # 邮政
        if cyrs >= 1000:
            zb1 = 1
        elif cyrs >= 300 and cyrs < 1000:
            zb1 = 2
        elif cyrs >= 20 and cyrs < 300:
            zb1 = 3
        elif cyrs < 20:
            zb1 = 4

        if yysr >= 30000:
            zb2 = 1
        elif yysr >= 2000 and yysr < 30000:
            zb2 = 2
        elif yysr >= 100 and yysr < 2000:
            zb2 = 3
        elif yysr < 100:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx
    elif hy[:2] == "61":  # 住宿
        if cyrs >= 300:
            zb1 = 1
        elif cyrs >= 100 and cyrs < 300:
            zb1 = 2
        elif cyrs >= 10 and cyrs < 100:
            zb1 = 3
        elif cyrs < 10:
            zb1 = 4

        if yysr >= 10000:
            zb2 = 1
        elif yysr >= 2000 and yysr < 10000:
            zb2 = 2
        elif yysr >= 100 and yysr < 2000:
            zb2 = 3
        elif yysr < 100:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx

    elif hy[:2] == "62":  # 餐饮
        if cyrs >= 300:
            zb1 = 1
        elif cyrs >= 100 and cyrs < 300:
            zb1 = 2
        elif cyrs >= 10 and cyrs < 100:
            zb1 = 3
        elif cyrs < 10:
            zb1 = 4

        if yysr >= 10000:
            zb2 = 1
        elif yysr >= 2000 and yysr < 10000:
            zb2 = 2
        elif yysr >= 100 and yysr < 2000:
            zb2 = 3
        elif yysr < 100:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx

    elif hy[:2] in ("63", "64"):  # 信息传输
        if cyrs >= 2000:
            zb1 = 1
        elif cyrs >= 100 and cyrs < 2000:
            zb1 = 2
        elif cyrs >= 10 and cyrs < 100:
            zb1 = 3
        elif cyrs < 10:
            zb1 = 4

        if yysr >= 100000:
            zb2 = 1
        elif yysr >= 1000 and yysr < 10000:
            zb2 = 2
        elif yysr >= 100 and yysr < 1000:
            zb2 = 3
        elif yysr < 100:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx
    elif hy[:2] == "65":  # 软件和信息技术服务业
        if cyrs >= 300:
            zb1 = 1
        elif cyrs >= 100 and cyrs < 300:
            zb1 = 2
        elif cyrs >= 10 and cyrs < 100:
            zb1 = 3
        elif cyrs < 10:
            zb1 = 4

        if yysr >= 10000:
            zb2 = 1
        elif yysr >= 1000 and yysr < 10000:
            zb2 = 2
        elif yysr >= 50 and yysr < 1000:
            zb2 = 3
        elif yysr < 50:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx

    elif hy == "7010":  # 房地产开发经营
        if zcze >= 10000:
            zb1 = 1
        elif zcze >= 5000 and zcze < 10000:
            zb1 = 2
        elif zcze >= 2000 and zcze < 5000:
            zb1 = 3
        elif zcze <= 2000:
            zb1 = 4

        if yysr >= 200000:
            zb2 = 1
        elif yysr >= 1000 and yysr < 200000:
            zb2 = 2
        elif yysr >= 100 and yysr < 1000:
            zb2 = 3
        elif yysr < 100:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx


    elif hy[:3] == "702":  # 物业管理
        if cyrs >= 1000:
            zb1 = 1
        elif cyrs >= 300 and cyrs < 1000:
            zb1 = 2
        elif cyrs >= 100 and cyrs < 300:
            zb1 = 3
        elif cyrs <= 100:
            zb1 = 4

        if yysr >= 5000:
            zb2 = 1
        elif yysr >= 1000 and yysr < 5000:
            zb2 = 2
        elif yysr >= 500 and yysr < 1000:
            zb2 = 3
        elif yysr < 500:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx

    elif hy == "L":  # 租赁和商务服务
        if cyrs >= 300:
            zb1 = 1
        elif cyrs >= 100 and cyrs < 300:
            zb1 = 2
        elif cyrs >= 10 and cyrs < 100:
            zb1 = 3
        elif cyrs <= 10:
            zb1 = 4

        if zcze >= 120000:
            zb2 = 1
        elif zcze >= 8000 and zcze < 120000:
            zb2 = 2
        elif zcze >= 100 and zcze < 8000:
            zb2 = 3
        elif zcze < 100:
            zb2 = 4

        # 等级判定后立刻退出,可以防止因为部分条件不满足上一级导致满足的指标也不满足下一级的判定
        if zb1 == 1 and zb2 == 1:
            qylx = "大"
            return qylx
        elif zb1 <= 2 and zb2 <= 2:
            qylx = "中"
            return qylx
        elif zb1 <= 3 and zb2 <= 3:
            qylx = "小"
            return qylx
        elif zb1 <= 4 and zb2 <= 4:
            qylx = "微"
            return qylx

    elif hy in ("M", "N", "O", "Q", "R") or hy[:3] in ("703", "709"):  # 其他未列明行业
        if cyrs >= 300:
            qylx = "大"
        elif cyrs >= 100 and cyrs < 300:
            qylx = "中"
        elif cyrs >= 10 and cyrs < 100:
            qylx = "小"
        elif cyrs <= 10:
            qylx = "微"
        return qylx
    else:  # 剩余的行业并没有进行说明,先保留代码
        pass


# 测试
if __name__ == '__main__':
    print(getType(hy="M", cyrs=80, yysr=20000))
