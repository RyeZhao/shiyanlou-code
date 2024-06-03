import pandas as pd

file_path = ".\\user_study.json"

def analysis(file=None, user_id=None):
    '''
    补充代码：
    1. 使用 Pandas 读取数据
    2. 使用 Pandas 选择数据
    '''
    times = 0
    minutes = 0
    if file and user_id:
        df = pd.read_json(file)
    else:
        return times, minutes
    
    user_data = df[df['user_id'] == user_id]
    times = df[df['user_id'] == user_id].shape[0]
    minutes = user_data['minutes'].sum()
    
    return times, minutes

if __name__ == '__main__':
    user_id=int(input('输入你想筛选的用户名称:'))
    a, b = analysis(file_path, user_id)
    print(a)
    print(b)



    