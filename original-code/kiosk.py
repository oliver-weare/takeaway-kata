from twilio.rest import Client as cl
from lib.validator import Validator as validator
from lib.menu import Menu 
from lib.order import Order as order
from datetime import datetime as dt, timedelta as td
import random

class Kiosk():
    user, address, orders = str, str, {}
    
    def __init__(self, name, add):
        self.validator = validator()
        
        if not self.validator.valid_string([name, add]):
            raise Exception('Invalid details provided')
        
        self.user, self.address = name, add
    
    def see_menu(self, menu):
        if not isinstance(menu, Menu):
            raise Exception('Must be menu')
        
        return list(menu.items)
    
    def order(self, menu, items):
        if not isinstance(menu, Menu):
            raise Exception('No valid menu')
        if not self.validator.valid_list([items]) or not self.validator.valid_string(items):
            raise Exception('Items must be strings')
        
        def generate_number():
            generated = random.randint(10000000, 99999999)
            if generated in self.orders: generate_number()
            return generated
        
        # unique_number = str(generate_number())
    
        # for testing
        unique_number = '10000000'
        
        total_cost = 0.0
        for item in items:
            if item not in menu.items: raise Exception(f'Could not find {item} on menu')
            
            total_cost += menu.items[item]
        
        ordered = {}
        for item in items:
            if item in ordered: ordered[item] += 1
            else: ordered[item] = 1
        
        now = dt.now()
        eta = now + td(minutes=30)
        eta_str = eta.strftime('%H:%M')
        
        self.orders[unique_number] = order(unique_number, self.user, self.address, ordered, eta_str, total_cost)
        to_print = self.orders.get(unique_number)
        
        client = cl() # redacted api key
        msg = client.messages.create(
            to='+447539203582',
            from_='+447401095513',
            body=f'Great news, order number: {unique_number} is on the way and due to arrive at {eta_str}'
        )
        
        to_print.print_receipt()
