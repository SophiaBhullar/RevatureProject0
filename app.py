
from database.login_dao import insert_user

# run flask here

def main():
    insert_user("test_user_1", "test_user_2")
  

if __name__ == "__main__":
    main()
