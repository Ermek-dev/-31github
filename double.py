from main import AbstractDoubleSquare,AbsSquare


class Square(AbsSquare):
    def __init__(self,side:int):
        self.side = side

    def get_side(self):
        square_area = self.side
        print(square_area)


    def __add__(self, other):
        if not isinstance(other,(int,Square)):
            raise ArithmeticError("Second operand could be int")
        operand = other
        if isinstance(other,Square):
            operand = other.side
        return Square(self.side*self.side+operand*operand)


class DoubleSquare(AbstractDoubleSquare):
    def get_side(self):
        pass


    def build_double_square(self, square_1: AbsSquare, square_2: AbsSquare):
        pass

    def calculate_area(self):
        pass

    def get_area(self):
        pass


