from ast import Try
import psycopg2
from psycopg2 import sql
import logging
import sys

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1111",  #!!!!!! change to your password
)
connection.set_session(autocommit=True)

with connection.cursor() as cursor:
    cursor.execute('SELECT COUNT(*) FROM users')
    result = cursor.fetchone()
    print(result)

def is_admin(username: str) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                admin
            FROM
                users
            WHERE
                username = %(username)s
        """,{
            'username':username
        })
        result = cursor.fetchone()

    if result is None:
        #User does not exist
        return False
    else:
        admin, = result
        return admin

def count_rows(table_name: str, limit: int) -> int:
    logging.basicConfig(filename='my.log', level=logging.INFO)
    logging.info('Start')
    with connection.cursor() as cursor:
        stmt = sql.SQL("""
            SELECT
                COUNT(*)
            FROM (
                SELECT
                    1
                FROM
                    {table_name}
                LIMIT
                    {limit}
            ) AS limit_query
        """).format(
            table_name=sql.Identifier(table_name),
            limit=sql.Literal(limit),
        )
        try:
            cursor.execute(stmt)
        except:
            logging.info('Call Error %s - Unable to Finalize or Recognize Value', sys.exc_info()[0])
            return "Error occured, Check Log File."
        result = cursor.fetchone()
    rowcount, = result
    logging.info(rowcount)
    logging.info('Complete')
    if rowcount == None:
        return
    return rowcount

def user_input():
    print(is_admin(input("Enter User Admin Name: ")))

#print(count_rows('users', 1))
#print(count_rows('users', 10))

user_input();
#print(is_admin('test')) #!!!!!change to your username
#print(is_admin("'; select true; --"))
#print(count_rows('users',1))
#print(count_rows('users',10))
#print( count_rows("(select 1) as foo; update users set admin = true where name = 'haki'; --", 1))
#print(is_admin("'; update users set admin = 'true' where username = 'alex'; select true; --"))
#print(is_admin("alex"))

# print(is_admin("'; update users set admin = 'true' where username = 'yan'; select true; --"))
# print(is_admin("yan"))