from .settings import db

class DB():
    def __init__(self):
        pass

    @staticmethod
    def check():
        for value in db.values():
            if not value:
                raise ValueError('Values cannot be null in settings.py')
                os.exit()

    @staticmethod
    def get_connection():
        #Return database's connection
        DB.check()
        host = db.get('host')# + ':' + db.get('port')
        username = db.get('username')
        password = db.get('password')
        db_name = db.get('db_name')
        #if use MySQL
        if db.get('type').lower() == 'mysql':
            import MySQLdb
            connection = MySQLdb.connect(host, username, password, db_name, charset='utf8')
            return connection

    @staticmethod
    def get_database_type():
        """
            Return database's type, in lowercase, eg:
            mysql, oracle, sqlserver...
        """
        return db.get('type').lower()

def main():
    pass

if __name__ == '__main__':
    main()
