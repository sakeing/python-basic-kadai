class Human():

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f'{self.name}は大人です')
        else:
            print(f'{self.name}は大人ではありません')



user1 = Human('太郎',25)
user2 = Human('二郎',18)
user3 = Human('花子',65)
user4 = Human('佐藤',12)
user5 = Human('鈴木',100)

#ここを繰り返しで入れられるようにしたい
users =[user1,user2,user3,user4,user5]

for user in users:
    user.check_adult()
