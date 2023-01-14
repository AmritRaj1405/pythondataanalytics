class Dog:
    def __init__(self, breed, age,weight): #__init__ is used to initialize the object and In self there is a parameters 
        self.breed=breed
        self.age=age
        self.weight=weight
        print("Dog object created")

panther= Dog(breed="German shepherd",age =11 ,weight=30)
tiger = Dog(breed='pug',age=3,weight=15)
blacky=Dog(breed='labrador',age=5,weight=25)

print(panther.breed)
print(tiger.breed)
print(blacky.breed)