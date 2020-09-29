from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
    """
    Общий предок всех математических выражений
    """

    @abstractmethod
    def calculate(self):
        """
        Метод вычисляет численное значение выражения

        :return: значение выражения как вещественное число
        """
        pass
