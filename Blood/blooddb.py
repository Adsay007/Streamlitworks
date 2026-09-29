import mysql.connector

class BloodCRUD:
    def __init__(self):
        self.connection = mysql.connector.connect( 
            user="root", 
            password="12345", 
            host="localhost", 
            database="blooddb"
        )
        print(self.connection)
        self.cursor = self.connection.cursor()
        print("Successfully connected")

    def list(self):
        query = "select * from donor" 
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        if records:
            for row in records:
                print(row)
            return records
        else:
            print("No records Found")
            return[]

    def create(self, name, bloodgroup, phone, city, last_donation):
        query = "insert into donor(name, bloodgroup, phone, city, last_donation) values (%s, %s, %s, %s, %s)" 
        data = (name, bloodgroup, phone, city, last_donation)
        self.cursor.execute(query, data) 
        self.connection.commit()
        print("Inserted Data Successfully")

    def retrieve(self, id):
        query = "select * from donor where id=%s" 
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
        query = "delete from donor where id=%s" 
        data = (id,)
        self.cursor.execute(query, data) 
        self.connection.commit()
        
        if self.cursor.rowcount > 0:
            return True
        else:
            return False

    def update(self, id, name, bloodgroup, phone, city, last_donation):
        query = "update donor set name=%s, bloodgroup=%s, phone=%s, city=%s, last_donation=%s where id=%s" 
        data = (name, bloodgroup, phone, city, last_donation, id)
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