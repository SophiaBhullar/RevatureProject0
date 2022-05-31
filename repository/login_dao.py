import psycopg2
from repository.connection import get_connection
from models.login_dto import Login

#DAO= Data Access Object
# All database interaction to this file
#like inserting queries and all

#create a user login
#read user login


def select_user_by_username(cust_name):
    connection = get_connection()
    cursor = connection.cursor()

    #select user from database

    qry = f"SELECT * FROM cust_login WHERE cust_name = '{cust_name}';"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
        
            user_login = Login(record[0], record[1], record[2])
            return user_login
    
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()



def select_user(cust_name,cust_pass):
    connection = get_connection()
    cursor = connection.cursor()

    #select user from database

    qry = f"SELECT * FROM cust_login WHERE cust_name = '{cust_name}' AND cust_pass = '{cust_pass}';"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
        
            user_login = Login(record[0], record[1], record[2])
            return user_login
    
    except(psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if connection is not None:
            connection.close()


def select_user_by_id(cust_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM cust_login where cust_id = {cust_id};"

    try:
        cursor.execute(qry)
        
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_login = Login(record[0],record[1], record[2])
            return user_login

    

    except(psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
    





def insert_user(cust_name, cust_pass):
    connection = get_connection()
    cursor = connection.cursor()
    
    #create a user
    qry = "INSERT INTO cust_login VALUES (default, %s, %s) RETURNING cust_id;"

    try:
        cursor.execute(qry, (cust_name,cust_pass))
        id = cursor.fetchone()[0]
        """ while True:
            record = cursor.fetchone()
            if record is None:
                break """
        connection.commit()
        return id

    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()

    finally:
        if connection is not None:
            connection.close()
