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
        {'username': 'user1', 'email': 'user1@example.com'},
        {'username': 'user2', 'email': 'user2@example.com'},
        {'username': 'user3', 'email': 'user3@example.com'},
        {'username': 'user4', 'email': 'user4@example.com'},
        {'username': 'user5', 'email': 'user5@example.com'},
        {'username': 'user6', 'email': 'user6@example.com'},
        {'username': 'user7', 'email': 'user7@example.com'},
    ]
    
    # retorna una query
    query = User.insert_many(users)
    query.execute()
    
    # con get, si no obtiene el registro lanza un error 
    # se debe implementar un try y un except
    # try:
    #     user = User.select().where(User.username == 'user1').get()
    #     print(type(user)) # un objeto del tipo User
    #     print(user) # el user
        
    # except User.DoesNotExist as err:
    #     print('No fue posible obtener al usuario!')
    
    ##### Método más práctico, first, 
    ##### pero más recomendado por código Pythonico el método get
        
    # con first, si no obtiene el registro retorna None
    # no lanza excepciones no hace falta un try y un except
    user = User.select().where(User.username == 'user1').first()
    print(type(user)) # un objeto del tipo User
    print(user) # el user    
    
    if user:
        print(user)
    else:
        print('No fue posible obtener al usuario!')
        
        
        
        
        
        
    
    
    
    
    
    
    
    