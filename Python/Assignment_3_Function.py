"""
Assignment 3: Functions (User-Defined, Recursive, Lambda, Map, Filter)
Description: Online billing and utility automation tools.
"""

# #############################################################################
# TASK 1 - BASIC FUNCTION: PRICE AFTER DISCOUNT
# 1. Write a function apply_discount(price, discount_percent) that:
#    - Returns the price after discount.
#    - If discount_percent is missing, apply a default discount of 5%.
# 2. Test the function with:
#    - apply_discount(1000, 10)
#    - apply_discount(500) # uses default discount
# Extra (optional): Add a condition inside the function to ensure discount never exceeds 60%.
# #############################################################################

print("TASK 1 - BASIC FUNCTION: PRICE AFTER DISCOUNT")

def apply_discount(price, discount_percent=5):
    if discount_percent > 60:
        discount_percent = 60
    return price - (price * (discount_percent / 100))

print(apply_discount(1000, 10))
print(apply_discount(500))

print("-" * 50)

# #############################################################################
# TASK 2 - RECURSIVE FUNCTION: FACTORIAL UTILITY
# 1. Create a recursive function factorial(n) that:
#    - Returns the factorial of n.
# 2. Handles two edge cases: n == 0 and n == 1.
# 3. Prints an error message if n is negative.
# Test with: factorial(5), factorial(0), factorial(-3)
# #############################################################################

print("TASK 2 - RECURSIVE FUNCTION: FACTORIAL UTILITY")

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(0))
print(factorial(-3))

print("-" * 50)

# #############################################################################
# TASK 3 - LAMBDA FUNCTION: GST CALCULATOR
# 1. Create a lambda function 'gst' that returns price after adding 18% GST.
# Example: gst = lambda price: price + (0.18 * price)
# Extra (optional): Create another lambda to compute final price after GST + discount together.
# #############################################################################

print("TASK 3 - LAMBDA FUNCTION: GST CALCULATOR")

gst = lambda price: price + (0.18 * price)

final_price = lambda price, discount_percent: price + (0.18 * price) - (price * (discount_percent / 100))

print(gst(1000))
print(final_price(1000, 10))

print("-" * 50)


# #############################################################################
# TASK 4 - USING map(): APPLY GST TO LIST OF PRICES
# 1. Given list: prices = [100, 250, 400, 1200, 50]
# 2. Use map() with your gst lambda to generate a new list prices_with_gst.
# 3. Print both lists: Original prices and Prices after GST.
# #############################################################################

print("TASK 4 - USING map(): APPLY GST TO LIST OF PRICES")

prices = [100, 250, 400, 1200, 50]

prices_with_gst = list(map(gst, prices))

print(f"Original prices: {prices}")
print(f"Prices after GST: {prices_with_gst}")

print("-" * 50)



# #############################################################################
# TASK 5 - USING filter(): FILTER EXPENSIVE PRODUCTS
# 1. Given list: prices = [100, 250, 400, 1200, 50, 2000, 850]
# 2. Use filter() to:
#    - Create a list of prices greater than 500.
#    - Create another list of prices less than or equal to 500.
# 3. Print both lists.
# #############################################################################

print("TASK 5 - USING filter(): FILTER EXPENSIVE PRODUCTS")

prices = [100, 250, 400, 1200, 50, 2000, 850]

expensive_products = list(filter(lambda price: price > 500, prices))
cheap_products = list(filter(lambda price: price <= 500, prices))

print(f"Expensive products: {expensive_products}")
print(f"Cheap products: {cheap_products}")

print("-" * 50)


# #############################################################################
# TASK 6 - COMBINED UTILITY FUNCTION
# 1. Write a function process_prices(prices) that:
#    - Takes a list of prices.
#    - Uses map() + lambda to apply 10% discount to all prices.
#    - Uses filter() to keep only discounted prices that are above 300.
# 2. Returns both lists: discounted_prices and filtered_prices.
# Test with: process_prices([100, 500, 900, 50, 750])
# #############################################################################

print("TASK 6 - COMBINED UTILITY FUNCTION")

def process_prices(prices):
    discounted_prices = list(map(lambda price: price * 0.9, prices))
    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))
    return discounted_prices, filtered_prices

discounted_prices, filtered_prices = process_prices([100, 500, 900, 50, 750])

print(f"Discounted prices: {discounted_prices}")
print(f"Filtered prices: {filtered_prices}")

print("-" * 50)


# #############################################################################
# TASK 7 - MINI PROBLEM: MENU USING FUNCTIONS
# 1. Create the following three small functions:
#    - add_price(prices_list, price) -> adds price to the list.
#    - get_average_price(prices_list) -> returns average price.
#    - get_max_price(prices_list) -> returns the maximum price.
# 2. Then create a simple menu:
#    1 -> Add price | 2 -> Show average | 3 -> Show highest | q -> Quit
# 3. Use only loops + function calls (no OOP).
# #############################################################################

print("TASK 7 - MINI PROBLEM: MENU USING FUNCTIONS")

prices_list = []

def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    if not prices_list: return 0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    if not prices_list: return "No prices added"
    return max(prices_list)

while True:
    print("1 -> Add price | 2 -> Show average | 3 -> Show highest | q -> Quit")
    choice = input("Enter your choice: ")
    if choice == "q":
        break
    elif choice == "1":
        price = float(input("Enter price: "))
        add_price(prices_list, price)
    elif choice == "2":
        print(f"Average price: {get_average_price(prices_list)}")
    elif choice == "3":
        print(f"Highest price: {get_max_price(prices_list)}")
    else:
        print("Invalid choice. Please try again.")
