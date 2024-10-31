from flask import Flask
import util

app = Flask(__name__)


username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'

@app.route('/')
def update_basket_a():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    try:
        # SQL command to insert a new row into basket_a
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (6, 'Cherry');")
        connection.commit() 
        return "Success!"  
    except Exception as e:
        connection.rollback() 
        # Return an error 
        return f"Error: {str(e)}"  
    finally:
        util.disconnect_from_db(connection, cursor)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1')

