Coffee Shop - Python OOP Project
This project simulates a simple coffee shop using Object-Oriented Programming (OOP) concepts in Python. It features three primary classes: Customer, Coffee, and Order. These classes model the relationships between customers, the coffees they order, and the orders themselves.

📑 Table of Contents
Project Overview
Features
Project Structure
Installation and Setup
Usage
Classes Overview
Customer
Coffee
Order
Tests
License
Project Overview
In this project, we create a system where customers can order different types of coffee, and these orders are tracked using Python classes. The main classes include:

Customer: Represents a customer of the coffee shop.
Coffee: Represents a type of coffee offered by the shop.
Order: Represents an order placed by a customer for a specific coffee, including the price of the order.
Each class is designed to manage relationships between the objects in a way that mirrors real-world associations between customers, orders, and coffee.

Features
Customer Management: Create and manage customers with unique names.
Coffee Management: Add coffees with fixed names and track the number of times they are ordered.
Order System: Create orders that link customers and coffees together, with pricing details.
Customer and Coffee Relationships: Track which coffees a customer has ordered and vice versa.
Advanced Queries: Get total orders for a coffee, average order price, and the customer who has spent the most on a particular coffee.
Project Structure
bash
Copy code
coffee_shop/
│
├── coffee.py          # Coffee class definition
├── customer.py        # Customer class definition
├── order.py           # Order class definition
├── README.md          # This README file
└── requirements.txt   # Dependencies (if any)


Installation and Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/coffee-shop.git
cd coffee-shop
Create a Virtual Environment: You can create a virtual environment to manage dependencies (if required):

bash
Copy code
python3 -m venv venv
Activate the Virtual Environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install Dependencies: Install the required dependencies (if any) listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
Usage
You can run the project in the terminal by importing the relevant classes (Customer, Coffee, and Order) and interact with them.

Example:
python
Copy code
from customer import Customer
from coffee import Coffee
from order import Order

# Create Customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Create Coffees
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create Orders
order1 = customer1.create_order(coffee1, 4.50)
order2 = customer2.create_order(coffee2, 5.00)

# Check Orders for a Coffee
print(coffee1.orders()) # Output: [<Order object>]
print(coffee1.customers()) # Output: ['Alice']

# Check Orders for a Customer
print(customer1.orders()) # Output: [<Order object>]

# Check Customer's Coffees
print(customer1.coffees()) # Output: ['Latte']
Classes Overview
Customer
Attributes:

name (string): A customer's name must be between 1 and 15 characters long.
Methods:
orders(): Returns a list of all orders placed by the customer.
coffees(): Returns a unique list of all coffees ordered by the customer.
create_order(coffee, price): Creates a new order linking the customer and coffee with the specified price.
most_aficionado(coffee): Class method that returns the customer who has spent the most on a given coffee.
Coffee
Attributes:

name (string): A coffee's name must be at least 3 characters long and cannot be changed after initialization.
Methods:

orders(): Returns a list of all orders for the coffee.
customers(): Returns a unique list of customers who have ordered this coffee.
num_orders(): Returns the total number of times the coffee has been ordered.
average_price(): Returns the average price of the coffee based on its orders.
Order
Attributes:

customer (Customer): The customer who placed the order.
coffee (Coffee): The coffee being ordered.
price (float): The price of the order, which must be between 1.0 and 10.0.
Methods:

Getters and setters for customer, coffee, and price.
Tests
You can manually test the relationships and behavior by creating instances of the Customer, Coffee, and Order classes.

Example Test:
python
Copy code
def test_customer_orders():
    customer = Customer("Eve")
    coffee = Coffee("Cappuccino")
    order = customer.create_order(coffee, 5.00)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.00
You can write and run similar tests to ensure the correctness of your classes and their methods.

License
This project is licensed under the MIT License - see the LICENSE file for details.

