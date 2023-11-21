from flask import Flask, jsonify
from manage_oracle_connection import ManageOracleConnection

app = Flask(__name__)

@app.route('/')
def hello():
    conn = ManageOracleConnection.get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table')
    data = cursor.fetchall()
    cursor.close()
    OracleConnectionManager.release_connection(conn)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run()
