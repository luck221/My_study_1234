"""
Реализация парсера математических выражений по представленной
ниже грамматике

  BNF:
  (https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)

  <expr> ::= <term> + <expr> | <term> - <expr> | <term>
  
  <term> ::= <factor> * <term> | <factor> / <term> | <factor> % <term> | <factor>
  
  <factor> ::= ( <expr> ) | <number>

"""

from Expressions import (
    AddOperation,
    SubtractOperation,
    ModuleOperation,
    MultiplyOperation,
    DivideOperation,
    NumberExpr
)
from .parser_error import ParserError
from .programmer_error import ProgrammerError


def skip_spaces(source, pos):
    """
    Функция пропуска пробелов в исходной строке, начиная с указанной позиции

    :param source: строка с исходным математическим выражением
    :param pos: текущая позиция
    :return: новая позиция
    """
    while pos < len(source) and source[pos] == ' ':
        pos += 1
    return pos


class ExprParser:
    """
    Парсер символа <expr> в представленной грамматике
    """

    @staticmethod
    def is_applicable(source, pos):
        """
        Метод проверяет применим ли символ <expr> к текущей позиции

        :param source: строка с исходным математическим выражением
        :param pos: текущая позиция
        :return: истина, если применим, ложь -- в обратном случае
        """
        return TermParser.is_applicable(source, pos)

    @staticmethod
    def parse(source, pos):
        """
        Метод выполянет разбор исходной строки, начиная с указанной позиции
        и заканчивая концом выражения

        :param source: строка с исходным математическим выражением
        :param pos: текущая позиция
        :return: кортеж (экземпляр :class:`~Expressions.Expression`, новая позиция)
        :raises: ParserError, ProgrammerError
        """
        left, pos = TermParser.parse(source, pos)
        pos = skip_spaces(source, pos)
        if pos == len(source):
            return left, pos

        if source[pos] == '+' or source[pos] == '-':
            op = source[pos]
            pos += 1
            pos = skip_spaces(source, pos)
            if not ExprParser.is_applicable(source, pos):
                raise ParserError(f"Invalid expression at {pos}")

            right, pos = ExprParser.parse(source, pos)

            if op == '+':
                return AddOperation(left, right), pos
            if op == '-':
                return SubtractOperation(left, right), pos

            raise ProgrammerError("Invalid parser state")

        return left, pos


class TermParser:
    """
    Парсер символа <term> в представленной грамматике
    """

    @staticmethod
    def is_applicable(source, pos):
        """
        Метод проверяет применим ли символ <term> к текущей позиции

        :param source: строка с исходным математическим выражением
        :param pos: текущая позиция
        :return: истина, если применим, ложь -- в обратном случае
        """
        return FactorParser.is_applicable(source, pos)

    @staticmethod
    def parse(source, pos):
        """
        Метод выполянет разбор исходной строки, начиная с указанной позиции
        и заканчивая концом выражения

        :param source: строка с исходным математическим выражением
        :param pos: текущая позиция
        :return: кортеж (экземпляр :class:`~Expressions.Expression`, новая позиция)
        :raises: ParserError, ProgrammerError
        """
        left, pos = FactorParser.parse(source, pos)
        pos = skip_spaces(source, pos)
        if pos == len(source):
            return left, pos

        if source[pos] == '*' or source[pos] == '/' or source[pos] == '%':
            op = source[pos]
            pos += 1
            pos = skip_spaces(source, pos)
            if not TermParser.is_applicable(source, pos):
                raise ParserError(f"Invalid term at {pos}")

            right, pos = TermParser.parse(source, pos)

            if op == '*':
                return MultiplyOperation(left, right), pos
            if op == '/':
                return DivideOperation(left, right), pos
            if op == '%':
                return ModuleOperation(left, right), pos 
            raise ProgrammerError("Invalid parser state")

        return left, pos


class FactorParser:
    """
    Парсер символа <factor> в представленной грамматике
    """

    @staticmethod
    def is_applicable(source, pos):
        """
        Метод проверяет применим ли символ <factor> к текущей позиции

        :param source: строка с исходным математическим выражением
        :param pos: текущая позиция
        :return: истина, если применим, ложь -- в обратном случае
        """
        if pos >= len(source):
            return False
        return source[pos] == '(' or NumberParser.is_applicable(source, pos)

    @staticmethod
    def parse(source, pos):
        """
        Метод выполянет разбор исходной строки, начиная с указанной позиции
        и заканчивая концом выражения

        :param source: строка с исходным математическим выражением
        :param pos: текущая позиция
        :return: кортеж (экземпляр :class:`~Expressions.Expression`, новая позиция)
        :raises: ParserError
        """
        if source[pos] == '(':
            pos += 1
            pos = skip_spaces(source, pos)
            if not ExprParser.is_applicable(source, pos):
                raise ParserError(f"Invalid expressions at {pos}")

            expr, pos = ExprParser.parse(source, pos)

            pos = skip_spaces(source, pos)
            if pos == len(source) or source[pos] != ')':
                raise ParserError(f"Expected ) at {pos}")

            pos += 1
            return expr, pos

        return NumberParser.parse(source, pos)


class NumberParser:
    """
    Парсер символа <number> в представленной грамматике
    """

    @staticmethod
    def is_applicable(source, pos):
        """
        Метод проверяет применим ли символ <number> к текущей позиции

        :param source: строка с исходным математическим выражением
        :param pos: текущая позиция
        :return: истина, если применим, ложь -- в обратном случае
        """
        if pos >= len(source):
            return False
        return ord(source[pos]) >= ord('0') and ord(source[pos]) <= ord('9')

    @staticmethod
    def parse(source, pos):
        """
        Метод выполянет разбор исходной строки, начиная с указанной позиции
        и заканчивая концом выражения

        :param source: строка с исходным математическим выражением
        :param pos: текущая позиция
        :return: кортеж (экземпляр :class:`~Expressions.Expression`, новая позиция)
        :raises: ParserError
        """
        start = pos

        while NumberParser.is_applicable(source, pos):
            pos += 1

        if pos < len(source) and source[pos] == '.':
            pos += 1
            if not NumberParser.is_applicable(source, pos):
                raise ParserError(f"Expected digit at {pos}")

            while NumberParser.is_applicable(source, pos):
                pos += 1

        value = float(source[start:pos])
        return NumberExpr(value), pos
