import random, datetime as dt, timedelta as td

from menu import Menu
from order import Order

class Kiosk():
    def __init__(self, name, address):
        if not name or not address:
            raise ValueError("Name and address must be provided")
        
        self.name, self.address, self.orders = name, address, {}
    
    
    def view_menu(self, menu=Menu):
        if not isinstance(menu, Menu):
            raise TypeError("Invalid menu")
        
        return list(menu.items)
    
    
    def generate_number(self):
        used_numbers = set(self.orders.keys())
        generated = random.randint(1, 501)
        
        while generated in used_numbers:
            generated = random.randint(1, 501)
        
        return generated
    
    
    def create_order(self, menu, items):
        order_number = self.generate_number()
        
        total_cost = 0.0
        ordered = {}
        
        for item in items:
            try:
                item_cost = menu.items.get(item)
                if item_cost is None:
                    raise ValueError(f"Item '{item}' not found in menu")
                
                total_cost += item_cost

                ordered[item] = ordered.get(item, 0) + 1
                
            except KeyError as e:
                print(f"Item '{item}' not found in menu")
        
        now = dt.now()
        eta = now + td(minutes=30)
        eta_str = eta.strftime('%H:%M')
        
        new_order = Order(order_number, self.name, self.address, ordered, eta_str, total_cost)
        self.orders[order_number] = new_order
        new_order.print_receipt()