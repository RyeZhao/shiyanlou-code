#下面是要求
#1 程序存放的位置 /home/shiyanlou/calculator.py
#2 程序可以处理 1 个及多个员工工资计算，输出的内容为 1 行或多行，每行内容必须为 工号:税后工资
#3 程序返回的税后工资数字保留两位小数，如果是整数，仍然需要保留xxx.00 这种形式
#4 如果参数数量不准确或者无法转成整数，需要打印 '请在薪资的位置输入数字' 。







import sys

## 定义下面的变量

# 原始收入，获取员工工号和工资，并封装成列表，输入的工号和工资用":"分开，不同员工的工号之间用空格分开
#工资需输入为整数
employee_and_income=sys.argv

# 税后收入
salary = 0

# 应纳税所得额
shouldPay = 0

# 纳税金额
tax = 0

def calculator(num):
    """计算税后薪资的函数，参数为原始收入"""

    # 应纳税所得额为收入减5000
    shouldPay = 0.835*num - 5000

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
    salary=format(num-tax,'.2f')
    # 返回最终收入
    return salary

#打印
if __name__ == "__main__":
    
    if len(employee_and_income[1:]) < 1:
        print("请提供员工工号和薪资。")
        sys.exit(1)

    for item in employee_and_income[1:]:
        parts = item.split(':')
        if len(parts) != 2:
            print("参数格式错误，请使用'工号:薪资'的格式。")
            continue

        id, income_str = parts
        try:
            income = int(income_str)  # 尝试将薪资转换为整数
        except ValueError:
            print("{ }: 请在薪资的位置输入数字".format(id))
            continue
        print("{}:{}".format(id,calculator(income)))

