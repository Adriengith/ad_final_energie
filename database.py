import psycopg2
from psycopg2 import OperationalError


def create_sectors():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS sectors (
                id SERIAL PRIMARY KEY,
                sector VARCHAR
            );""")

    insert_sector("agriculture")
    insert_sector("industrie")
    insert_sector("tertiaire")
    insert_sector("résidentiel")
    insert_sector(" professionnel non affecté")


def create_deliveries():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS deliveries (
                id SERIAL PRIMARY KEY,
                energy_id INT,
                operator_id INT,
                date INT,
                territory_id INT,
                sector_id INT,
                conso INT,
                address VARCHAR,
                city_id INT
            );""")

def create_cities():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS cities (
                id SERIAL PRIMARY KEY,
                city VARCHAR
            );""")


def create_operators():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS operators (
                id SERIAL PRIMARY KEY,
                operator VARCHAR
            );""")

def create_territories():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS territories (
                id SERIAL PRIMARY KEY,
                territory VARCHAR
            );""")

def create_energies():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS energies (
                id SERIAL PRIMARY KEY,
                energy VARCHAR
            );""")

    insert_energies("électricité")
    insert_energies("gaz")





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
        print("Connection to    DB as successful")
    except OperationalError as e:
        print(f"The error '{e}' as occured")
    return connection


def insert_sector(sector):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO sectors(sector) VALUES (%s);",(sector,))
            print("add in db")


def insert_energies(energy):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO energies(energy) VALUES (%s);",(energy,))
            print("add in db")




def insert_deliveries(energy_id, operator_id, date, territory_id, sector_id, conso, address, city_id):
    with connection:
        with connection.cursor() as cursor:

            cursor.execute("INSERT INTO deliveries(energy_id, operator_id, date, territory_id, sector_id, conso, address, city_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",(energy_id, operator_id, date, territory_id, sector_id, conso, address, city_id))

            print("add in db")


def find_operator_id(operateur):
    with connection:
        with connection.cursor() as cursor: 
            cursor.execute(f"select id from operators where operator = '{operateur}'")
            operator_id = cursor.fetchone()
            try :
                operator_id = operator_id[0]
            except:
                pass
            if operator_id is None:
                cursor.execute("INSERT INTO operators(operator) VALUES (%s);",(operateur,))
                cursor.execute(f"select id from operators where operator = '{operateur}'")
                operator_id = cursor.fetchone()
                try :
                    operator_id = operator_id[0]
                except:
                    pass
    return operator_id


def find_city_id(city):
    with connection:
        with connection.cursor() as cursor: 
            cursor.execute(f"select id from cities where city = '{city}'")
            city_id = cursor.fetchone()
            try :
                city_id = city_id[0]
            except:
                pass
            if city_id is None:
                cursor.execute("INSERT INTO cities(city) VALUES (%s);",(city,))
                cursor.execute(f"select id from cities where city = '{city}'")
                city_id = cursor.fetchone()
                try :
                    city_id = city_id[0]
                except:
                    pass
    return city_id


def find_territory_id(territory):
    with connection:
        with connection.cursor() as cursor: 
            cursor.execute(f"select id from territories where territory = '{territory}'")
            territory_id = cursor.fetchone()
            try :
                territory_id = territory_id[0]
            except:
                pass
            if territory_id is None:
                cursor.execute("INSERT INTO territories(territory) VALUES (%s);",(territory,))
                cursor.execute(f"select id from territories where territory = '{territory}'")
                territory_id = cursor.fetchone()
                try :
                    territory_id = territory_id[0]
                except:
                    pass
    return territory_id


connection = create_connection("energies","postgres","postgres","localhost","5432")




