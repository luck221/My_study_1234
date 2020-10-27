from .command import Command
class SimpleMenuItem():
    def __init__(self:SimpleMenuItem, commmand:Command) -> None:
        self.__command = commmand 
    def SimpleMenuItemMethod(self:SimpleMenuItem, number:int, title:str, command:Command):
        pass
    def execute(self:SimpleMenuItem):
        pass
