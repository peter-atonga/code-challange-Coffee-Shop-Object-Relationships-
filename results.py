from customer import *
from coffee import *
from order import *

#instances of customers
client1=Customer("client1")
client2=Customer("client2")

#instances of coffee
doppio=Coffee("doppio")
doppio2=Coffee("doppio")

#instances of orders
Order1=Order(client1,doppio,9.0)
order2=Order(client1,doppio,7.8)


print(doppio.orders()) #a list of all orders of that coffee
print(doppio.customers())#returns a list of unique customers who ordered that coffee. 
print(client1.orders()) #list of all orders by a specific customer
print(client1.coffees())#a list of unique coffees ordered by a customer
print(client2.create_order(doppio2,8.5)) #creates an order of latte2 for customer cust2
print(client2.create_order(doppio2,9.8))
print(client2.orders()) #confirm that cust2 now has an order
print(client1.coffees())
print(doppio2.num_orders())#num of times a coffee has been ordered
print(doppio2.average_price()) #average price of a coffee based on its orders
print(Customer.most_aficionado(doppio2)) #customer instance  that has spent most money on the coffee instance --None if no customer