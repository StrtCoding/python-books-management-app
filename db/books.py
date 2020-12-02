import sqlite3
from sqlite3 import Error
from .connection import create_connection


def insert_book(data):
    conn = create_connection()
    sql = """ INSERT INTO books (title, category, page_qty, book_path, description) 
                VALUES(?, ?, ?, ?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo libro agregado")
        return True, cur.lastrowid
    except Error as e:
        print("Errro Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def update_book(_id, data):
    conn = create_connection()

    sql = f""" UPDATE books SET  
                            title = ?,
                            category = ?,
                            page_qty = ?,
                            page_qty_read = ?,
                            book_path = ?,
                            description = ?
            WHERE book_id = {_id}

    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Libro Actualizado")
        return True
    except Error as e:
        print("Error updating book: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book(_id):
    conn = create_connection()
    sql = f"DELETE FROM books WHERE book_id = {_id}"


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books():
    conn = create_connection()
    sql = "SELECT * FROM books"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_id(_id):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE book_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchone()
        return book
    except Error as e:
        print("Error selecting book by id: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_title(title):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE title LIKE '%{title}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting book by title: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_category(category):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE category LIKE '%{category}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error Selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


