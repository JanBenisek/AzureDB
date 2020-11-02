# %%
import pyodbc

server = 'server-randomfacts.database.windows.net'
database = 'database-randomfacts'
username = 'azureadmin'
password = 'Password123!'
driver = '{ODBC Driver 17 for SQL Server}'

app.config['AZURE_STORAGE_CONTAINER']

conn_str = ('DRIVER={driver};SERVER={server};PORT={port}'
            ';DATABASE={database};UID={user};PWD={password}').format(
        driver=driver,
        server=server,
        port=1433,
        database=database,
        user=username,
        password=password)

qry_rnd = "SELECT TOP 1 fact_text FROM dbo.randomFacts ORDER BY NEWID()"
qry = "SELECT TOP 1 fact_text FROM dbo.randomFacts WHERE fact_key='history' ORDER BY NEWID()"


with pyodbc.connect(conn_str) as conn:
    with conn.cursor() as cursor:
        cursor.execute(qry)
        row = cursor.fetchone()
        print(row[0])


# %%
def randomFact(conn_str: str, key: str = None) -> str:
    '''
    Function returns random fact from a DB

    Parameters
    ----------
    conn_str: str
        connection string to the DB

    key: str, default=None
        If not none, returns fact within group

    Output
    ------
    Random fact, as a string
    '''
    qry_all = '''SELECT TOP 1 fact_text
                 FROM dbo.randomFacts
                 ORDER BY NEWID()'''

    qry_grp = '''SELECT TOP 1 fact_text
                 FROM dbo.randomFacts
                 WHERE fact_key='{grp}'
                 ORDER BY NEWID()'''.format(grp=key)

    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            if key is None:
                cursor.execute(qry_all)
            else:
                cursor.execute(qry_grp)
            row = cursor.fetchone()
            return row[0]


randomFact(conn_str=conn_str, key='history')
# %%
