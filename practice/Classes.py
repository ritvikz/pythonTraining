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
        return "test"

    def Sum(self, c):
        #In python always attach self. to call any variable
        # For class variable: it is always written with self keyword or with the class name Claculator.num
        return self.a + self.b + self.num +c # OR Claculator.num






#to call a class we create an object of that particular class just like in java but the syntax is different
obj = Claculator(2,3) #Syntax to create objects in python
print(obj)
obj.getData() #method
print(obj.a) #attribute
print(obj.num) #attribute
print(obj.Sum(4))



#Example 2:
obj1 = Claculator(4, 5)
obj1.getData()
print(obj1.Sum(8))



#__str__ Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"


p1 = Person("Alice", 25)
print(p1)  # Alice, 25 years old

#Delete Objects
#You can delete an object using del.
p = Person("Alice")
del p
# print(p)  # This would raise an error

#pass Statement
#pass is a placeholder that does nothing. Useful when you want an empty class or function.
class EmptyClass:
    pass


#git test fr