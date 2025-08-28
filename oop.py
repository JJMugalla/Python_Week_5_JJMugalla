#use object and classes to structure our code, so that we can use it later.
#ease of maintaining, debugging and reusing the code. Dry code (you do not repeat yourself). Build applications that are reusable. (reuse classes, objects, functions, giving you clear structures, speed and saving time)
#classes are blueprints for creating objects. They encapsulate data and behavior, allowing us to model real-world entities and their interactions.
#create a class,  by giving it functions(def_init), variables (def), etc then create an object. ( object=class(attributes))
class Dog:
    def __init__(self, name, age):#variable
        self.name = name
        self.age = age

    def bark(self):#method
        print("Woof!")
    def move(self, x, y):#method
        print(f"Moving to ({x}, {y})")

#creating an object
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
print(my_dog.bark())  # Output: Woof!

#attributes and methods
#attributes are variables that hold data related to the object. Methods are functions that define the behavior of the object.
#instance variables are attributes that are specific to each instance of a class.
#methods can access and modify the instance variables. methods are used to create behaviors for the objects.