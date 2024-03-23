import sqlite3
import sql_scripts as ss


DATABASE = 'cars.db'



def print_cars_by_owner(owner):
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('fast_cars.db')
        cursor = db.cursor()

        sql = "SELECT * FROM owner;"

        cursor.execute(ss.SQL_SELECT_CARS_BY_OWNER,(owner,))
        results = cursor.fetchall()

        for record in results:
            print(record)  




if __name__ == "__main__":
    print("Hello, World")
    print("What can I do for you?")
    owner = input("What person do you want to investigate? ")
    print_cars_by_owner(owner)