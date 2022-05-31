
from models import cust_info_dto
from models.login_dto import Login
from repository.cust_info__dao import select_by_user
from repository.login_dao import select_user

def check_login(login_input):
    print(login_input)
    user_dto = select_user(login_input.get("cust_name"), login_input.get("cust_pass"))
    if user_dto is not None:
        return user_dto
   

def user_details(cust_id):
    details= select_by_user(cust_id)
    if details is not None:
        return details