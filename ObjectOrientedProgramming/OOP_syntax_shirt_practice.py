class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        """
        INPUT:
        color - string - color of shirt
        size - int - size of shirt
        style - string - style of shirt
        price - int - price of shirt

        OUPUT:
        """
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    def change_price(self, new_price):
        """
        Change price of shirt with new price.
        INPUT:
        new_price - int - price for shirt. 

        OUPUT:
        """
        self.price = new_price
    
    def discount(self, discount):
        """
        A function that provides discount on the shirt item.
        INPUT:
        
        OUPUT:       
        discount - int - discount for the shirt

        """            
        return self.price * (1 - discount)


if __name__ == "__main__":
    
    # Question 1: 
    #   - inssantiate a shirt object with the following characterstics
    #   - color: red, size: 5, style: long-sleeve, price: 25  
    #    - store the  object in variable called shirt_one

    shirt_one = Shirt('red', 'S', 'long-sleeve', 25)

    # Question 2:
    #     - print the price of the shirt using the price attribute
    #     - change the price of the shirt to be 10
    #     - print the price of the shirt using the price attribute
    #     - print the price of the shirt with a 12% discount

    shirt_one.change_price(10)
    print(shirt_one.price)

    # Question 3:
    #    - instantiate another object with the following characteristics:
    # .  - color orange, size large, style short sleeve, and price 10
    #    - store the object in a variable called shirt_two

    shirt_two = Shirt('orange', 'L','short_sleeve', 10)

    # Question 4:
    #   - calculate the total cost of shirt_one and shirt_two
    #   - store the results in a variable called total

    total = shirt_one.price + shirt_two.price
    print("Total price of both shirt:{} ".format(total))

    # Question 5:
    #   - use the shirt discount method to calculate the total cost if
    #   - shirt_one has a discount of 14% and shirt_two has a discount of 6%
    #   - store the results in a variable called total_discount

    total_discount = shirt_one.discount(0.14) + shirt_two.discount(0.06)
    print("Total price after discount :{}".format(total_discount))