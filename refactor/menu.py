class Menu():
    def __init__(self, items, prices):
        if not items or not prices or len(items) != len(prices):
            raise ValueError("Invalid items and/or prices")
        
        self.items = {key: value for key, value in zip(items, prices)}
