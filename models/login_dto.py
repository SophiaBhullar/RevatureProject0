class Login:
    def __init__(self, cust_id, cust_name, cust_pass):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.cust_pass = cust_pass


    def __repr__(self) -> str:
        return f"User Login: id - {self.cust_id} cust_name - {self.cust_name} cust_pass - {self.cust_pass}"
        

    