import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn=None
    try:
      conn = sqlite3.connect(db_file)  # To-Do add a connection for the database
      conn.ProgrammingError
    except Error as e:
        print(e)
    finally:
    #To-Do return the connection 
     return conn 

def close_connection(conn):
    """ closes a connection to a database """
    conn.close()


def select_all(conn): 

    cur = conn.cursor() 
    query = "SELECT * FROM longley "
    cur.execute(query)

      # To-Do fetch all rows using the cursor cur
    rows = cur.fetchall() 
    return rows 


def print_rows(rows):
    """ Loop through the retrived rows of a table and print them"""
    # All of the function body is a todo task
    for row in rows:
        print(row)
create_connection("longley.db")