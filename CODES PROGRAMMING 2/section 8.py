#class and instance variable
class Employee:
    c_name = "TechCarp"
    
    def __init__(self , n):
        self.name = n
        
e1 = Employee("Arwa") 
e2 = Employee("Lily")

print(e1.c_name) ; print(e2.c_name)

print(Employee.c_name)

print("-" * 20)

Employee.c_name = "NewTechCrop"
print(e1.c_name) 
print(e2.c_name)

print("-" * 20)

e1.c_name = "Test"
print(e1.c_name) 
print(e2.c_name)
print("-" * 20)
########################################
#over ridding : نفس الداله ومتغيرات
class Parent:
    def greet(self):
        print("Hello this parent class !")
        
class Child(Parent):
    def greet(self):
        print("Hello this Child class !")


c1 = Child()
c1.greet()

print("-" * 20)        
###########################################
#over writing
class Parent:
    def greet(self):
        print("Hello this parent class !")
        
class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello this Child class !")
        
c2 = Child()
c2.greet()

print("-" * 20)
#####################################
#over load : اي هو الهدف نفس الداله بس المتغيرات مختلفه
#بتغير هواياتها مش ثابته وتتغير بتغير المتغيرات 
#not supported
def Product(a , b ):
    p = a * b 
    print(p)

def Product(a , b , c):
    p = a * b * c
    print(p)
    
#Product(4, 2) #ERROR
Product(4, 2, 3) #24

print("-" * 20)
#المثال الصح ازاي نعملها 
def add(datatype , *args):
    
    answer = 0
    
    if datatype == "int" : 
        answer ==  0
        
    if datatype == "str" :
        answer  = " "
        
    for x in args:
        answer += x
        
    print(answer)
    
add("int", 5 , 6)


print("-" * 20)
###################################
#@dispatch(int , int)
def product1(f , s , t):
    r = f * s * t
    print(r)
    
#@dispatch(int , int , int)
def product2(f , s , t):
    r = f * s * t
    print(r)
    
#@dispatch(float , float , float)
def product3(f , s , t):
    r = f * s * t
    print(r)
    
product1(3, 5, 7) ; product2(2, 5, 8) ; product3(7, 5, 7)
print("-" * 20)
######################################
# ABC : abstract base class 
from abc import ABC , abstractedmethod

class Shape(ABC):
    @abstractedmethod
    def area(self):
        pass 
    
    @abstractedmethod
    def perimeter(self):
        pass 
    
class Rectangle(Shape):
    def __init__(self , w , h):
        self.width = w
        self.height = h
        
    def area(self):
        return self.width * self.height 
    
    def perimeter(self):
        return 2 * (self.height + self.width)
    
r = Rectangle(4, 8)

print(f"This area {r.area()}")