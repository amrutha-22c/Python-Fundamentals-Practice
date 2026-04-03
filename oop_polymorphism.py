# Method Overriding 
class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def show(self):   
        print("This is child class")

obj = Child()
obj.show()


# 
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Dog()
b = Cat()

a.sound()
b.sound()


# example
class Content:
    def play(self):
        print("Playing content")

class Movie(Content):
    def play(self):
        print("Playing Movie")

class Series(Content):
    def play(self):
        print("Playing Series")

c1 = Movie()
c2 = Series()

c1.play()
c2.play()



# example
class Shape:
    def area(self):
        print("Area calculation")

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Rectangle area:", self.l * self.b)

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Circle area:", 3.14 * self.r * self.r)

r = Rectangle(5, 3)
c = Circle(4)

r.area()
c.area()