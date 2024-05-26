from werkzeug.security import generate_password_hash, check_password_hash

class Permission:
    '''用户身份类，每个用户在创建的时候都会有对应的身份和权限
    '''

    ROLE_USER = 10        # 普通用户
    ROLE_FORUMADMIN = 20  # 监督员，负责监督用户的博客及评论
    ROLE_ADMIN = 30       # 管理员，拥有最高权限


class User:
    ''' 该类用于创建用户账号
    '''

    # 初始化方法中需要定义用户的身份
    # TODO 默认用户身份为普通用户
    def __init__(self,name,email,password,root_level=Permission.ROLE_USER):
        self.name=name
        self.email=email
        self.password_hash=self.save_password(password)
        self.root_level=root_level


    # 创建哈希密码，该方法前一个挑战已完成，本次挑战不涉及
    def save_password(self, password):
        return generate_password_hash(password)

    # 验证密码，该方法前一个挑战已完成，本次挑战不涉及
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # TODO 定义 is_admin 方法判断用户是否具有管理员权限，参考下面 main 中的使用
    # 要求该方法可以像调用属性一样调用（使用 property 装饰器）
    @property
    def is_admin(self):
        return self.root_level == 30


    # TODO 定义修改用户角色的方法 change_role，参考下面 main 中的使用
    def change_role(self,new_root_leval):
        self.root_level=new_root_leval

        

# 该方法用于验证大家补充的代码功能是否能够正常使用
def main():
    # 创建一个普通用户，无需提供角色参数，使用默认值
    user1 = User('James', 'james@haha.com', '123456')
    # 创建一个管理员用户
    user2 = User('Admin', 'admin@haha.com', '123456', Permission.ROLE_ADMIN)
    # 判断他们是不是管理员
    for user in (user1, user2):
        if user.is_admin:
            print('{} 是管理员'.format(user.name))
        else:
            print('{} 不是管理员'.format(user.name))
            print('现在的权限等级：{}'.format(user.root_level))
            # 不是管理员的话，使用前面定义的方法将其角色修改为管理员
            user.change_role(Permission.ROLE_ADMIN)
            print('修改角色后，{} 变成管理员'.format(user.name))
            print('修改后的权限等级：{}'.format(user.root_level))


if __name__ == '__main__':
    main()