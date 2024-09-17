               Deliverables 

    -Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

        -Initializers and Properties
    Customer
    Customer init(self, name) Customer is initialized with a name Customer property name Returns customer's name Names must be of type str Names must be between 1 and 15 characters, inclusive Should be able to change after the customer is instantiated

        -Coffee
    Coffee init(self, name) Coffee is initialized with a name Coffee property name Returns the coffee's name Names must be of type str Names length must be greater or equal to 3 characters Should not be able to change after the coffee is instantiated hint: hasattr()

        -Order
    Order init(self, customer, coffee, price) Order is initialized with a Customer instance, a Coffee instance, and a price Order property price Returns the price for the order Prices must be of type float Price must be a number between 1.0 and 10.0, inclusive Should not be able to change after the order is instantiated hint: hasattr()

        -Object Relationship Methods and Properties
                    -Order
    Order property customer Returns the customer object for that order Must be of type Customer Order property coffee Returns the coffee object for that order  Must be of type Coffee

        -Coffee
    Coffee orders() Returns a list of all orders for that coffee Orders must be of type Order Coffee customers() Returns a unique list of all customers who have ordered a particular coffee. Customers must be of type Customer

        -Customer
    Customer orders() Returns a list of all orders for that customer Orders must be of type Order Customer coffees() Returns a unique list of all coffees a customer has ordered Coffees must be of type Coffee

        -Aggregate and Association Methods
                - Customer
    Customer create_order(coffee, price) Receives a coffee object and a price number as arguments Creates and returns a new Order instance and associates it with  that customer and the coffee object provided.

                -Coffee
    Coffee num_orders() Returns the total number of times a coffee has been ordered Returns 0 if the coffee has never been ordered Coffee average_price() Returns the average price for a coffee based on its orders Returns 0 if the coffee has never been ordered Reminder: you can calculate the average by adding up all the orders prices and dividing by the number of orders

               - Bonus:
         Aggregate and Association Method
    Customer classmethod most_aficionado(coffee) Receives a coffee object argument Returns the Customer instance that has spent the most money on the coffee instance provided as argument. Returns None if there are no customers for the coffee instance provided. hint: will need a way to remember all Customer objects

                            