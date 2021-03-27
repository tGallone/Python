import sqlite3
import json
     
def connect():
    conn=sqlite3.connect("books2.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title nvarchar(100), author nvarchar(100), year integer, isbn integer)")
    conn.commit()
    conn.close()    

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books2.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("books2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows 
    
# def truncate():
#     conn=sqlite3.connect("books2.db")
#     cur=conn.cursor()
#     cur.execute("DELETE from book")
#     conn.commit()
#     conn.close()

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book where title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books2.db")
    cur=conn.cursor()
    cur.execute("DELETE from book where id = ?",(id,))
    conn.commit()
    conn.close()
    
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books2.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title = ?, author=?, year=?, isbn=? where id = ?",(title,author,year,isbn,id))
    conn.commit()
    rows=cur.fetchall()
    conn.close()

connect()

# truncate()
# insert("sample1","def",2003,123457)
# insert("sample2","def",2003,123457)

