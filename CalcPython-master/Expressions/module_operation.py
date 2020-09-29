from .binary_operation import BinaryOperation

class ModuleOperation(BinaryOperation):
    """
    Операция остаток от деления
    """

    def calculate(self):
        """
        Метод вычисляет численное значение выражения

        :return: значение выражения как вещественное число
        """
        return self._left.calculate() % self._right.calculate()
