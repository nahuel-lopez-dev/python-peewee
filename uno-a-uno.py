import peewee

database = peewee.MySQLDatabase('pythonpeewee', 
    host='localhost', 
    port=3306, 
    user='root', 
    passwd='password')


class User(peewee.Model()):
    username = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=50)

    class Meta:
        database = database
        db_table = 'users'

        def __str__(self):
            return self.username
        
        @property
        def admin(self):
            return self.admins.first()

class Admin(peewee.Model()):
    permission_level = peewee.IntegerField(default=1)
    user = peewee.ForeignKeyField(User, backref='admins', unique=True) # el plural del modelo como regla

    class Meta:
        database = database
        db_table = 'admins'
        
    def __str__(self):
        return 'Admin' + str(self.id)    
    
    
if __name__ == '__main__':
    
    
    
    database.drop_tables([User, Admin])
    database.create_tables([User, Admin])
    
    user1 = User.create(username='User1', email='user1@example.com')
    admin1 = Admin.create(permission_level=10, user=user1)
    
    # print(admin1.user.email)
    print(user1.admin) # user1.admin
    
    
    
    
    

