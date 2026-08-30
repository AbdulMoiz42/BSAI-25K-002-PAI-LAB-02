def add_products(cart_list, IDs):
    while True:
        product_name = input("Enter product name (or 'q' to quit): ").strip()
        if product_name.lower() == 'q':
            break

        product_category = input("Enter product category: ").strip()
        
        product_price = float(input("Enter product price: "))
        if product_price <= 0:
            print("Product price cannot be zero or negative!")
            break
    
        product_quantity = int(input("Enter product quantity: "))
        if product_quantity <= 0:
            print("Product quantity cannot be zero or negative!")
            break

        product_exists = False
        for item in cart_list:
            if item['name'].lower() == product_name.lower() and item['category'].lower() == product_category.lower():
                item['quantity'] += product_quantity
                print(f"Product already in cart. Updated {item['name']} quantity to {item['quantity']}.")
                product_exists = True
                break

        if not product_exists:
            IDs += 1
            product = {
                'ID': IDs,
                'name': product_name,
                'category': product_category,
                'price': product_price,
                'quantity': product_quantity
            }
            cart_list.append(product)

    return IDs

def display_products(list_of_products):
    if not list_of_products:
        print("Your shopping cart is empty.")
        return
        
    print("\n--- Current Shopping Cart ---")
    for p in list_of_products:
        item_total = p['price'] * p['quantity']
        print(f"ID: {p['ID']} | Name: {p['name']} | Category: {p['category']} | Price: ${p['price']:.2f} | Quantity: {p['quantity']} | Total: ${item_total:.2f}")
    
    grand_total = sum(item['price'] * item['quantity'] for item in list_of_products)
    print(f"Grand Total Bill: ${grand_total:.2f}")

def update_price(list_of_product):
    if not list_of_product:
        print("Your cart is empty. Cannot update prices.")
        return

    product_id = int(input("Enter ID of product: "))
    if product_id <= 0:
        print("ID cannot be negative or zero.")
        return

    for p in list_of_product:
        if p['ID'] == product_id:
            new_price = float(input(f"Enter new price for {p['name']}: "))
            if new_price <= 0:
                print("Price cannot be zero or negative.")
                return

            p['price'] = new_price
            print(f"Successfully updated price for {p['name']}.")

            return
                
        print("Product ID not found in cart.")

def update_stock(list_of_product):
    if not list_of_product:
        print("Your cart is empty. Cannot modify quantities.")
        return

    product_id = int(input("Enter ID of product: "))
    if product_id <= 0:
        print("ID cannot be negative or zero.")
        return

    for p in list_of_product:
        if p['ID'] == product_id:
            new_stock = int(input(f"Enter quantity to adjust (use negative numbers to remove items, current: {p['quantity']}): "))
                
            if p['quantity'] + new_stock <= 0:
                list_of_product.remove(p)
                print(f"Quantity dropped to 0 or less. Removed {p['name']} from cart.")
            else:
                p['quantity'] += new_stock
                print(f"Successfully updated stock. New quantity for {p['name']} is {p['quantity']}.")

                return
                
        print("Product ID not found in cart.")

def out_stock(list_of_product):
    if not list_of_product:
        print("Your cart is empty.")
        return
        
    found_empty = False
    for p in list_of_product:
        if p['quantity'] <= 0:
            print(f"ID: {p['ID']} ({p['name']}) is out of stock / empty!")
            found_empty = True
            
    if not found_empty:
        print("All items in your cart have valid active quantities.")

if __name__ == "__main__":
    shopping_cart = []
    IDs = 0

    while True:
        print("\n===== ONLINE SHOPPING CART SYSTEM =====")
        print("1. Enter new product(s) / Add to existing data")
        print("2. View all products and bill")
        print("3. Update Price")
        print("4. View out of stock products")
        print("5. Update stock products (Modify Quantity)")
        print("6. Exit program")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            IDs = add_products(shopping_cart, IDs)
        elif choice == '2':
            display_products(shopping_cart)
        elif choice == '3':
            update_price(shopping_cart)
        elif choice == '4':
            out_stock(shopping_cart)
        elif choice == '5':
            update_stock(shopping_cart)
        elif choice == '6':
            print("Exiting system. Thank you for shopping with us!")
            break
        else:
            print("Enter options 1 to 6 only.")
