def get_product():
    product_name = input("Enter product: ")

    while True:
        product_price = float(input("Product price: "))
        if product_price <= 0:
            print("Invalid input. Enter a positive number.") 
        else:
            break
    
    while True:
        product_quantity = int(input("Enter quantity: "))
        if product_quantity <= 0:
            print("Invalid input. Enter a positive number.") 
        else:
            break
    
    item =  [product_name, product_price, product_quantity]
    return item

# TODO: (Angela) Create a loop to ask the user for input until all 
# orders are complete

# TODO: (Gabrielle) Ask for the customer name and the senior id 

# TODO: (John Mark) Print the items and calculate the total

# TODO: (John Matthew) Call all necessary functions and 
# calculate the grand total