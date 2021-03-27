import sqlite3

def connect():
    conn=sqlite3.connect("books1.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year int,isbn int)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books1.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book ")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
insert("sample","abc",2003,123456)
insert("sample2","def",2003,123457)
print(view())