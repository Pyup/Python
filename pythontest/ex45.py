## Animal is-a object (yes, sort of confusing) Look at the extra credit

class Animal(object):
    pass

## Dog is an Animal
class Dog(Animal):
    def __init__(self, name):
        # set the "name" attribute of a Dog instance
        self.__name = name 
    def print_name(self):
        print "In the print of Dog"
        print "%s" % self.__name

    def set_name(self, name):
        self.__name = name

## Cat is also an Animal
class Cat(Animal):
    def __init__(self, name):
        # set the "name" attribute of a Cat instance
        self.__name = name

    def print_name(self):
        print "In the print of Cat"
        print "%s" % self.__name

    def set_name(self, name):
        self.__name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        # set the "name" attribute of a Person instance
        self.name = name
        # Person has-a pef of some kind
        self.pet = None
        print "In the Person__init__ %s" % self.name 

    def print_name(self):
        print "%s" % self.name    

    def print_pet_name(self):
        self.pet.set_name("Cassie")
        self.pet.print_name()
        
## Employee is-a person:
class Employee(Person):
    def __init__(self, name, salary):
        ## set the "name" attribute of father instance
        super(Employee, self).__init__(name)
        ## Employee has-a attribute salary
        self.salary = salary
        print "In the Employee __init__ %s" % self.name

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")
mary.print_name()

## mary's pet a Cat "satan"
mary.pet = satan
mary.print_pet_name()

## frank is an Employee
frank = Employee("Frank", 120000)
frank.print_name()

## frank's pet is Dog "rover"
frank.pet = rover
frank.print_pet_name()

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halbut
harry = Halibut()
