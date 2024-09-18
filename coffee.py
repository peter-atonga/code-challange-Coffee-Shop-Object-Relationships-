class Coffee:
    coffee_orders=[]
    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if hasattr(self,'_name'):
            raise AttributeError("Cannot change the name..") #restricts change of name after the object has been instantiated
        if type(name)==str and len(name)>=3:
            self._name=name
        else:
            raise ValueError


    def orders(self): #returns a list of all orders for that coffee
        return [item for item in Coffee.coffee_orders if item.coffee==self]

    def customers(self):#returns a unique list of customers who ordered a certain coffee
        cust_list=[item.customer.name for item in Coffee.coffee_orders if item.coffee==self]
        unique=[]
        for item in cust_list:
            if item not in unique:
                unique.append(item)
        return unique

    def num_orders(self):#returns the number of times a coffee has been ordered
        return len(self.orders()) #calls the orders method above since it contains a list of all orders for a coffee

    def average_price(self): #returns average price of the coffee based on its orders
        return sum([item.price for item in self.orders()])/self.num_orders()