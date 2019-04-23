import psycopg2
import datetime
def insert(table, column, value):
    connection = psycopg2.connect('dbname = thezdb' , 'user= postgres')
    mark = connection.cursor()
    statement = 'INSERT INTO ' + table + ' (' + column + ') VALUES (' + value + ')'
    mark.execute(statement)
    connection.commit()
    return