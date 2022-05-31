from distutils.log import Log
import imp
from multiprocessing.spawn import import_main_path
import psycopg2
from repository.connection import get_connection
from models.cust_info_dto import Customer
from models.login_dto import Login




def select_by_user(cust_id):
    connection = get_connection()
    cursor = connection.cursor()

    #select user from database

    qry = f"SELECT * FROM cust_info WHERE cust_id = '{cust_id}';"

    try:
        cursor.execute(qry)
        
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            cust_info = Customer(record[0],record[1], record[2], record[3], record[4], record[5])
            return cust_info


    except(psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()


def select_cust_info_by_id(acc_num: int):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM cust_info where acc_num = {acc_num};"

    try:
        cursor.execute(qry)
        
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            cust_info = Customer(record[0],record[1], record[2], record[3], record[4], record[5])
            return cust_info

    except(psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()




def insert_user_info(login_dto: Login, first_name:str, last_name:str, acc_type:str, balance:float):
    connection = get_connection()
    cursor = connection.cursor()
    
    #create a user
    qry = "INSERT INTO cust_info VALUES (default, %s, %s, %s, %s, %s) RETURNING acc_num;"

    try:
        cursor.execute(qry, (login_dto.cust_id, first_name, last_name, acc_type, balance))
        id = cursor.fetchone()[0]
        connection.commit()
        return id

    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()

    finally:
        if connection is not None:
            connection.close()
