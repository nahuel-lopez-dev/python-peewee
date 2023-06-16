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
    
    ##### 1. Insertando con el método save()
    # requiere de un objeto
    
    # pasando por parámetros
    user1 = User(username='user1', email='user1@gmail.com', active=True)
    print(user1.active)
    
    user1.save()
    
    # insertando las propiedades con los valores
    user2 = User()
    user2.username = 'user2'
    user2.email = 'user2@gmail.com'
    
    user2.save()
    
    # creando un diccionario
    values = {
        'username': 'user3',
        'email': 'user3@gmail.com'
    }
    
    user3 = User(**values)
    user3.save()
    
    ##### 2. Insertando con el método create de clase
    # crea un objeto, lo persiste en la tabla, y lo retorna
    user4 = User.create(username='user4', email='user4@gmail.com')
    print(user4.id)
    
    ##### 3. Insertando con el método insert, es un método de clase
    # retorna una query
    query = User.insert(username='user5', email='user5@gmail.com')
    print(query)
    print(type(query)) # ModelInsert
    
    query.execute()
    
    
    
    
    
    
    
    
    
    
    
    
