from werkzeug.security import generate_password_hash, check_password_hash

class User:
    ''' 该类用于创建用户账号
    '''

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)

    def check_email(self, email):
        return self.email == email

    def save_password(self, password):
        '''生成 hash 密码的方法
        '''
        return generate_password_hash(password)

    def check_password(self, password):
        '''检查 hash 密码的方法，返回布尔值
        '''
        return check_password_hash(self.password_hash,password)

def main():
    userList = []  # 创建用户列表
    print('■■■■■■■■■■ 欢迎 ■■■■■■■■■■')
    while True:
        try:
            choose = int(input('''
            请选择：
            1. 注册
            2. 登录
            3. 退出
            '''))
            if choose == 1:
                # 进入注册流程
                print('请输入:')
                name = input('name:')
                email = input('email:')
                password = input('password:')
                newUser = User(name, email, password)
                userList.append(newUser)
                print("注册成功！")

            elif choose == 2:
                # 进入登录流程
                print('请输入:')
                email = input('email:')
                password = input('password:')
                found = False
                for user in userList:
                    if user.check_email(email) and user.check_password(password):
                        print("登录成功！")
                        found = True
                        break
                if not found:
                    print("邮箱或密码错误！")

            elif choose == 3:
                print("退出程序。")
                break

        except ValueError:
            print("请输入有效的选项！")

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()