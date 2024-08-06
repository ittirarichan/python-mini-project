import mysql.connector

st = mysql.connector.connect(
    host="localhost",
    user="Abhishek", 
    password="@Abhishek2003"
)

cursor = st.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS student_registration')
cursor.execute('USE student_registration')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_registeration (
        std_id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        email VARCHAR(100),
        number INT,       
        course VARCHAR(100)  -- corrected datatype for course
    )
''')

while True:
    print('\n1.add\n2.update\n3.delete\n4.search\n5.view all\n6.group by\n7.order by\n8.like\n9.exit')
    ch = int(input('Enter your choice: '))

    if ch == 1:
        l = int(input("Enter number of students: "))
        for i in range(l):
            id = int(input('Enter student ID: '))
            name = input('Enter name: ')
            age = int(input('Enter age: '))
            email = input('Enter email: ')
            num = int(input('Enter phone number: '))
            cus = input('Enter course: ')

            cursor.execute('INSERT INTO student_registeration (std_id, name, age, email, number, course) VALUES (%s, %s, %s, %s, %s, %s)',
                           (id, name, age, email, num, cus))
            st.commit()

    elif ch == 2:
        id = int(input('Enter ID of student: '))
        name = input('Enter new name: ')
        age = int(input('Enter new age: '))
        email = input('Enter new email: ')
        num = int(input('Enter new phone number: '))  # changed to int
        cus = input('Enter new course: ')
        cursor.execute('UPDATE student_registeration SET name=%s, age=%s, email=%s, number=%s, course=%s WHERE std_id=%s',
                       (name, age, email, num, cus, id))
        st.commit()

    elif ch == 3:
        id = int(input('Enter ID of student to delete: '))
        cursor.execute('DELETE FROM student_registeration WHERE std_id=%s', (id,))
        st.commit()

    elif ch == 4:
        id = int(input('Enter ID to search: '))
        cursor.execute('SELECT * FROM student_registeration WHERE std_id=%s', (id,))
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}'.format('ID', 'Name', 'Age', 'Email', 'Number', 'Course'))
        print('-' * 65)
        if data:
            for i in data:
                print("{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}".format(i[0], i[1], i[2], i[3], i[4], i[5]))
        else:
            print('ID not available')

    elif ch == 5:
        cursor.execute('SELECT * FROM student_registeration')
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}'.format('ID', 'Name', 'Age', 'Email', 'Number', 'Course'))
        print('-' * 65)
        if data:
            for i in data:
                print("{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}".format(i[0], i[1], i[2], i[3], i[4], i[5]))

    elif ch == 6:
        cursor.execute('SELECT * FROM student_registeration GROUP BY name')
        data = cursor.fetchall()
        for i in data:
            print(i)

    elif ch == 7:
        cursor.execute('SELECT * FROM student_registeration ORDER BY course')
        data = cursor.fetchall()
        for i in data:
            print(i)

    elif ch == 8:
        a = input("Enter the first letter of name you want to search: ") + '%'
        cursor.execute('SELECT * FROM student_registeration WHERE name LIKE %s', (a,))
        data = cursor.fetchall()
        print('{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}'.format('ID', 'Name', 'Age', 'Email', 'Number', 'Course'))
        print('-' * 85)
        for i in data:
            print("{:<10}{:<10}{:<10}{:<10}{:<20}{:<15}".format(i[0], i[1], i[2], i[3], i[4], i[5]))

    elif ch == 9:
        break
    else:
        print('Invalid choice.')

cursor.close()
st.close()