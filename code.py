import re
import mysql.connector
from tabulate import tabulate


database = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="",
        database ="db_akademik_0580"
)

connector = database.cursor()



def sedata():
        selector = ("SELECT * FROM tbl_students_0580")
        connector.execute(selector)
        result = connector.fetchall()
        print(tabulate(result, headers=['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'], tablefmt='psql'))
        print('')
def limit():
        input_limit = input("Masukkan limit: ")
        print('')
        hasil_seleksi = ("SELECT * FROM tbl_students_0580 LIMIT %s"% input_limit)
        connector.execute(hasil_seleksi)
        result = connector.fetchall()
        result1 = (tabulate(result, headers=['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'], tablefmt='psql'))
        print (result1)
def nim():
        cari_nim = input("Masukkan NIM: ")
        print('')
        format_seleksi = ("SELECT * FROM tbl_students_0580 WHERE nim = '{}';" .format(cari_nim))
        connector.execute(format_seleksi)
        result = connector.fetchall()
        print(tabulate(result, headers=['No.', 'NIM', 'Nama', 'JK', 'Jurusan', 'Alamat'], tablefmt='psql'))    
        print('')

while True:
    print("""
1. Tampilkan semua data
2. Tampilkan data berdasarkan limit
3. Cari berdasarkan NIM
0. Keluar
        """)
    input_menu = int(input("Masukkan Inputan Anda : "))
    if  input_menu == 1: 
        sedata()
    elif input_menu == 2:
        limit()
    elif input_menu == 3:
        nim()
    elif input_menu == 0:    
        database.close()
        exit()
   
