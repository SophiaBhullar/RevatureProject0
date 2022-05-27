import psycopg2
from database.connection import get_connection

#DAO= Data Access Object
# All database interaction to this file
#like inserting queries and all

#create a user login
#read user login

def insert_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()
    
    #create a user
    qry = "INSERT INTO cust_login VALUES (default, %s, %s) RETURNING cust_id;"

    try:
        cursor.execute(qry, (username,password))
        while True:
            record = cursor.fetchone()
            if record is None:
                break
        connection.commit()
        return record

    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()

    finally:
        if connection is not None:
            print("Connection is closed")
            connection.close()
