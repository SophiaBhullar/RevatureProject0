class Customer:
    def __init__(self, acc_num:int, cust_id:int, first_name: str, last_name:str, acc_type: str, balance:float):
        self.acc_num = acc_num
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.acc_type = acc_type
        self.balance = balance


    def __repr__(self) -> str:
        return f"Customer Info: {self.acc_num} + {self.cust_id} + {self.first_name} + {self.last_name} + {self.acc_type} + {self.balance}"
        

    
    def validate_user_info(self) -> bool:
        if len(self.first_name) < 5 or len(self.last_name) < 5:
            return False
        elif len(self.first_name) > 20 or len(self.last_name) >20:
            return False
        else:
            return True