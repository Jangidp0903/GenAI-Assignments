"""
Assignment 1: Python - Data Structures
Description: Inventory utility for an e-commerce store.
"""

# =============================================================================
# Task 1: Product Collections (Lists & Tuples)
# 1. Create a list named products containing at least 6 product names (strings).
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch", "Camera"]

# 2. Create a tuple named sample_product that stores (product_name, price, category) for one product.
sample_product = ("Laptop", 999.99, "Electronics")

# 3. Print the 2nd and last product from the products list.
print(f"2nd product: {products[1]}")
print(f"Last product: {products[-1]}")

# 4. Append two new product names to products and then print the updated list.
products.append("Gaming Console")
products.append("Smart Home Hub")
print(f"Updated products list: {products}")

# Extra (optional): Convert sample_product into a list, change its price, and convert it back to a tuple.
sample_product_list = list(sample_product)
sample_product_list[1] = 899.99  # Change price
sample_product = tuple(sample_product_list)
print(f"Updated sample product: {sample_product}")
# =============================================================================




# =============================================================================
# Task 2: Categories (Sets)
# 1. From your products list, create a set of categories called categories_set.
categories_set = {"Electronics", "Accessories", "Gaming", "Smart Home"}

# 2. Demonstrate adding a new category to the set and show that duplicates are ignored.
categories_set.add("Audio")
categories_set.add("Audio")  # This duplicate will be ignored
print(f"Categories set after adding 'Audio': {categories_set}")

# 3. Show how to check whether a category exists in the set (print a boolean result).
print(f"Is 'Electronics' in categories_set? {'Electronics' in categories_set}")

# Extra (optional): Show how to get the total number of unique categories using a set.
print(f"Total unique categories: {len(categories_set)}")
# =============================================================================




# =============================================================================
# Task 3: Product Pricing (Dictionaries)
# 1. Create a dictionary price_dict where keys are product names and values are prices (integers or floats).
price_dict = {
    "Laptop": 999.99,
    "Smartphone": 599.99,
    "Tablet": 399.99,
    "Headphones": 49.99,
    "Smartwatch": 199.99,
    "Camera": 699.99
}
# 2. Write small code blocks to: 
#    - Add a new product with price to price_dict.
price_dict["Wireless Earbuds"] = 79.99

#    - Update the price of an existing product.
price_dict["Smartphone"] = 549.99

#    - Remove a product by name (handle the case when the product does not exist).
if "Camera" in price_dict:
    del price_dict["Camera"]
else:
    print("Product 'Camera' does not exist in price_dict.")

# 3. Print the average price of all products (use only dictionary operations and basic arithmetic).
total_price = sum(price_dict.values())
count = len(price_dict)
average_price = total_price / count if count > 0 else 0
print(f"Average price of all products: {average_price}")

# Extra (optional): Print the product with both the maximum and minimum prices.
max_price_product = max(price_dict, key=price_dict.get)
min_price_product = min(price_dict, key=price_dict.get)
print(
    f"Product with maximum price: {max_price_product} | "
    f"Price: {price_dict[max_price_product]}"
)
print(
    f"Product with minimum price: {min_price_product} | "
    f"Price: {price_dict[min_price_product]}"
)
# =============================================================================




# =============================================================================
# Task 4: Combined Operations
# prodcut_categories is a dictionary mapping product names to their categories.
product_categories = {
    "Laptop": "Electronics", "Smartphone": "Electronics", "Tablet": "Electronics",
    "Headphones": "Accessories", "Smartwatch": "Accessories", "Camera": "Electronics",
    "Gaming Console": "Gaming", "Smart Home Hub": "Smart Home"
}
# 1. Using the products list and price_dict, create a list of tuples named catalog where each tuple is (product_name, price, category).
catalog = []
for product in products:
    price = price_dict.get(product, "Price not available")
    category = product_categories.get(product, "Category not available")
    catalog.append((product, price, category))

# 2. From catalog, create a new dictionary category_to_products that maps each category to a list of product names in that category.
category_to_products = {}
for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

# 3. Print all products that belong to the category that has the maximum number of products.
max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))
print(f"Category with maximum products: {max_category}")
print(f"Products in this category: {category_to_products[max_category]}")
# =============================================================================

