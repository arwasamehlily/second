#OPEN / CLOSED

from abc import ABC , abstractmethod
class Shape(ABC):
    def __init__(self , shape_type):
        self.shape_type = shape_type
        
    @abstractmethod
    def calculate_area(self) :
        pass

class Circle(Shape):
    def __init__(self , r) :
        super().__init__("circle")
        self.radius = r
        
    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape) :
    def __init__(self , w , h):
        super().__init__("rectangle")
        self.width = w
        self.heigth = h 
        
#L
        