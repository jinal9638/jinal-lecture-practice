#Abstraction in OOP
'''
abstraction is the process of hiding implementation details and showing only essential features to the user.

reduce complexity
increase secruity
improve code reusability

An abstract class is a class that
cannot be instantiate(object cannot be created directly.)

ABC--> ABTRACT BASE CLASS

IT IS BUILT IN PYTHON MODULE USED TO CREATE ABSTRACT CLASSES.
'''
from abc import ABC,abstractmethod

class animal(ABC):

    @abstractmethod
    def sound(animal):
        pass

class dog(animal):

    def sound(self):
        print("Dog Bow Bow")

dog().sound()

#YOU CANNOT CREATE AN OBJECT OF AN ABSTRACT CLASS

#ABTRACT CLASS AND METHODS

from abc import ABC,abstractmethod

class animal(ABC):

    @abstractmethod
    def sound(animal):
        pass

    def sleep(self):
        print("ANIMAL IS SLEEPING.")

#CHILD CLASS

class dog(animal):

    def sound(self):
        print("Dog Bow Bow")

class cat(animal):

    def sound(self):
        print("Cat Meow Meow")

        
dog().sound()
dog().sleep()
cat().sound()
cat().sleep()

#abtract class shape with area()

from abc import ABC,abstractmethod

class shape(ABC):

    @abstractmethod

    def area(self):
        pass

    @abstractmethod

    def perimeter(self):
        pass

class rectangle(shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

class circle(shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*(self.radius**2)

    def perimeter(self):
        return round(2*3.14*self.radius,2)

r=rectangle(10,5)
c=circle(10)

print("Rectangle Area:",r.area())
print("Rectangle Perimeter:",r.perimeter())
print("Circle area:",c.area())
print("Circle perimeter:",c.perimeter())

#MLMODEL ABSTRACT CLASS

from abc import ABC,abstractmethod

class MLMODEL(ABC):
    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

#LINEAR REGRESSION MODEL

class LINEARREGRESSIONMODEL(MLMODEL):

    def train(self):
        print("TRAINING LINEAR REGRESSION MODEL")

    def predict(self):
        print("PREDICTING USING LINEAR REGRESSION")

class DECISIONTREEMODEL(MLMODEL):

    def train(self):
        print("TRAINING DECISION TREE MODEL")

    def predict(self):
        print("PREDICTING USING DECISION TREE")

LINEARREGRESSIONMODEL().train()
LINEARREGRESSIONMODEL().predict()

DECISIONTREEMODEL().train()
DECISIONTREEMODEL().train()




        
    

    




