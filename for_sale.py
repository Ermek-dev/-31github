from random import randint
from state.state import State


class ForSaleState(State):
    def raise_price(self):
        print("Успешное повышение цены на продукт")

    def set_up(self):
        print("Продукт не может быть повторно выставлен на торги")

    def give_to_the_winner(self):
        if self.product.price == 0:
            print("Нельзя отдать продукт бесплатно")
        else:
            state_name = "sold"
            self.product.change_state(state_name)

    def set_off(self):
        print("Продукт вернулся на склад")
        state_name = "in_stock"
        self.product.change_state(state_name)
