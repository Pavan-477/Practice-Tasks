
class Dog:
    def __init__(self,name,age,coat_color):
      self.name=name
      self.age=age
      self.coat_color=coat_color

    def description(self):
        print('Dog name  is ',self.name)
        print('Dog age  is ',self.age)
    
    def get_info(self):
        print('Coat color is ',self.coat_color)


class JackRussellTerrier(Dog):
    legs=4
    eyecolor='black'
    def eyes(self):
        print("Eye color is ",self.eyecolor)
    
    def walky(self):
        print("Total legs are",self.legs,"And a happy tail")


class Bulldog(Dog):
    legs=4
    eyecolor='pitch black'
    def eye_balls(self):
        print("Eye color is ",self.eyecolor)
    
    def walk(self):
        print("Total legs are ",self.legs,'And a happy tail')

dog1=JackRussellTerrier('Snoopy',5,'brown')
dog1.description()
dog1.get_info()
dog1.eyes()
dog1.walky()

print("*"*50)

dog2=Bulldog('Gymson',6,'beige')
dog2.description()
dog2.get_info()
dog2.eye_balls()
dog2.walk()

