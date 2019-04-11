# Contestant ID: 506

import Pizza
import tkinter as tk
import tkinter.messagebox
import Order


# our main class
class Main:
    pizzas = []

    def __init__(self):
        self.pizzas = []
        # create the window
        self.main_win = tkinter.Tk()
        self.main_win.title("Pizza Ordering Application")
        self.main_win.geometry("340x500")

        # =============================================================================
        # Create frames
        # =============================================================================
        self.top_frame = tkinter.Frame(self.main_win)
        self.upper_mid_frame = tkinter.Frame(self.main_win)
        self.lower_mid_frame = tkinter.Frame(self.main_win)
        self.bottom_frame = tkinter.Frame(self.main_win)
        self.left_bottom_frame = tkinter.Frame(self.bottom_frame)
        self.right_bottom_frame = tkinter.Frame(self.bottom_frame)
        self.bottom2_frame = tkinter.Frame(self.main_win)
        # =============================================================================

        # =============================================================================
        # Create the title and customer name entry
        # =============================================================================
        self.title_label = tkinter.Label(self.top_frame, text="Pizza Order")
        self.enter_name_label = tkinter.Label(self.top_frame, text="Customer Name: ")
        self.input_customer_name = tkinter.Entry(self.top_frame, width=30)
        self.title_label.pack()
        self.enter_name_label.pack(side='left')
        self.input_customer_name.pack(side='left')
        # =============================================================================

        # =============================================================================
        # Create the crust selection radio buttons
        # =============================================================================
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.size_label = tkinter.Label(self.upper_mid_frame, text="Select a Size: ")
        self.rb1 = tkinter.Radiobutton(self.upper_mid_frame, text="Large $15.95", variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.upper_mid_frame, text="Medium $12.95", variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.upper_mid_frame, text="Small $10.95", variable=self.radio_var, value=3)

        self.size_label.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        # =============================================================================

        # =================================================================
        # Checkboxes for toppings
        # =================================================================
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)

        # lable for toppings
        self.toppings_label = tkinter.Label(self.lower_mid_frame, text="Select Your Toppings: ($1.25 Each)")

        # create the checkbox elements
        self.cb1 = tkinter.Checkbutton(self.lower_mid_frame, text="Anchovies", variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.lower_mid_frame, text="Pineapple", variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.lower_mid_frame, text="Mushrooms", variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.lower_mid_frame, text="Tofu", variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.lower_mid_frame, text="Bacon", variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.lower_mid_frame, text="Pepperoni", variable=self.cb_var6)

        self.toppings_label.pack()
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        # =================================================================

        # ====================================================================
        # Pizza Shape
        # ===================================================================
        self.radio_var2 = tkinter.IntVar()
        self.radio_var2.set(1)

        self.shape_label = tkinter.Label(self.left_bottom_frame, text="Select a Shape: ")
        self.shape_rb1 = tkinter.Radiobutton(self.left_bottom_frame, text="Round", variable=self.radio_var2, value=1)
        self.shape_rb2 = tkinter.Radiobutton(self.left_bottom_frame, text="Square", variable=self.radio_var2, value=2)
        self.shape_rb3 = tkinter.Radiobutton(self.left_bottom_frame, text="Triangular", variable=self.radio_var2,
                                             value=3)

        self.shape_label.pack()
        self.shape_rb1.pack()
        self.shape_rb2.pack()
        self.shape_rb3.pack()
        # ====================================================================

        # ====================================================================
        # Pizza Shape
        # ===================================================================
        self.radio_var3 = tkinter.IntVar()
        self.radio_var3.set(1)

        self.crust_label = tkinter.Label(self.right_bottom_frame, text="Select a Shape: ")
        self.crust_rb1 = tkinter.Radiobutton(self.right_bottom_frame, text="Thick", variable=self.radio_var3, value=1)
        self.crust_rb2 = tkinter.Radiobutton(self.right_bottom_frame, text="Thin", variable=self.radio_var3, value=2)

        self.crust_label.pack()
        self.crust_rb1.pack()
        self.crust_rb2.pack()
        # ====================================================================

        # ====================================================================
        # Buttons for the bottom panel
        # ====================================================================
        self.add_to_order_btn = tkinter.Button(self.bottom_frame,
                                               text="Add To Order", command=self.AddToOrder)
        self.calculate_btn = tkinter.Button(self.bottom_frame,
                                            text="Calculate", command=self.Calculate)
        self.reset_btn = tkinter.Button(self.bottom_frame,
                                        text="Start Over", command=self.Reset)
        self.exit_btn = tkinter.Button(self.bottom_frame,
                                       text="Exit", command=self.Exit)
        self.add_to_order_btn.pack()
        self.calculate_btn.pack()
        self.reset_btn.pack()
        self.exit_btn.pack()
        # ====================================================================

        # ============================================================
        # packs all the frames into the main window
        # =============================================================
        self.top_frame.pack()
        self.upper_mid_frame.pack()
        self.lower_mid_frame.pack()
        self.left_bottom_frame.pack(side='left')
        self.right_bottom_frame.pack(side='left')
        self.bottom2_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
        # =============================================================

    def AddToOrder(self):
        # this will hold our toppings:
        toppings = []
        # pizza size is equal to
        size = ""
        shape = ""
        crust = ""

        if self.radio_var.get() == 1:
            size = "Large"
        elif self.radio_var.get() == 2:
            size = "Medium"
        elif self.radio_var.get() == 3:
            size = "Small"
        else:
            # if a size has not been selected, give the user an error message
            tkinter.messagebox.showerror("Error", "Please select a size!")

        if self.cb_var1 == 1:
            toppings.append("Anchovies")
        if self.cb_var2 == 1:
            toppings.append("Pineapple")
        if self.cb_var3 == 1:
            toppings.append("Mushrooms")
        if self.cb_var4 == 1:
            toppings.append("Tofu")
        if self.cb_var5 == 1:
            toppings.append("Bacon")
        if self.cb_var6 == 1:
            toppings.append("Pepperoni")

        if self.radio_var2.get() == 1:
            shape = "Round"
        elif self.radio_var2.get() == 2:
            shape = "Square"
        elif self.radio_var2.get() == 3:
            shape = "Triangular"
        else:
            # if a size has not been selected, give the user an error message
            tkinter.messagebox.showerror("Error", "Please select a shape!")

        if self.radio_var3.get() == 1:
            crust = "Thick"
        elif self.radio_var3.get() == 2:
            crust = "Thin"
        else:
            # if a size has not been selected, give the user an error message
            tkinter.messagebox.showerror("Error", "Please select a crust!")

        # adds a new pizza object to our pizza list
        self.pizzas.append(Pizza.Pizza(size, toppings, crust, shape))

    # Makes an order and receipt
    def Calculate(self):
        order1 = Order.Order(self.input_customer_name.get(), self.pizzas)
        self.GenerateReceipt(order1)

    # Resets all
    def Reset(self):
        self.radio_var.set(1)
        self.radio_var2.set(1)
        self.radio_var3.set(1)
        self.pizzas = []
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)

    def Exit(self):
        tkinter.messagebox.showinfo("Goodbye!", "Thank you for using the pizza ordering application!")
        exit()

    # Generates our receipt
    @staticmethod
    def GenerateReceipt(order1):
        title = "Transaction Receipt"
        message = ""
        pizzaCounter = 1
        for pizza in order1.get_pizzas_ordered():
            message += "Pizza:" + str(pizzaCounter) + "\n"
            message += pizza.get_pizza_size()
            message += "\n"
            for topping in pizza.get_toppings():
                message += "--" + topping
                message += "\n"
            message += pizza.get_crust_type() + " Crust"
            message += "\n"
            message += pizza.get_pizza_shape() + " Pizza Shape"
            message += "\n"
            message += "=========================="
            message += "\n"
            pizzaCounter += 1

        message += "Subtotal...: $" + str(order1.get_price())
        message += "\n"
        message += "Sales-Tax..: $" + str(order1.get_sales_tax())
        message += "\n"
        message += "Total......: $" + str(order1.get_total())
        message += "\n"

        tkinter.messagebox.showinfo(title, message)


main = Main()
