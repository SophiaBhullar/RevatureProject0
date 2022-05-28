
from flask import Flask, render_template, request
from database.login_dao import insert_user, select_user
from models.login_dto import Login

# run flask here

app = Flask(__name__)
    

@app.route('/', methods=["GET"])
def landing_page():
    return render_template("index.html")

@app.route('/login', methods=["GET"])
def login_page():
    return render_template("login.html")


@app.route('/login/input', methods=["POST"])
def validate_login():
    login_input = request.form
    print(login_input)
    user_dto = select_user(login_input.get("cust_name"), login_input.get("cust_pass"))
    if user_dto is None:
        print(user_dto)
        return "Failed login"
    else:
        return render_template("details.html")
 

#print(insert_user("test_user_4", "pass_2"))
    #user_login= select_user(6)
    #print(user_login.cust_id)
    #print(user_login.cust_name)
    #print(user_login.cust_pass)


if __name__ == "__main__":
    app.run(debug=True)
