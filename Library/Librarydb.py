import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection = mysql.connector.connect( 
            user="root", 
            password="12345", 
            host="localhost", 
            database="Library_db"
        )
        print(self.connection)
        self.cursor = self.connection.cursor()
        print("Successfully connected")

    def list(self):
        query = "select * from book" 
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        if records:
            for row in records:
                print(row)
            return records
        else:
            print("No records Found")
            return[]

    def create(self, title, author, price, pages, language):
        query = "insert into book(title, author, price, pages, language) values (%s, %s, %s, %s, %s)" 
        data = (title, author, price, pages, language)
        self.cursor.execute(query, data) 
        self.connection.commit()
        print("Inserted Data Successfully")

    def retrieve(self, id):
        query = "select * from book where id=%s" 
        data = (id,)
        self.cursor.execute(query, data) 
        record = self.cursor.fetchone()
        
        if record:
            print(record)
            return record
        else:
            print("No record found")
            return None

    def delete(self, id):
        query = "delete from book where id=%s" 
        data = (id,)
        self.cursor.execute(query, data) 
        self.connection.commit()
        
        if self.cursor.rowcount > 0:
            return True
        else:
            return False

    def update(self, id, title, author, price, pages, language):
        query = "update book set title=%s, author=%s, price=%s, pages=%s, language=%s where id=%s" 
        data = (title, author, price, pages, language, id)
        self.cursor.execute(query, data) 
        self.connection.commit()
        
        if self.cursor.rowcount > 0:
            print("Updated Data successfully")
            return True
        else:
            print("No record Found")
            return False

#b = BookListCreateRetrieveUpdateDelete()

#b.list()
#b.create('ABC', "john", 300, 500, "English")
#b.retrieve(4)
#b.delete(4)
#b.update(id=5, title="STU", author="mike", price=300, pages=400, language="english")