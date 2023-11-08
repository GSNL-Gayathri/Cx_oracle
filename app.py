from flask import Flask, jsonify
import cx_Oracle

app = Flask(__name)

user = "your_username"
password = "your_password"
dsn = "your_oracle_server"

class Initialization(object):
    _pool = None

    def __new__(cls):
        if not cls._pool:
            cls._pool = cx_Oracle.SessionPool(user,
                                             password,
                                             dsn,
                                             min=1,
                                             max=1,
                                             increment=0,
                                             getmode=cx_Oracle.SPOOL_ARRIVAL_WAIT,
                                             encoding='utf-8'
                                             )
        return cls._pool

# Initialize the connection pool (only once)
connection_pool = Initialization()

@app.route('/')
def hello():
    # In each worker, you can use the same connection pool to get a connection
    conn = connection_pool.acquire()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table')
    data = cursor.fetchall()
    cursor.close()
    
    # When done, release the connection
    connection_pool.release(conn)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run()
