class Shape2DInterface:
    def draw(self): pass


class Shape3DInterface:
    def build(self): pass


class Circle(Shape2DInterface):
    def draw(self):
        print("Circle.draw")


class Square(Shape2DInterface):
    def draw(self):
        print("Square.draw")


class Sphere(Shape3DInterface):
    def draw(self):
        print("Sphere.build")


class Cube(Shape3DInterface):
    def build(self):
        print("Cube.build")



# Abstract Shape Factory
class ShapeFactoryInterface:
    def getShape(sides): pass



# Concrete shape factories
class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, "Bad 2d shape creation, shape not allowed"


class shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        """here sides refers to the number of faces"""

        if sides == 1:
            return Sphere()

        if sides == 6:
            return Cube()

        assert 9, "Bad 3D shape creation: shape not found"



if __name__ == '__main__':
    shape = Shape2DFactory().getShape(1)
    shape.draw()



