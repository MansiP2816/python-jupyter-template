import json

class Menu:
    def __init__(self, menu_file="restaurant_management/data/menu.json"):
        with open(menu_file, "r") as f:
            self.menu = json.load(f)

    def show_menu(self):
        print("\n---- MENU ----")
        for category, items in self.menu.items():
            print(f"\n{category.upper()}")
            for item in items:
                print(f"{item['id']}. {item['name']} - ₹{item['price']}")

    def get_item(self, item_id):
        for items in self.menu.values():
            for item in items:
                if item["id"] == item_id:
                    return item
        return None
