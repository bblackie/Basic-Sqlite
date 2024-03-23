import sqlite3

DATABASE = 'cars.db'
SQL_SELECT_CARS_BY_OWNER = '''
                            SELECT owner.name, owner.wealth, car.name
                            FROM owner JOIN car_owner ON owner.id = car_owner.owner_id
                            JOIN car ON car.id = car_owner.car_id
                            WHERE owner.name = ?;
                            '''


def print_cars_by_owner(owner):
    with sqlite3.connect(DATABASE) as db:
        db = sqlite3.connect('fast_cars.db')
        cursor = db.cursor()

        sql = "SELECT * FROM owner;"

        cursor.execute(SQL_SELECT_CARS_BY_OWNER,(owner,))
        results = cursor.fetchall()

        for record in results:
            print(record)  





if __name__ == "__main__":
    
    owner = input("What person do you want to investigate? ")
    print_cars_by_owner(owner)