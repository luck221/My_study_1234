from .parser_impl import (
    skip_spaces,
    ExprParser
)
from .parser_error import ParserError

class Parser:
    """
    Класс разбора математического выражения как строки
    """

    def __init__(self, source):
        """
        Конструктор

        :param source: строка, содержащая математическое выражение
        """
        self.__source = source

    def parse(self):
        """
        Метод преобразует строку, переданную в конструктор,
        в дерево операндов и возвращает корневой элемент.

        :return: корневой элемент дерева операндов
        """
        pos = 0

        pos = skip_spaces(self.__source, pos)
        if not ExprParser.is_applicable(self.__source, pos):
            raise ParserError("Not a valid expression")

        result, pos = ExprParser.parse(self.__source, pos)

        pos = skip_spaces(self.__source, pos)
        if pos != len(self.__source):
            raise ParserError(f"Unexpected symbols at the end of expression after {pos}")

        return result
