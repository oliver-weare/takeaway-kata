from lib.validator import Validator as validator

class Menu():
    items = {}
    
    def __init__(self, items, prices):
        self.validator = validator()
        
        if not self.validator.valid_list([items, prices]):
            raise Exception('Invalid args provided')
        if len(items) != len(prices):
            raise Exception('Items and prices must match')
        if not self.validator.valid_string(items) or not self.validator.valid_float(prices):
            raise Exception('Invalid list items provided')
        
        self.items = {key: value for key, value in zip(items, prices)}