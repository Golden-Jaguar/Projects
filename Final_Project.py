import psycopg2
from psycopg2 import sql
import logging

logging.basicConfig(level=logging.DEBUG, filename="Final_Project.log", filemode="a+")
logging.info('Start')

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
        logging.debug("User is not an admin")
        logging.info("End of Program")
        return False
    else:
        admin, = result
        logging.info("succesful loggin")
        return admin

def count_rows(table_name: str, limit: int) -> int:
    try: #error ha1ndling
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
            cursor.execute(stmt)
            result = cursor.fetchone()
        rowcount, = result
        return rowcount
    except Exception as a:
        error_m = str(a)
        error_m = "Error" + error_m
        logging.debug("Error" + "," + error_m)
        return "Invalid Input"
def user_input():
    print(is_admin(input("Enter User Admin Name: ")))


user_input();


rows = count_rows('users', 10)
print("Number of rows: ", + rows)
print(count_rows("(select 1) as foo; update users set admin = true where name = 'haki'; --", 1))
logging.info("End of Program")
#print(count_rows('users', 1))
#print(is_admin('test')) #!!!!!change to your username
#print(is_admin("'; select true; --"))
#print(count_rows('users',1))
#print(count_rows('users',10))
#print(is_admin("'; update users set admin = 'true' where username = 'alex'; select true; --"))
#print(is_admin("alex"))
# print(is_admin("'; update users set admin = 'true' where username = 'yan'; select true; --"))
# print(is_admin("yan"))