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

class DeliveryOrder(Order):
    def __init__(self, items, total):
        super().__init__(items, total)

    def calculate_fees(self):
        return 5
    
    def process_order(self):
        return "Order dispatched for delivery"