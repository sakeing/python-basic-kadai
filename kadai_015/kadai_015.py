class Human:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name)
        print(self.age)


taro = Human('太郎','20')

taro.printinfo()
