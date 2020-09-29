from .expression import Expression

class NumberExpr(Expression):
    """
    Числовая константа как математическое выражение
    """

    def __init__(self, value):
        """
        Конструктор

        :param value: значение числовой константы
        """
        self.__value = value

    def calculate(self):
        """
        Метод вычисляет численное значение выражения

        :return: значение выражения как вещественное число
        """
        return self.__value
