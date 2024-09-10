class Customer:
    customer_orders=[]
    def __init__(self,name):
        self.name=name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if type(name)==str and 1<=len(name)<=15: #set customer name to a string of length 1 to 15
            self._name=name
        else:
            raise ValueError

    def orders(self): #returns orders by a specific customer
        return [order for order in Customer.customer_orders  if order.customer==self]

    def coffees(self):#returns a list of unique coffees by a customer
        my_coffees=[order.coffee.name for order in Customer.customer_orders if order.customer==self]
        unique_coffees=[]
        for coffee in my_coffees:
            if coffee not in unique_coffees:
                unique_coffees.append(coffee)
        return unique_coffees

    def create_order(self,coffee,price): #takes in an instance of Coffee and a price and creates & returns an order 
        from order import Order
        return Order(self,coffee,price)

    @classmethod
    def most_aficionado(cls,coffee):#returns customer instance that has spent most money on a coffee instance
        cust_spend={}
        max_value=0 #to store the maximum value in dict 
        max_key=None #to store the key with the maximum value
        from order import Order
        spend_list=[item for item in Order.all if item.coffee==coffee] #list of orders for a coffee instance
        for item in spend_list:
            cust_spend[item.customer.name]=cust_spend.get(item.customer.name,0)+item.price #update a dict to contain spendings of individual unique customers
        for key,value in cust_spend.items(): #loop through the dict to obtain maximum value and corresponding key
            if(value>max_value):
                max_key=key
                max_value=value
        return max_key