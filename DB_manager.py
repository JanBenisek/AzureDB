import pyodbc
from typing import List


def randomFact(conn_str: str, key: str = None,
               src: str = None) -> List[str]:
    '''
    Function returns random fact from a DB

    Parameters
    ----------
    conn_str: str
        connection string to the DB

    key: str, default=None
        If not none, returns fact within group

    src: str, default=None
        If not none, returns fact which user inserted

    Output
    ------
    Tuple with category and a random fact.
    Returns None if sql result is empty.
    '''
    qry_all = '''SELECT TOP 1 fact_key, fact_text
                 FROM dbo.randomFacts
                 ORDER BY NEWID()'''

    qry_grp = '''SELECT TOP 1 fact_key, fact_text
                 FROM dbo.randomFacts
                 WHERE fact_key='{grp}'
                 ORDER BY NEWID()'''.format(grp=key)

    qry_own = '''SELECT TOP 1 fact_key, fact_text
                 FROM dbo.randomFacts
                 WHERE fact_source='{src}'
                 ORDER BY NEWID()'''.format(src=src)

    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            if key is not None:
                cursor.execute(qry_grp)
            elif src is not None:
                cursor.execute(qry_own)
            else:
                cursor.execute(qry_all)
            row = cursor.fetchone()
            return row


def insertFact(conn_str: str, cat: str, fact: str):
    '''
    Function inserts new random fact

    Parameters
    ----------
    conn_str: str
        connection string to the DB

    cat: str, default=None
         Category of random fact

    fact: str, default=None
        Text of random fact

    Output
    ------
    None
    '''
    qry_ins = '''INSERT INTO dbo.randomFacts (fact_key, fact_source, fact_text)
                 VALUES ('{cat}', 'usr', '{txt}')'''.format(cat=cat, txt=fact)

    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            cursor.execute(qry_ins)
        conn.commit()
