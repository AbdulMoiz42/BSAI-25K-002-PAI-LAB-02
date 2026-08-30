def add_products(list_of_products,IDs):
    while True:
        product_name = input("Enter product name (or 'q' to quit): ").strip()
        if product_name.lower()=='q':
            break

        product_category = input("Enter product category :").strip()

        product_price = float(input("Enter product price: "))
        if product_price<=0:
            print("Product price can not zero or negative!")
            break

        product_quantity = int(input("Enter product quantity: "))
        if product_quantity<=0:
            print("Product quantity can not zero or negative!")
            break

        IDs+=1

        product={
            'ID':IDs,
            'name':product_name,
            'category':product_category,
            'price':product_price,
            'quantity':product_quantity
        }

        list_of_products.append(product)

    return IDs

def display_products(list_of_products):
    if not list_of_products:
        print("No data available.")
        return
        
    print("\n--- Records ---")
    for p in list_of_products:
        print(f"Name: {p['name']} | Category: {p['category']} | Price: {p['price']} | ID: {p['ID']} | Quantity: {p['quantity']}")

def update_price(list_of_product):
    id=int(input("Enter id of product:"))
    new_price=float(input("Enter new price:"))

    if id<=0:
        print("Id is not negative and zero")
        return

    for p in list_of_product:
        if p['ID']==id:
            p['price']=new_price

def update_stock(list_of_product):
    id=int(input("Enter id of product:"))
    new_stock=int(input("Enter new price:"))

    if id<=0:
        print("Id is not negative and zero")
        return

    for p in list_of_product:
        if p['ID']==id:
            p['quantity']+=new_stock 

def out_stock(list_of_product):
    if not list_of_product:
        return 0
    for p in list_of_product:
        if p['quantity']<=0:
            print(f"ID: {p['ID']} is out of stock!")

if __name__=="__main__":
    Inventory=[]
    IDs=0

    while True:
        print("\n===== Inventory SYSTEM =====")
        print("1. Enter new product(s) / Add to existing data")
        print("2. View all products")
        print("3. Update Price")
        print("4. View out of stock products")
        print("5. Update stock products")
        print("6. Exit program")

        choice = input("Select an option (1-5): ").strip()

        if choice=='1':
            IDs=add_products(Inventory,IDs)
        elif choice=='2':
            display_products(Inventory)
        elif choice=='3':
            update_price(Inventory)
        elif choice=='4':
            out_stock(Inventory)
        elif choice=='5':
            update_stock(Inventory)
        elif choice=='6':
            print("Exit system")
            break
        else:
            print("Enter options 1 to 6 only")
