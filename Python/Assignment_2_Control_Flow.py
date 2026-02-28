"""
Assignment 2: Python - Control Flow
Description: Order processing utilities for a small e-commerce store.
"""

# =============================================================================
# Task 1: Discount Rules (if / elif / else)
# 1. Write a program that reads an integer order_amount from the user using input().
# 2. Apply the following discount rules and print the final amount:
#    order_amount >= 2000 -> 15% discount, 1500-2000 -> 10%, 1000-1500 -> 7%, else 0%.
# 3. Handle non-numeric input by displaying an error message and exiting.
# =============================================================================

order_input = input("Enter the order amount: ")

# Checking if input is numeric to avoid using libraries or crash
if order_input.replace('.', '', 1).isdigit():
    order_amount = float(order_input)
    
    if order_amount >= 2000:
        discount_rate = 0.15
    elif 1500 <= order_amount < 2000:
        discount_rate = 0.10
    elif 1000 <= order_amount < 1500:
        discount_rate = 0.07
    else:
        discount_rate = 0.00

    discount_amt = order_amount * discount_rate
    final_amount = order_amount - discount_amt
    
    print(f"Order Amount: ${order_amount:.2f}")
    print(f"Discount Applied: {discount_rate*100}% (${discount_amt:.2f})")
    print(f"Final Amount: ${final_amount:.2f}")

    # Extra (Optional): Add tax (fixed 5%) after discount
    tax_amount = final_amount * 0.05
    total_with_tax = final_amount + tax_amount
    print(f"Subtotal: ${final_amount:.2f} | Tax (5%): ${tax_amount:.2f} | Total: ${total_with_tax:.2f}")

else:
    print("Invalid input. Please enter a numeric value. Exiting Task 1.")


# =============================================================================
# Task 2: Process Multiple Orders (for loop)
# 1. Given a list of order amounts: orders = [1200, 2500, 800, 1750, 3000].
# 2. Use a for loop to apply Task 1 rules to each order and print a summary table.
# 3. Compute and print the total revenue after discounts.
# Extra: Print the number of orders that received a discount.
# =============================================================================

orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_count = 0

print("\n" + "="*45)
print(f"{'Order':<10} | {'Discount %':<12} | {'Final Amount':<12}")
print("-"*45)

for order in orders:
    # Applying same rules as Task 1
    if order >= 2000:
        rate = 0.15
    elif 1500 <= order < 2000:
        rate = 0.10
    elif 1000 <= order < 1500:
        rate = 0.07
    else:
        rate = 0.00

    final = order * (1 - rate)
    total_revenue += final
    
    if rate > 0:
        discounted_count += 1
        
    print(f"${order:<9.2f} | {rate*100:<10.0f}% | ${final:<11.2f}")

print("-"*45)
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Orders with Discount: {discounted_count}")


# =============================================================================
# Task 3: User Menu (while loop + break/continue)
# 1. Implement a while-loop driven menu: 1-Add order, 2-Show totals, q-Quit.
# 2. Use continue to re-show menu after invalid input and break to exit on 'q'.
# =============================================================================

menu_orders = []

while True:
    print("\n--- Order Management Menu ---")
    print("1 - Add order amount")
    print("2 - Show all orders and total")
    print("q - Quit")
    
    choice = input("Enter your choice: ").lower()

    if choice == 'q':
        print("Quitting menu...")
        break # Exit the loop
    
    if choice == '1':
        amt_input = input("Enter order amount: ")
        if amt_input.replace('.', '', 1).isdigit():
            menu_orders.append(float(amt_input))
        else:
            print("Invalid amount. Returning to menu.")
            continue # Skip to next iteration
            
    elif choice == '2':
        if not menu_orders:
            print("No orders recorded yet.")
            continue
            
        current_total = 0
        for o in menu_orders:
            # Quick discount calculation for summary
            d = 0.15 if o >= 2000 else 0.10 if o >= 1500 else 0.07 if o >= 1000 else 0
            current_total += o * (1 - d)
            print(f"Order: ${o:.2f} -> Net: ${o*(1-d):.2f}")
        print(f"Current Total Revenue: ${current_total:.2f}")
        
    else:
        print("Invalid choice. Please use 1, 2, or q.")
        continue # Re-show menu


# =============================================================================
# Task 4: Loop Control with Conditions (break & continue)
# 1. Given daily sales: daily_sales = [200, 150, 0, 400, 50, -1, 300].
# 2. If -1: break. If 0: continue.
# 3. Print running total for valid sales and final total.
# =============================================================================

daily_sales = [200, 150, 0, 400, 50, -1, 300]
running_sales_total = 0

print("\n--- Daily Sales Processing ---")


for sale in daily_sales:
    if sale == -1:
        print("Corrupted data found (-1). Stopping loop.")
        break # Exit loop immediately
    
    if sale == 0:
        print("Skipping zero sale day.")
        continue # Skip this iteration
    
    running_sales_total += sale
    print(f"Sale: ${sale} | Running Total: ${running_sales_total}")

print(f"Final Processed Total: ${running_sales_total}")