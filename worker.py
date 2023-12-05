from strategy.abs_strategy import AbsStrategy
from strategy.hand_strategy import HandStrategy
from utils import get_strategy_by_strategy_name


class Worker:
    def __init__(self,name,age,strategy_name):
        self.name = name
        self.age = age
        self.strategy_name = self.strategy.name
        self.__strategy = get_strategy_by_strategy_name(strategy_name)


    def work(self):
        self.__strategy.work()

    def set_strategy(self,strategy:AbsStrategy):
        self.__strategy = strategy
        self.strategy_name = strategy.name

    def __str__(self):
        return f"{self.name} {self.age} {self.strategy_name}"
