SERVER = 'server-randomfacts.database.windows.net'
DATABASE = 'database-randomfacts'
USERNAME = 'azureadmin'
PASSWORD = 'Password123!'
DRIVER = '{ODBC Driver 17 for SQL Server}'
PORT = 1433
SECRET_KEY = 'supersecret'

CONN_STR = ('DRIVER={driver};SERVER={server};PORT={port};'
            'DATABASE={database};UID={user};PWD={password}').format(
        driver=DRIVER,
        server=SERVER,
        port=PORT,
        database=DATABASE,
        user=USERNAME,
        password=PASSWORD)
