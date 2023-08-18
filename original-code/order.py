from lib.validator import Validator as validator

class Order():
    number, name, deliver_to, ordered, eta, order_total = str, str, str, dict, str, float
    
    def __init__(self, number, name, deliver_to, ordered, eta, order_total):
        self.validator = validator()
        
        if not self.validator.valid_string([number, name, deliver_to, eta]) or not self.validator.valid_dict([ordered]) or not self.validator.valid_float([order_total]):
            raise Exception('Invalid details provided')
        
        self.number = number
        self.name = name
        self.deliver_to = deliver_to
        self.ordered = ordered
        self.eta = eta
        self.order_total = order_total
    
    def print_receipt(self):
        receipt = f"""
        ------------------------------
            THANK YOU FOR ORDERING
        ------------------------------
        ORDER NO. {self.number}
        ------------------------------
        FOR: {self.name}
        TO: {self.deliver_to}
        ------------------------------
        ITEMS ORDERED:
        {list(self.ordered)}
        
        ------------------------------
        TOTAL: {str(self.order_total)}
        """