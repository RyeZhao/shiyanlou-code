# -*- coding: utf-8 -*-
import random
import time

def draw_card(num_draws, package):
    """抽卡功能，随机从给定的牌组中抽取指定次数的卡片并添加到背包中。"""
    for _ in range(num_draws):
        card = ret_num()
        package[card]=1+package[card]
        print("你抽到了：{}".format(card))
        time.sleep(0.3)
    print("卡已存入背包")

def view_package(package):
    """查看背包内容。"""
    if package:
        print("嬴政 - 数量：{}".format(package['嬴政']))
        print("诸葛亮 - 数量：{}".format(package['诸葛亮']))
        print("宫本武藏 - 数量：{}".format(package['宫本武藏']))
        print("武则天 - 数量：{}".format(package['武则天']))
        print("李白- 数量：{}".format(package['李白']))
    else:
        print("背包是空的！")

def ret_num():
    n=random.randint(0,185)
    if n < 6:
        return '武则天'
    elif n < 16:
        return '嬴政'
    elif n < 36:
        return '诸葛亮'
    elif n < 86:
        return '宫本武藏'
    else :
        return '李白'


def main():
    package = {'武则天' : 0, '嬴政' : 0, '诸葛亮': 0, '宫本武藏' : 0, '李白' : 0}
    while True:
        choose = int(input("请选择你的选项！\n  1.抽卡\n  2.查看背包\n  3.离开\n"))
        if choose == 1:
            num_draws = int(input("输入你希望的抽卡次数："))
            draw_card(num_draws,  package)
        elif choose == 2:
            view_package(package)
        elif choose == 3:
            print("感谢使用，再见！")
            break
        else:
            print("输入有误，请重新输入！")

if __name__ == "__main__":
    main()
