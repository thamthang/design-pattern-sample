from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Draw a Circle")

class Rectangle(Shape):
    def draw(self):
        print("Draw a Rectangle")

class Square(Shape):
    def draw(self):
        print("Draw a Square")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "square":
            return Square()
        raise ValueError(f"Invalid shape type: {shape_type}")
    
if __name__ == "__main__":
    factory = ShapeFactory()
    shapes = ["circle", "rectangle", "square", "triangle"]

    for shape in shapes:
        try:
            shape_obj = factory.create_shape(shape)
            shape_obj.draw()
        except ValueError as e:
            print(e)