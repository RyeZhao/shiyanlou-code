## 定义下面的变量

# 原始收入，获取用户输入，转换为 int
income =int(input("请输入你的原始收入"))

# 税后收入
salary = 0

# 应纳税所得额
shouldPay = 0

# 纳税金额
tax = 0

def calculator(num):
    """计算税后薪资的函数，参数为原始收入"""

    # 应纳税所得额为收入减5000
    shouldPay = num - 5000

    # 用条件判断语句，根据扣税表写出不同薪资的扣税公式
    if shouldPay <= 0:
        tax = 0
    elif 0 < shouldPay <= 3000:
        tax = shouldPay * 0.03
    # 下面的请你补充
    elif shouldPay <= 12000:
        tax = shouldPay * 0.1-210
    elif shouldPay <=25000:
        tax = shouldPay * 0.2-1410
    elif shouldPay <= 35000:
        tax = shouldPay * 0.25-2660
    elif shouldPay <= 55000:
        tax = shouldPay * 0.3-4410
    elif shouldPay <= 80000:
        tax = shouldPay * 0.35-7160
    else:
        tax = shouldPay * 0.45-15160
    # 最终收入为税前收入减去税款，并保留两位小数
    salary=format(income-tax,'.2f')
    # 返回最终收入
    return salary
# 打印
print('你的税后收入是：{}'.format(calculator(income)))