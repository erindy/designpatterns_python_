class ShapeInterface:
    def draw(self): pass


class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")


class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()

        if type == 'square':
            return Square()

        assert 9, 'Could not find shape ' + type



if __name__=='__main__':
    f = ShapeFactory()
    s = f.getShape('square')
    s.draw()
    print(s)
