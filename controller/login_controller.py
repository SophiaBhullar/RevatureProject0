from flask import render_template, session
from repository.cust_info__dao import select_by_user
from service.login_service import check_login 

def get_login_page():
    return render_template("login.html")


def check_cust_login(login_input):
    user_login = check_login(login_input)

    if user_login is None:
        return "Failed Login"
    else:
        session['cust_id'] = user_login.cust_id
        details = select_by_user(user_login.cust_id)
        return render_template("details.html", username=user_login.cust_name,acc_num=details.acc_num, first_name=details.first_name, last_name=details.last_name,acc_type=details.acc_type,balance=details.balance)


    