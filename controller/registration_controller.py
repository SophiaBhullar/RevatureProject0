import imp
from flask import render_template
from service.registration_service import create_login, create_user_info, validate_registration

def get_registration_page():
    return render_template("registration.html")


def register_user(register_input):
    #validate input
    input_dict={
        "cust_name":register_input["cust_name"],
        "cust_pass":register_input["cust_pass"],
        "first_name":register_input["first_name"],
        "last_name":register_input["last_name"],
        "acc_type":register_input["acc_type"],
        "balance":register_input["balance"],

    }

    if validate_registration(input_dict):

        #create new user
        cust_id = create_login(register_input)
        acc_num = create_user_info(cust_id, register_input)
        #return success
        if acc_num is not None:
            return render_template("login.html")

    else:
        return "Failed to register"