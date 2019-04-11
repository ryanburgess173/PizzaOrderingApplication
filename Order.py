# Contestant ID: 506
# The Order.py class file will hold all of our order data including a list of Pizza objects.

import tkinter


class Order:
    # "private" properties for this class:

    # Holds the customer's name
    __customerName = ""

    # this will hold Pizza objects
    __pizzasOrdered = []

    # These are variables that give us prices for different items.
    __largePrice = 15.95
    __mediumPrice = 12.95
    __smallPrice = 10.95
    __toppingPrice = 1.25
    __salesTaxRate = 0.065  # assumes sales tax is 6.5%

    # These will be determined by methods in this class.
    # These methods will be called inside the constructor.
    __price = 0.0
    __salesTax = 0.0
    __total = 0.0

    # Class constructor
    def __init__(self, customer_name, pizzas):
        self.__customerName = customer_name
        for pizza in pizzas:
            self.__pizzasOrdered.append(pizza)
        self.calculate_price()
        self.calculate_sales_tax()
        self.calculate_total()

    # ===============================================================================================
    # Price calculator method:
    # ===============================================================================================
    def calculate_price(self):
        # Counter will hold onto what pizza the loop is currently on,
        # that way if an error occurs in the order, we can tell the user
        # which pizza the problem occurred on.
        counter = 1
        # loops through every pizza in our __pizzasOrdered list
        for pizza in self.__pizzasOrdered:
            # if size is large
            if pizza.get_pizza_size() == "Large":
                self.__price += self.__largePrice
            # if size is medium
            elif pizza.get_pizza_size() == "Medium":
                self.__price += self.__mediumPrice
            # if size is small
            elif pizza.get_pizza_size() == "Small":
                self.__price += self.__smallPrice
            # otherwise, throw an error message to the user
            else:
                print("No crust size for pizza #" + str(counter) + " selected!")
            # increments counter
            counter += 1

            # Loop through each of the toppings in each of the pizzas
            # and add $1.25 to the price for each pizza.
            toppingCounter = 1
            for topping in pizza.get_toppings():
                self.__price += self.__toppingPrice
                toppingCounter += 1

    # ===============================================================================================

    # ===============================================================================================
    # Calculate sales tax:
    # ===============================================================================================
    def calculate_sales_tax(self):
        self.__salesTax = self.__price * self.__salesTaxRate

    # ===============================================================================================

    # ===============================================================================================
    # Calculate total:
    # ===============================================================================================
    def calculate_total(self):
        self.__total = self.__price + self.__salesTax

    # ===============================================================================================

    # ===============================================================================================
    # Getter and Setter for the total price:
    # ===============================================================================================
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    # ===============================================================================================

    # ===============================================================================================
    # Getter and Setter for the sales tax:
    # ===============================================================================================
    def get_sales_tax(self):
        return self.__salesTax

    def set_sales_tax(self, tax):
        self.__salesTax = tax

    # ===============================================================================================

    # ===============================================================================================
    # Getter and Setter for the total order cost:
    # ===============================================================================================
    def get_total(self):
        return self.__total

    def set_total(self, t):
        self.__total = t
    # ===============================================================================================

    def get_pizzas_ordered(self):
        return self.__pizzasOrdered