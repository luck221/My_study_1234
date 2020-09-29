from .expression import Expression

# pylint: disable=abstract-method
class BinaryOperation(Expression):
    """
    Общий предок для бинарных операторов
    """

    def __init__(self, left, right):
        """
        Конструктор
        Обычно наследуется без изменений в классах конкретных операций.

        :param left: левый операнд
        :param right: правый операнд
        """
        self._left = left
        self._right = right
