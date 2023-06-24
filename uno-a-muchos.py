import peewee
from datetime import datetime

database = peewee.MySQLDatabase('pythonpeewee', 
    host='localhost', 
    port=3306, 
    user='root', 
    passwd='password')

class Author(peewee.Model):
    name = peewee.CharField(max_length=50)
    
    class Meta:
        database = database
        db_table = 'authors'
        
    def __str__(self):    
        return self.name

class Book(peewee.Model):
    title = peewee.CharField(max_length=50)
    author = peewee.ForeignKeyField(Author, backref='books')
    
    class Meta:
        database = database
        db_table='books'
        
    def __str__(self):
        return self.title

if __name__ == '__main__':
    
    database.drop_tables([Author, Book])
    database.create_tables(Author, Book)
    
    author1 = Author.create(name='Stephen King')
    
    book1 = Book.create(title='It 1', author=author1)
    book2 = Book.create(title='It 2', author=author1)
    book3 = Book.create(title='It 3', author=author1)
    
    print(book2.author)
    print(author1.books)
    
    for book in author1.books:
        print(book)
    
    
    
    
    
    
    
    




    
    
    