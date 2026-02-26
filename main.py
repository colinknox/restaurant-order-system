class Order:
    def __init__(self, items, total):
        self.items = items
        self.total = total

    def calculate_tax(self):
        return self.total * 0.08
    
    def calculate_fees(self):
        raise NotImplementedError("Each order type has different fees")

    def process_order(self):
        raise NotImplementedError("Each order type processes differently")

    def get_final_total(self):
        return self.total + self.calculate_tax() + self.calculate_fees()





order = Order(["Gang-Jeong", "Cheesling"], 10)

print(f"""
ITEMS: {order.items}
TOTAL: {order.total}
TAX: {order.calculate_tax()}
FINAL TOTAL: {order.get_final_total()}
""")

# print(f"""
# ITEMS: {order.items}
# TOTAL: {order.total}
# TAX: {order.calculate_tax()}
# CALCULATE FEES: {order.calculate_fees()}
# PROCESS ORDER: {order.process_order()}
# """)


