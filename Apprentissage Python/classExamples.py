# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack,

from abc import ABC, abstractmethod


class Point:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # equals
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # greater
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # add
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # strings
    def __str__(self):
        return f"({self.x} {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"


point = Point(1, 2)
point.draw()
# print(type(point))
# print(isinstance(point, Point))
print(point.x)
print(point.y)
point.z = 10
print(point.default_color)
print(point.__str__())

another = Point(3, 4)
another.draw()
print(another.default_color)
pointZeroZero = Point.zero()


point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1 == point2)
print(point1 > point2)
print(point1 + point2)


# Custom Containers
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag: str):
        tag = tag.lower()
        # by default return 0 and adds + 1
        self.__tags[tag] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        tag = tag.lower()
        # by default return 0
        return self.__tags.get(tag, 0)

    def __setitem__(self, tag, count):
        tag = tag.lower()
        self.__tags[tag] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("pyThon")
cloud.add('PythOn')
print(cloud["PYThoN"])


##### property getter and setter #####
class Product:
    def __init__(self, price):
        self.price = price

    @property  # property getter using decorator
    def price(self):  # getter
        return self.__price

    @price.setter  # property setter using decorator
    def price(self, value):  # setter
        if value < 0:
            raise ValueError('Price cannot be negative.')
        self.__price = value


product = Product(50)

# product.price = -1  # error


##### inheritance #####
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


m = Mammal()
m.eat()
m.walk()

print(isinstance(m, Mammal))

print(isinstance(m, Animal))

print(isinstance(Animal, object))


# Multiple inheritance
# class Manager(Person, Employee):
#     pass

# Good example of multiple inheritance
class Flyer:
    def fly(self):
        print('flying')


class Swimmer:
    def swim(self):
        print('swimming')


class FlyingFish(Flyer, Swimmer):
    pass


# A good example of inheritance

class InvalidOperationError(Exception):
    pass


# Abstract
class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("reading data from a network.")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")
    pass


stream = MemoryStream()
