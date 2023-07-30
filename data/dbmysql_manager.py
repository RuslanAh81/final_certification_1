import mysql.connector
from mysql.connector import Error
from data.config import db_config

from model.pack_animals import Horses, Camels, Donkeys
from model.pets import Cats, Dogs, Hamsters
from model.registry_animals import RegistryAnimals


class MySqlManager:
    def __init__(self, path: str):
        self.__path = path
        print(path)

    def create_connection_mysql_db(db_host, user_name, user_password, db_name):
        connection_db = "Human_friends"
        try:
            connection_db = mysql.connector.connect(
                host=db_host,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Подключение к MySQL успешно выполнено")
        except Error as db_connection_error:
            print("Возникла ошибка: ", db_connection_error)
        return connection_db

    conn = create_connection_mysql_db(db_config["mysql"]["host"],
                                      db_config["mysql"]["user"],
                                      db_config["mysql"]["pass"],
                                      "Human_friends")
    try:
        cursor = conn.cursor()
        create_cat_table_query = """
            DROP TABLE IF EXISTS Cats;
            CREATE TABLE Cats (
 	        id_animal INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
 	        type_id INT UNSIGNED NOT NULL,
    	    name VARCHAR(50),
    	    birth_date DATE,
    	    command TEXT,    
    	    FOREIGN KEY (type_id) REFERENCES Types_animals(id_type)
        );"""
        cursor.execute(create_cat_table_query)

        # # вставка данных в таблицу
        insert_cats_table_query = '''
            INSERT INTO Cats (id_animal, type_id, name, birth_date, command) VALUES
            ('1', '1', 'Мурзик', '2010-01-02', 'сидеть, лежать,нельзя'),
            ('2', '1', 'Барсик','2010-02-02','сидеть, нельзя'
            ); '''
        cursor.execute(insert_cats_table_query)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

    def __read_cat(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        print("Кошки")
        try:
            with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="ruslan",
                    database="Human_friends"
            )as connection:
                show_db_query = "SELECT id_animal, name, birth_date, command FROM cats"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    rows = cursor.fetchall()
                    print(" Catsss")
                    for row in rows:
                        cat = Cats(row[0], row[1], row[2], row[3])
                        log_registry.get_log_registry().append(cat)
                        print("кошки 2")
                return "Успешно"

        except Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()


    def __read_dog(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        print("Собаки")
        try:
            with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="ruslan",
                    database="Human_friends"
            ) as connection:
                show_db_query = "SELECT id_animal, name, birth_date, command FROM cats"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    rows = cursor.fetchall()
                    print("Dogss")
                    for row in rows:
                        dog = Dogs(row[0], row[1], row[2], row[3])
                        log_registry.get_log_registry().append(dog)
                        print(" dogs2")
                return "Успешно"

        except Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_hamster(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        print("Ham")
        try:
            with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="ruslan",
                    database="Human_friends"
            ) as connection:
                show_db_query = "SELECT id_animal, name, birth_date, command FROM cats"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    rows = cursor.fetchall()
                    print("Hammm")
                    for row in rows:
                        hamster = Hamsters(row[0], row[1], row[2], row[3])
                        log_registry.get_log_registry().append(hamster)
                        print("hams2")
                return "Успешно"

        except Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()


    def __read_horse(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        print("Hors")
        try:
            with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="ruslan",
                    database="Human_friends"
            ) as connection:
                show_db_query = "SELECT id_animal, name, birth_date, command FROM cats"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    rows = cursor.fetchall()
                    print("Horsss")
                    for row in rows:
                        horse = Horses(row[0], row[1], row[2], row[3])
                        log_registry.get_log_registry().append(horse)
                        print("Horss2")
                return "Успешно"

        except Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_camel(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        print(" Camal")
        try:
            with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="ruslan",
                    database="Human_friends"
            ) as connection:
                show_db_query = "SELECT id_animal, name, birth_date, command FROM cats"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    rows = cursor.fetchall()
                    print("Camal")
                    for row in rows:
                        camel = Camels(row[0], row[1], row[2], row[3])
                        log_registry.get_log_registry().append(camel)
                        print("Camal2")
                return "Успешно"

        except Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_donkey(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        print("Don Key")
        try:
            with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="ruslan",
                    database="Human_friends"
            ) as connection:
                show_db_query = "SELECT id_animal, name, birth_date, command FROM cats"
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                    rows = cursor.fetchall()
                    print("Don keee")
                    for row in rows:
                        donkey = Donkeys(row[0], row[1], row[2], row[3])
                        log_registry.get_log_registry().append(donkey)
                        print("Don keyyy")
                return "Успешно"

        except Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    __function_read_animal = [__read_cat, __read_dog, __read_hamster,
                              __read_horse, __read_donkey, __read_camel]

    def read_db(self, log_registry: RegistryAnimals):
        result = "Успешно"
        print(" read дибил")
        for item in self.__function_read_animal:
            result = item(self, log_registry)
            if result.startswith('Ошибка'):
                return result
        return result
