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

class DineInOrder(Order):
    def __init__(self, items, total):
        super().__init__(items, total)
    
    def calculate_fees(self):
        return 0
    
    def process_order(self):
        return "Order sent to kitchen, table service"

class TakeoutOrder(Order):
    def __init__(self, items, total):
        super().__init__(items, total)

    def calculate_fees(self):
        return 2
    
    def process_order(self):
        return "Order prepared for pickup"



order = Order(["Gang-Jeong", "Cheesling"], 10)
dine_in_order = DineInOrder(["Burger", "Chicken fries", "Soda"], 50)
takeout_order = TakeoutOrder(["Water"], 5)

# print(f"""
# ITEMS: {order.items}
# TOTAL: {order.total}
# TAX: {order.calculate_tax()}
# FINAL TOTAL: {order.get_final_total()}
# """)

print(f"""
ITEMS           : {takeout_order.items}
TOTAL           : {takeout_order.total}
TAX             : {takeout_order.calculate_tax()}
CALCULATE FEES  : {takeout_order.calculate_fees()}
PROCESS ORDER   : {takeout_order.process_order()}
FINAL TOTAL     : {takeout_order.get_final_total()}
""")


