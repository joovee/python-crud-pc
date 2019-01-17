import pymysql
import sys
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='personal collection',
)

def add():
    particular = input("Enter particular: ")
    items = input("Enter items: ")
    unit = input("Enter unit: ")
 
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO product (`particular`,`items`,`unit`) VALUES (%s, %s, %s)"
            try:
                cursor.execute(sql, (particular, items, unit))
                print("Task added successfully")
            except:
                print("Oops! Something wrong")
                
        connection.commit()
    finally:
        print ("\n")
        return

def read():
    print ("product\n")
    try:
        with connection.cursor() as cursor:
            sql = "select * from product"
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            print("id\tparticular\t\titems\t\t\t\tunit")
            print("---------------------------------------------------------------------------")
            for row in results :
                print(str(row[0]) + "\t" + row[1] + "\t\t\t" + (row[2]) + "\t\t\t\t" , row[3])

        connection.commit()
    finally:
        print ("")
        return
def update():
    read()
    print("")
    product_id = input("Enter   id: ")
    particular = input("Enter new particular: ")
    items = input("Enter new items: ")
    unit = input("Enter new unit: ")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE product SET `particular`=%s, `items`=%s, `unit`=%s WHERE `product_id` =%s"
            try:
                cursor.execute(sql, (particular, items, unit, product_id))
                print("Successfully Updated...")
            except:
                print("Oops! Something wrong")
 
        connection.commit()
    finally:
        print ("")
        return
def delete():
    read()
    print("")
    product_id = input("Enter the id product: ")
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM product WHERE product_id = %s"
            try:
                cursor.execute(sql, (product_id))
                print("Successfully Deleted...")
            except:
                print("Oops! Something wrong")
 
        connection.commit()
    finally:
        print ("")
        return
def exit():
    sys.exit(0)

balik = 1
while balik:
    print (" \t\tPersonal Collection")
    print ("A => Create Product") 
    print ("B ---> Read Product")
    print ("C ---> Update Product")
    print ("D ---> Delete Product")
    print ("E ---> Exit")
    

    balik = input("Please Enter the letter of your choices: ")

    if balik in ('Aa'):
        add()
    elif balik in ('Bb'):
        read()
    elif balik in ("Cc"):
        update()
    elif balik in ("Dd"):
        delete()
    elif balik in ("Ee"):
        exit()

    else:
        print ("Invalid Input!\n")
        balik = 1
