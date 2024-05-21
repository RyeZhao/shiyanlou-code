# -*- coding: utf-8 -*-
import csv
import json

def calculator(num):
    """计算税后薪资的函数，参数为原始收入"""
    # 应纳税所得额为收入减5000
    shouldPay = max(0, num - 5000)

    # 根据税率表计算税款
    if shouldPay <= 3000:
        tax = shouldPay * 0.03
    elif shouldPay <= 12000:
        tax = shouldPay * 0.1 - 210
    elif shouldPay <= 25000:
        tax = shouldPay * 0.2 - 1410
    elif shouldPay <= 35000:
        tax = shouldPay * 0.25 - 2660
    elif shouldPay <= 55000:
        tax = shouldPay * 0.3 - 4410
    elif shouldPay <= 80000:
        tax = shouldPay * 0.35 - 7160
    else:
        tax = shouldPay * 0.45 - 15160

    # 最终收入为税前收入减去税款，并保留两位小数
    salary = format(num - tax, '.2f')
    return salary

def process_employees(file_path):
    id_and_salary_dict = {}

    # 读取员工数据
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                try:
                    employee_id = int(row[0])
                    income = float(row[1])
                    net_salary = calculator(income)
                    id_and_salary_dict[employee_id] = net_salary
                except ValueError:
                    print("输入数据有误，请确保ID为整数且收入为数字。")

    # 将结果写入JSON文件
    with open('usr.json', 'w') as f:
        json.dump(id_and_salary_dict, f)

if __name__ == "__main__":
    process_employees('usr.csv')





        

