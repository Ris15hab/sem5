import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='pass@123'
)

mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE student_details')

print("\n\n\nshow databases\n\n\n")

mycursor.execute('SHOW DATABASES')
for  x in mycursor:
    print(x)

mycursor.execute('USE student_details')

mycursor.execute('''CREATE TABLE student_info(
                 id int primary key,
                 name varchar(55),
                 email varchar(55),
                 phone varchar(55)
)''')

print("\n\n\nshow tables\n\n\n")

mycursor.execute('SHOW TABLES')
for  x in mycursor:
    print(x)

mycursor.execute('''INSERT INTO student_info VALUES
                 (1,'student1','student1@gmail.com','8889997777')
''')
mydb.commit()

print("\n\n\nselect * from student_info\n\n\n")
mycursor.execute('SELECT * FROM student_info')

for  x in mycursor:
    print(x)