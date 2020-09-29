from .binary_operation import BinaryOperation

class MultiplyOperation(BinaryOperation):
    """
    Операция умножения
    """

    def calculate(self):
        """
        Метод вычисляет численное значение выражения

        :return: значение выражения как вещественное число
        """
        return self._left.calculate() * self._right.calculate()
