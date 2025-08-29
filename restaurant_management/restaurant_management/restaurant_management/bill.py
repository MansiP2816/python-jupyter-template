class Bill:
    def __init__(self, order, tax_rate=0.05, service_charge=0.10):
        self.order = order
        self.tax_rate = tax_rate
        self.service_charge = service_charge

    def generate_bill(self):
        subtotal = sum(item["item"]["price"] * item["quantity"] for item in self.order.items)
        tax = subtotal * self.tax_rate
        service = subtotal * self.service_charge
        total = subtotal + tax + service

        print("\n---- BILL ----")
        print(f"Subtotal: ₹{subtotal}")
        print(f"Tax (5%): ₹{tax:.2f}")
        print(f"Service Charge (10%): ₹{service:.2f}")
        print(f"TOTAL: ₹{total:.2f}")
