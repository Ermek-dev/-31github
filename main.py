class Order:
    def __init__(self,name,price,quantity)->None:
        self.name = name
        self.price = price
        self.quantity = quantity


    def total(self):
        return self.price * self.quantity


order = Order('яблоки',15,12)
print(order.total())