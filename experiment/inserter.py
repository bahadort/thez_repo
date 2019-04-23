import psycopg2
import datetime
def insert(table, column, value):
    connection = psycopg2.connect(dbnam='thezdb', user= 'postgres', password='123456')
    mark = connection.cursor()
    statement = 'INSERT INTO ' + table + ' (' + column + ') VALUES (' + value + ')'
    mark.execute(statement)
    connection.commit()
    return