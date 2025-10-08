def main():
    menu = {
        "pizza" : 5.50,
        "nachos" : 4.75,
        "popcorn" : 6.25,
        "fries" : 3.50,
        "chips" : 2.00,
        "pretzel" : 3.50,
        "soda" : 2.75,
        "lemonade" : 3.00
    }
    orders = []
    print_menu(menu)
    order(menu, orders)
    final_print(menu, orders)

def print_menu(menu):
    print("----{[MENU]}----")
    for item, price in menu.items():
        print(item.ljust(10), end="")
        print(f"${price:.2f}")
    print("----------------\n")

def order(menu, orders):
    while True:
        choice = input("Select an item (Q to quit) ").strip().lower()
        if choice == "q":
            break
        if choice in menu:
            orders.append(choice)

def final_print(menu, orders):
    total = 0
    print("\n----{[YOUR ORDER]}----")
    for i in range(len(orders)):
        print(orders[i], end=" ")
    print("\n----------------------")
    for i in range(len(orders)):
        total += menu[orders[i]]
    print(f"Total: {total:.2f}")

if __name__ == "__main__":
    main()