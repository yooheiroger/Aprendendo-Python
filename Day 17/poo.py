class User:
    def __init__(self,user_id,username,user_age,user_sex):
        self.id  = user_id
        self.username = username
        self.age = user_age
        self.sex = user_sex
        self.nickname = 'nickname'
        self.follower = 0
        self.following = 0

    def follow(self,user):
        user.follower += 1
        self.following += 1

    def show_atributtes(self,user):
        print('name: ' + user.username,'ID: ' + user.id,'Age', user.age,'Sex: '+ user.sex,'Followers' , user.follower,'Following', user.following)


user1 = User('001','Yoohei', 31,'M')
user2 = User('002','Mariana', 33, 'F')

# print(user1.username)
# print(user1.id)
# user1.nickname = 'Abc'
# print(user1.nickname)

user1.follow(user2  )
print(user1.show_atributtes(user1))
print(user2.show_atributtes(user2))