import peewee

db = peewee.MySQLDatabase('databasename', 
    host='localhost', 
    port=3306, 
    user='user', 
    passwd='password')



