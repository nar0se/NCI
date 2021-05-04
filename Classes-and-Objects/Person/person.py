class Person:
    def __init__(self, fname = None, lname = None, age = None, phone = None):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.phone = phone

    def setFirstName(self, fname):
        self.fname = fname
    
    def getFirstName(self):
        return self.fname 
    
    def setLastName(self, lname):
        self.lname = lname
    
    def getLastName(self):
        return self.lname 

    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age 
    
    def setPhone(self, phone):
        self.phone = phone
    
    def getPhone(self):
        return self.phone
    
    def printHello(message):
        print(f'Hi, this is my message: {message}')