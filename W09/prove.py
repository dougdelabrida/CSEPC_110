items_cart = []

menu_action = None

while menu_action != 5:
    print("1 - Add a new item")
    print("2 - Display the contents of the shopping cart")
    print("3 - Remove an item (only needed for the final project deliverable)")
    print("4 - Compute the total (only needed for the final project deliverable)")
    print("5 - Quit")

    menu_action = int(input(""))

    if menu_action == 1:
        item_name = input("What item would you like to add? ")
        items_cart.append(item_name)
        print(f"'{item_name}' has been added to the cart")
    # if menu_action == 2:
    #     print(items_cart)
    # if menu_action == 3:
    #     print("number 3")
    # if menu_action == 4:
    #     print("number 4")
