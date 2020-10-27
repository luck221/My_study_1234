from .command import Command
from .menu_item import MenuItem
from .simple_menu_item import SimpleMenuItem
class Menu():
    def __init__(self:Menu, number = 0, title = ""  ) -> None:
        self.__number = number
        self.__title  = title
    def setStartupCommand(self:Menu, command:Command):
        command.execute()
    def setBeforeSelectCommand(self:Menu, command:Command):
        command.execute()
    def setTearDownCommand(self:Menu, command : Command):
        command.execute()
    def addItem(self:Menu, title:str, command:Command) -> MenuItem:
        return command.execute()
    def addSubmenu(self:Menu, title:str) -> Menu:
        pass
    def __printMenu(self:Menu):
        """Выводит меню в консоль"""
        print()
    def __select(self:Menu) -> bool:
        pass
    def execute(self:Menu):
        pass
