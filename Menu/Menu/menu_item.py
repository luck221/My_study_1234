from abc import ABCMeta , abstractmethod
class MenuItem(metaclass = ABCMeta):
    def __init__(self:MenuItem, number:int , title:str) -> None:
        self.__number = number
        self.__title  = title

    def getNumber(self) -> int:    
        return self.__number
    
    def getTitle(self) -> str:
        return self.__title

    def print(self) -> None:
        print(f"{self.__number}.{self.__title}")

    @abstractmethod
    def execute(self) -> None:
        pass 