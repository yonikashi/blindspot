import time
import os

from sqlalchemy import create_engine

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'pg-service'
db_port = '5432'

db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

def add_new_row(n):
    db.execute("INSERT INTO numbers (number,timestamp) "+\
        "VALUES ("+\
        str(n) + "," + \
        str(int(round(time.time() * 1000))) + ");")

def get_last_row():
    query = "" + \
            "SELECT number " + \
            "FROM numbers " + \
            "WHERE timestamp >= (SELECT max(timestamp) FROM numbers)" +\
            "LIMIT 1"

    result_set = db.execute(query)  
    for (r) in result_set:  
        return r[0]

if __name__ == '__main__':
    print('Application started')
    add_new_row(os.getenv('VALUE_ID'))
    print('The last value insterted is: {}'.format(get_last_row()))