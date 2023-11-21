import cx_Oracle

class ManageOracleConnection:
    _pool = None

    @classmethod
    def get_connection(cls):
        if not cls._pool:
            cls._pool = cx_Oracle.SessionPool(
                user="your_username",
                password="your_password",
                dsn="your_oracle_server",
                min=1,
                max=1,
                increment=0,
                getmode=cx_Oracle.SPOOL_ARRIVAL_WAIT,
                encoding='utf-8'
            )
        return cls._pool.acquire()

    @classmethod
    def release_connection(cls, connection):
        cls._pool.release(connection)
