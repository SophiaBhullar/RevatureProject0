# for successful registration: need valid username and password, first name, last name and other information
#to validate, we are checking length of input from user

import imp
from select import select
from models.cust_info_dto import Customer
from models.login_dto import Login
from repository.login_dao import insert_user, select_user_by_id
from repository.cust_info__dao import insert_user_info

def validate_registration(input):
    login_dto = Login(0, input.get("cust_name"), input.get("cust_pass"))
    cust_info_dto = Customer(0,0,input.get("first_name"), input.get("last_name"), input.get("acc_type"), input.get("balance"))

    return login_dto.validate_login() and cust_info_dto.validate_user_info()
       

def create_login(input):
    cust_id = insert_user(input.get("cust_name"), input.get("cust_pass"))

    if cust_id is not None:
        return cust_id


def create_user_info(cust_id, input):
    login_dto = select_user_by_id(cust_id)
    acc_num = insert_user_info(login_dto, input.get("first_name"), input.get("last_name"), input.get("acc_type"), input.get("balance"))


    if acc_num is not None:
        return acc_num


