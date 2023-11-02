### TODO:

# write a Pants class
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28

### TODO: Declare the Pants Class
class Pants:
    def __init__(self, Pants_color, Pants_waist_size, Pants_length, Pants_price):
        self.color = Pants_color
        self.waist_size = Pants_waist_size
        self.length = Pants_length
        self.price = Pants_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        discounted_price = self.price - (self.price * discount)
        return discounted_price
### TODO: write an __init__ function to initialize the attributes

### TODO: write a change_price method:
#    Args:
#        new_price (float): the new price of the shirt
#    Returns:
#        None

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount.
#            For example 0.05 for a 5% discount.
#
#    Returns:
#        float: the discounted price