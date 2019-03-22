class Dog:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    def ShowName(self):
        print("Dog's name :" + self.name)
    def ShowColor(self):
        print("Dog's color :" + self.color)
small_dog = Dog("black", "kit")
big_dog = Dog("white", "pit")
lazy_dog = Dog("yellow", "zet")

class Carbin_Dog(Dog):
    def __init__(self, run, sit, name):
        self.run = run
        self.sit = sit
        self.name = name
    def status(self):
        print(self.run)
    def ShowName(self):
        print("this CarbinDog's name :"+self.name)
Carbin_Dog_1 = Carbin_Dog("running"," ","alice")
Carbin_Dog_1.status()
Carbin_Dog_1.ShowName()