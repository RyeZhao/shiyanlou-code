import random

def draw_card(num_draws, card_tuple, package):
    """抽卡功能，随机从给定的牌组中抽取指定次数的卡片并添加到背包中。"""
    for _ in range(num_draws):
        card = random.choice(card_tuple)
        package.append(card)
        print(f"你抽到了：{card}")

def view_package(package):
    """查看背包内容。"""
    if package:
        print("背包中的卡片有：", package)
    else:
        print("背包是空的！")

def sort_package(package):
    """整理背包，对背包中的卡片进行排序。"""
    package.sort()
    print("背包已整理。现在的卡片顺序是：", package)

def main():
    card_tuple = ('武则天', '嬴政', '诸葛亮', '宫本武藏', '李白')
    package = []
    while True:
        choose = int(input("请选择你的选项！\n  1.抽卡\n  2.查看背包\n  3.整理背包\n  4.离开\n"))
        if choose == 1:
            num_draws = int(input("输入你希望的抽卡次数："))
            draw_card(num_draws, card_tuple, package)
        elif choose == 2:
            view_package(package)
        elif choose == 3:
            sort_package(package)
        elif choose == 4:
            print("感谢使用，再见！")
            break
        else:
            print("输入有误，请重新输入！")

if __name__ == "__main__":
    main()
