# object is an instance of a class

# class Car
  # color
  # year
  # model
  # speed
  # numOfWheel
  # engine
  # numOfSeats

  # BMW -> color, year, model, speed, numOfWheels, engine, numOfSeats
  # Mercedes

class Animal:
    # create a constructor 
    def __init__(self, breed = None, name = None, size = None, age = None, temperament = None):
        self.breed = breed
        self.name = name
        self.size = size 
        self.age = age 
        self.temperament = temperament
    
    # create accessors (getters) and mutators (setters)
    def setBreed(self, breed):
        self.breed = breed
    
    def getBreed(self):
        return self.breed

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setSize(self, size):
        self.size = size
    
    def getSize(self):
        return self.size

    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age

    def setTemperament(self, temperament):
        self.temperament = temperament
    
    def getTemperament(self):
        return self.temperament


# Class Vehicle
# Possible Objects: Car, Truck, Boat, Bus, Plane, Bike, Bicycle
# Possible properties: tires, engine, speed, color, model, make
    
# Class Person
# Possible Objects: Mtagui, Pushpa, Aicha, Daniel, Omer
# Possible properties: height, weight, age, gender, fname, lname