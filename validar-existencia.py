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
        
    def __str__(self):
        return self.username
            
    
if __name__ == '__main__':
    
    if User.table_exists():
        User.drop_table()
    
    User.create_table()
    
    ##### 1. Insertando múltiples registros
    users = [
        {'username': 'user1', 'email': 'user1@example.com', 'active': True},
        {'username': 'user2', 'email': 'user2@example.com'},
        {'username': 'user3', 'email': 'user3@example.com', 'active': True},
        {'username': 'user4', 'email': 'user4@example.com'},
        {'username': 'user5', 'email': 'user5@example.com'},
        {'username': 'user6', 'email': 'user6@example.com', 'active': True},
        {'username': 'user7', 'email': 'user7@example.com', 'active': True},
    ]
    
    # retorna una query
    query = User.insert_many(users)
    query.execute()
    
    # count = User.select().where(User.username == 'user7').count()
    # print(count)
    
    # if count > 0:
    #     print('El usuario existe en la tabla.')
    # else:
    #     print('No fue posible obtener al usuario.')
    
    
    exists = User.select().where(User.username == 'user7').exists()
    print(exists)
    
    if exists:
        print('El usuario existe en la tabla.')
    else:
        print('No fue posible obtener al usuario.')
        
    # count: para conocer cuántos registros fueron obtenidos en la consulta
    # exists: para conocer si la consulta retorno o no registros