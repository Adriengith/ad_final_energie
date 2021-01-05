import psycopg2
from psycopg2 import OperationalError


def create_companies():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS companies (
                id SERIAL PRIMARY KEY,
                test1 TEXT,
                test2 TEXT,
                test3 TEXT,
                test4 TEXT
            );""")


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
        )
        print("Connection to BODACC_DB as successful")
    except OperationalError as e:
        print(f"The error '{e}' as occured")
    return connection


def insert_companies(test1, test2, test3, test4 ):
    while True:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO companies(test1, test2, test3, test4) VALUES (%s, %s, %s, %s);",(test1, test2, test3, test4))
                print("add ok")










connection = create_connection("energies","postgres","postgres","localhost","5432")




create_companies()
print("ok")
insert_companies("LOLLOLLOL","LOLLOLLOL","LOLLOLLOL","LOLLOLLOL")