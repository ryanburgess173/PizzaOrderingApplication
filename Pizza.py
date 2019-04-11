# Contestant ID: 506
# The Pizza.py class file will hold all of our data for a single pizza.

class Pizza:
    # "Private" access attributes
    # (These aren't really private in the sense of private in Java,
    # as there are no access modifiers in Python.
    # This is simply a way of naming variables that is common in the
    # development community to help identify variables that should be
    # treated as private.)

    # These will be assigned by the class constructor.
    __pizzaSize = None
    __toppings = []
    __crustType = None
    __pizzaShape = None

    # class constructor
    def __init__(self, size, toppings, crust, shape):
        self.__toppings = []
        self.__pizzaSize = size
        self.__toppings = toppings
        self.__crustType = crust
        self.__pizzaShape = shape

    # =========================================================
    # Getters and Setters for the pizza size:
    # =========================================================
    def get_pizza_size(self):
        return self.__pizzaSize

    def set_pizza_size(self, size):
        self.__pizzaSize = size

    # =========================================================

    # ========================================================
    # Getter, setter, and appender for the toppings list:
    # ========================================================
    def get_toppings(self):
        return self.__toppings

    def set_toppings(self, toppings):
        # sets toppings to an empty list
        self.__toppings = []
        # loops through each topping in the toppings list
        for topping in toppings:
            # adds the toppings to the toppings list
            self.__toppings.append(topping)

    # appender method
    def add_toppings(self, toppings):
        for topping in toppings:
            self.__toppings.append(topping)
    # =======================================================

    # =========================================================
    # Getters and Setters for the crust type:
    # =========================================================
    def get_crust_type(self):
        return self.__crustType

    def set_crust_type(self, crust):
        self.__crustType = crust

    # =========================================================

    # =========================================================
    # Getters and Setters for the pizza shape:
    # =========================================================
    def get_pizza_shape(self):
        return self.__pizzaShape

    def set_pizza_shape(self, shape):
        self.__pizzaShape = shape

    # =========================================================
