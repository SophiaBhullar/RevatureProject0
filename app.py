
from flask import Flask, render_template, request
from controller.registration_controller import get_registration_page, register_user
from repository.login_dao import insert_user, select_user
from models.login_dto import Login
from controller.home_controller import *
from controller.login_controller import *

# run flask here

app = Flask(__name__)
app.secret_key= "banking"

@app.route('/', methods=["GET"])
def login_page():
    return get_login_page()


@app.route('/login/input', methods=["POST"])
def cust_login():
    return check_cust_login(request.form)
    
 
@app.route('/registration')
def registration_page():
    return get_registration_page()


@app.route('/registration/register', methods=["POST"])
def register_new_user():
    return register_user(request.form)




#print(insert_user("test_user_4", "pass_2"))
    #user_login= select_user(6)
    #print(user_login.cust_id)
    #print(user_login.cust_name)
    #print(user_login.cust_pass)


if __name__ == "__main__":
    app.run(debug=True)
