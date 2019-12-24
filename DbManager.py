
import sqlite3

class DbManager:
    def __init__(self):
        pass

    def init_table(self):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """
        CREATE TABLE users (
            login VARCHAR(20) PRIMARY KEY ,
            password VARCHAR(20)
        );
        """
        cursor.execute(request)
        connection.close()

    def init_table_tickets(self):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """
        CREATE TABLE tickets (
            login VARCHAR(20) PRIMARY KEY ,
            ticket VARCHAR(20), time VARCHAR(20)
        );
        """
        cursor.execute(request)
        connection.close()

    def registration(self, login, password):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = f'INSERT INTO users (login, password) VALUES ("{login}","{password}");'
        cursor.execute(request)
        connection.commit()
        connection.close()

    def registration_tickets(self, login, ticket, time):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = f'INSERT INTO tickets (login, ticket, time) VALUES ("{login}","{ticket}","{time}");'
        cursor.execute(request)
        connection.commit()
        connection.close()

    def read_table(self, login):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """
        SELECT login, password FROM users WHERE login=?;
        """
        cursor.execute(request, (login,))
        R = cursor.fetchone()
        connection.close()
        return R

    def read_table_tickets(self, ticket):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """
        SELECT login, time  FROM tickets WHERE ticket=?;
        """
        cursor.execute(request, (ticket,))
        R = cursor.fetchone()
        connection.close()
        return R


    def delete(self, login):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """DELETE FROM users WHERE login=?;"""
        
        cursor.execute(request, (login,))
        connection.commit()
        connection.close()

    def delete_tickets(self, ticket):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """DELETE FROM tickets WHERE ticket=?;"""
        
        cursor.execute(request, (ticket,))
        connection.commit()
        connection.close()

    def read_all_table(self):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """
        SELECT * FROM users ;
        """
        cursor.execute(request)
        RR = cursor.fetchall()
        
        connection.close()
        return RR

    def read_all_table_tickets(self):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """
        SELECT * FROM tickets ;
        """
        cursor.execute(request)
        RR = cursor.fetchall()
        
        connection.close()
        return RR


#a = DbManager()
#a.init_table_tickets()
#a.registration_tickets("log-bbb","tic-bbb","time-bbb")
#print(a.read_table_tickets("tic-aaa"))
#a.delete_tickets("tic-bbb")
#print(a.read_all_table_tickets())

#a.delete("bbb")
#print(a.read_all_table())



