from flask import Flask, render_template
import util

# create an application instance
app = Flask(__name__)

username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/')

def index():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    try:
    	record = util.run_and_fetch_sql(cursor, "SELECT a.fruit_a AS fruit_a, NULL AS fruit_b FROM basket_a a LEFT JOIN basket_b b ON a.fruit_a = b.fruit_b WHERE b.fruit_b IS NULL UNION ALL SELECT NULL AS fruit_a, b.fruit_b AS fruit_b FROM basket_b b LEFT JOIN basket_a a ON b.fruit_b = a.fruit_a WHERE a.fruit_a IS NULL;")
    	if record == -1:
    		return "Something is wrong with the SQL command"
    	col_names = [desc[0] for desc in cursor.description]
    	log = record[:5]
    except Exception as e:
    	connection.rollback()
    	error_message = str(e)
    	return f"Error: {str(e)}"
    # disconnect from database
    finally:
    	util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', sql_table = log, table_title=col_names)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

