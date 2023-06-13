import peewee
from datetime import datetime

database = peewee.MySQLDatabase('pythonpeewee', 
    host='localhost', 
    port=3306, 
    user='root', 
    passwd='password')

# Creando el modelo User, que representa la tabla users
# 4 atríbutos 4 columnas
# la columna id se genera de forma automática
class User(peewee.Model):
    username = peewee.CharField(max_length=50, unique=True, index=True)
    email = peewee.CharField(max_length=60, null=False, )
    active = peewee.BooleanField(default=False)
    created_at = peewee.DateTimeField(default=datetime.now)
    
    class Meta:
        database = database
        db_table = 'users'
    
if __name__ == '__main__':
    
    if User.table_exists():
        User.drop_table()
    
    User.create_table()
