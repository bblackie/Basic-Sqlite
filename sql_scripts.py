

SQL_SELECT_CARS_BY_OWNER = '''
                            SELECT owner.name, owner.wealth, car.name
                            FROM owner JOIN car_owner ON owner.id = car_owner.owner_id
                            JOIN car ON car.id = car_owner.car_id
                            WHERE owner.name = ?;
                            '''
                            
                            