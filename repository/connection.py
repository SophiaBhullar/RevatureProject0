import psycopg2


# define function for database connection

def get_connection():
        connection = psycopg2.connect(
            database="bankDB",
            user="postgres",
            password="project0",
            host="bank-database.c9nrebfnqjzt.us-east-2.rds.amazonaws.com",
            port="5432"
    
    )
        return connection