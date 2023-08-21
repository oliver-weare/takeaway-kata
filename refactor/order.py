class Order():
    def __init__(self, number, name, address, order, eta, total):
        self.number = number
        self.name = name
        self.address = address
        self.order = order
        self.eta = eta
        self.total = total
    
    def print_receipt(self):
        order_list = "\n".join([f"{item}: {quantity}" for item, quantity in self.order.items()])
        
        receipt = f"""
        ------------------------------
            THANK YOU FOR ORDERING
        ------------------------------
        ORDER NO. {self.number}
                
        FOR: {self.name}
        TO: {self.address}
        ------------------------------
        ITEMS ORDERED:
        {order_list}
        ------------------------------
        TOTAL: {self.total:.2f}
        """
        
        print(receipt)
