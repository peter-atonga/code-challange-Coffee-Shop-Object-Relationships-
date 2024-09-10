from coffee import *
from customer import *
class Order:

    all=[]
    def __init__(self,customer,coffee,price):
        self.customer=customer
        self.coffee=coffee
        self.price=price
        Order.all.append(self)
        Coffee.coffee_orders.append(self)
        Customer.customer_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self,customers):
        if isinstance(customers,Customer):
            self._customer=customers


    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self,coffee):

        if isinstance(coffee,Coffee):
            self._coffee=coffee
        else:
            raise ValueError(f"{coffee} is not an instance of Coffee class.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,price):
        if hasattr(self,"_price"):
            raise AttributeError
        if type(price)==float and 1.0<=price<=10.0:
            self._price=price



# customer1=Customer("cust1")
# latte=Coffee("latte")

# print([item.coffee for item in Coffee.coffee_orders])
# print(Coffee.all_instances)
# print(item for item in Coffee.all_instances if item==latte)