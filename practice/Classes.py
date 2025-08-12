#Classes are user defined blueprint and prototypes
#Using function inside a class is a method, syntax for function and methods are same
class Claculator:
    #class variable: The variable declared immediately after the class below is a class variable
    num = 100 #class variables
    '''
    a constructor is a special method called automatically when an object is created from a class.
    It is used to initialize the object’s attributes (variables).
    '''

    # if you don't define anything the default constructor is called
    # below is the syntax how a default constructor looks like
    #As this is called first the parameters will reach the constructor first
    #The parameter must be catched by constructor so they are passed in the constructor
    # self keyword is mandatory for calling variable names into method
    #self is like this keyword in java
    # constructor name should be __init__
    def __init__(self, a, b):
        self.a = a  # This is a instance variable: it is declared as a variable in a constructor
        self.b = b
        print("I'm called first")

    # self keyword is mandatory for calling variable names into method
    def getData(self):
        print("I am now executing as method in class")

    def Sum(self):
        #In python always attach self. to call any variable
        # For class variable: it is always written with self keyword or with the class name Claculator.num
        return self.a + self.b + self.num # OR Claculator.num




#to call a class we create an object of that particular class just like in java but the syntax is different
obj = Claculator(2,3) #Syntax to create objects in python
obj.getData()
print(obj.num)
print(obj.Sum())

#Example 2:
obj1 = Claculator(4, 5)
obj1.getData()
print(obj1.Sum())
#12345