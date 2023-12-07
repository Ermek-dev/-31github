from constants import STATE_NAMES
from utils import get_by_state

class Product:
    def __init__(self,id:int,name:str,price:int,honorary_code:None, state:"str"):
        # _state_name =
        self.id = id
        self.name = name
        self.price = price
        self.honorary_code = honorary_code
        self.state = state
        self.state_name = get_by_state(state)
        self.state_name.set_product(self)


    def change_state(self,state:str):
        self.state_name = get_by_state(state)
        self.state = state
        self.state_name.set_product(self)


    def raise_price(self):
        self.price+=100
        self.state_name.raise_price()


    def set_up(self):
        self.state_name.set_up()


    def set_off(self):
        self.state_name.set_off()


    def give_to_the_winner(self):
        self.state_name.give_to_the_winner()


    def __str__(self):
        return f"{self.id:3} | {self.name:15} | {self.price:15} | {self.honorary_code:15} | {STATE_NAMES.get(self.state)}"