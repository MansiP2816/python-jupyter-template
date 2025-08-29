from menu import Menu
from order import Order
from bill import Bill

def main():
    menu = Menu()
    order = Order()

    while True:
        menu.show_menu()
        choice = input("\nEnter item ID to order (or 'q' to quit): ")

        if choice.lower() == "q":
            break

        item = menu.get_item(int(choice))
        if item:
            qty = int(input("Enter quantity: "))
            order.add_item(item, qty)
            order.show_order()
        else:
            print("Invalid choice! Try again.")

    if order.items:
        bill = Bill(order)
        bill.generate_bill()
    else:
        print("No items ordered.")

if __name__ == "__main__":
    main()

