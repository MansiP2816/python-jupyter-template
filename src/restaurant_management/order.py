class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append({"item": item, "quantity": quantity})

    def show_order(self):
        print("\n---- CURRENT ORDER ----")
        for entry in self.items:
            item = entry["item"]
            print(f"{item['name']} x {entry['quantity']} = ₹{item['price'] * entry['quantity']}")
