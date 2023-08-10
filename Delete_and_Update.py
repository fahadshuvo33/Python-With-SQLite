import sqlite3

conn = sqlite3.connect('Sample_1.db')
cursor = conn.cursor()

# Update a Book Info 
def update_book_by_name(book_name, price, publisher, page):
    update_sql = f'''
        UPDATE Book_List
        SET Book_Price = {price}, Publisher = '{publisher}', Book_Pages = {page}
        WHERE Subject = '{book_name}'
    '''
    cursor.execute(update_sql)
    conn.commit()

# Delete a Book Details
def delete_book_by_name(book_name):
    delete_sql = f'''
        DELETE FROM Book_List
        WHERE Subject = '{book_name}'
    '''
    cursor.execute(delete_sql)
    conn.commit()

update_book_by_name('Physics 1st Paper', 370, "Ideal Books", 810)
update_book_by_name('Chemistry 1st Paper', 400, "Abacas Publications", 528)
update_book_by_name('Biology 2nd Paper', 315, "Hasan Book House", 316)

delete_book_by_name('Higher Math 1st Paper')
delete_book_by_name('Higher Math 2nd Paper')

conn.close()
