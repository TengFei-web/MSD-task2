class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, username):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)
                return True
        return False

    def update_password(self, username, new_password):
        for user in self.users:
            if user.username == username:
                user.password = new_password
                return True
        return False

# 创建用户存储库对象
user_repository = UserRepository()

# 添加用户
user1 = User("user1", "password1")
user2 = User("user2", "password2")
user_repository.add_user(user1)
user_repository.add_user(user2)

# 删除用户
user_repository.remove_user("user1")

# 更新用户密码
user_repository.update_password("user2", "new_password")

# 打印所有用户信息
for user in user_repository.users:
    print(f"Username: {user.username}, Password: {user.password}")