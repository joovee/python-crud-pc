import pymysql
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='mobile_att',
)
print ("***WELCOME TO EXAMPLE***\n\n")
print ("[1] = Create a new data\n")
print ("[2] = Read data\n")
print ("[3] = Update data\n")
print ("[4] = Delete data\n")

choice = input("Choices: \n")


if choice == "1":
        First_Name = input("Enter Name: ")
        Last_Name = input("Enter Lastname: ")
        Middle_Initial = input("Enter you Middle Name: ")
        Name_Extension = input("Enter your Name_Extension: ")
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO student (`First_Name`,`Last_Name`,`Middle_Initial`,`Name_Extension`) VALUES (%s, %s, %s, %s);"
                try:
                    cursor.execute(sql, (First_Name,Last_Name,Middle_Initial,Name_Extension))
                    print("Student added successfully")
                except:
                    print("Oops! Something went wrong")
            connection.commit()
        finally:
            choice = 1

if choice =="2":
    try:
        with connection.cursor() as cursor:
            sql = "select * from student"
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            print("ID\tName\tMI\tName_Extension")
            print("---------------------------------------------------------------------------")
            for row in results :
                print(str(row[0]) + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] + "\t\t\t" + row[4])

        connection.commit()
    finally:
        print ("")

if choice =="3":
    print("")
    Student_ID = input("Enter   id: ")
    First_Name = input("Enter new Name: ")
    Last_Name = input("Enter new Last Name: ")
    Middle_Name = input("Enter new Middle_Name: ")
    Name_Extension = input("Enter new Name Extension: ")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE student SET `First_Name`=%s, `Last_Name`=%s, `Middle_Name`=%s, `Name_Extension`=%s WHERE `Student_ID` =%s"
            try:
                cursor.execute(sql, (First_Name, Last_Name, Middle_Initial, Name_Extension, Student_ID))
                print("Successfully Updated...")
            except:
                print("Oops! Something went wrong")
 
        connection.commit()
    finally:
        print ("")
