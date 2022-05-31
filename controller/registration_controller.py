import imp
from flask import render_template
from service.registration_service import create_login, create_user_info, validate_registration

def get_registration_page():
    return render_template("registration.html")


def register_user(register_input):
    #validate input
    if validate_registration(register_input):

        #create new user
        cust_id = create_login(register_input)
        acc_num = create_user_info(cust_id, register_input)
        #return success
        if acc_num is not None:
            return render_template("login.html")

    else:
        return "Failed to register"