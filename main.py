def get_product():
    while True:
        product_name = input("Enter product: ")
        if product_name.isalpha():
            break 
        else:
            print("Invalid input. Enter a word")

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

def collect_orders():
    inventory = []
    item = get_product()
    inventory.append(item)

    while True:
        continue_input = input("\nDo you want to add another item? (y/n): ")
        continue_order = continue_input.strip().lower()
        if continue_order == "y":
            item = get_product()
            inventory.append(item)
        elif continue_order == "n":
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
    
    return inventory

# TODO: (Gabrielle) Ask for the customer name and the senior id 

# TODO: (John Mark) Print the items and calculate the total

# TODO: (John Matthew) Call all necessary functions and 
# calculate the grand total