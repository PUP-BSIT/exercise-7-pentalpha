def get_product():
    while True:
        product_name = input("Enter product: ")
        if product_name.isdigit():
            print("Invalid input. Enter a word")
        else:
            break

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

def print_items(inventory):
    print("\nOrder Summary:")
    print("========================================")
    print("Product Name     | Price   | Qty | Total")
    print("========================================")

    for item in inventory:
        product_name = item[0]
        price = float(item[1])
        quantity = int(item[2])
        total = price * quantity
        print(f"{product_name} | {price:.2f} | {quantity} | {total:.2f}")

    print("========================================")

def main_execution():
    print("Welcome! Please enter your order")
    orders = collect_orders()

    customer_name = input("Enter Customer Name: ")
    while True:
        senior_id = input("Enter Senior ID Number (leave blank if none): ")
        if senior_id.isdigit() or senior_id == "":
            break
        else:
            print("Please input a valid Senior ID Number.")
            
    is_senior = senior_id != ""
    print_items(orders)

main_execution()

# TODO: (John Matthew) Call all necessary functions and 
# calculate the grand total