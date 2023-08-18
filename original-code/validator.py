class Validator():
    def valid_string(self, to_check):
        for check in to_check:
            if not isinstance(check, str): return False
            elif not check.strip(): return False
        return True
    
    def valid_list(self, to_check):
        for check in to_check:
            if not isinstance(check, list): return False
            elif len(check) == 0: return False
        return True
    
    def valid_float(self, to_check):
        for check in to_check:
            if not isinstance(check, float): return False
        return True
    
    def valid_dict(self, to_check):
        for check in to_check:
            if not isinstance(check, dict): return False
            elif len(check) == 0: return False
        return True