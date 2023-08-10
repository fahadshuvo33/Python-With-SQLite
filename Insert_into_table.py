import sqlite3

conn = sqlite3.connect('Sample_1.db')
cursor = conn.cursor()

def insert(sub, price, publisher, page):
    ins = f'''INSERT INTO Book_List(Subject, Book_Price, Publisher, Book_Pages)
              VALUES ('{sub}', {price}, '{publisher}', {page})'''

    cursor.execute(ins)
    conn.commit()

insert("Bangla 1st Paper", 250, "NCTB", 350)
insert("Bangla 2nd Paper", 588, "The Atlas Publishing House", 1422)
insert("English 1st Paper", 250, "NCTB", 350)
insert("English 2nd Paper", 700, "Chowdhury and Hossain", 1950)
insert("Information and Communication Technology", 310, "Systech Publications", 616)

insert("Physics 1st Paper", 350, "Hasan Book House", 744)
insert("Physics 2nd Paper", 365, "Hasan Book House", 708)
insert("Chemistry 1st Paper", 390, "Lecture Publications", 704)
insert("Chemistry 2nd Paper", 370, "Lecture Publications", 940)
insert("Biology 1st Paper", 315, "Gazi Publishers", 316)
insert("Biology 2nd Paper", 360, "Gazi Publishers", 428)
insert("Higher Math 1st Paper", 184, "Alpha Publications", 484)
insert("Higher Math 2nd Paper", 155, "Alpha Publications", 426)

conn.close()
