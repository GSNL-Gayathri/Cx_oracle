from flask import Flask, jsonify, g
from manage_oracle_connection import ManageOracleConnection

app = Flask(__name__)

def get_oracle_connection():
    if 'oracle_pool' not in g:
        g.oracle_pool = OracleConnectionManager()
    return g.oracle_pool.acquire()

@app.route('/')
def hello():
    conn = get_oracle_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table')
    data = cursor.fetchall()
    cursor.close()
    g.oracle_pool.release_connection(conn)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run()
