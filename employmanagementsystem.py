# """
# 1. insert new employee ✅
# 2. update email id of employee ✅
# 3. delete employee on behalf of eid✅
# 4. search employee ✅
# 5. search according to dept no.✅
# 6. show all employees ✅
# 7. exit
# choice-

# """


import sqlite3 as dbms
import csv

conn = dbms.connect("Employmangement.db")
cur= conn.cursor()

def create_table():
    createTable = """
create table if not exists employee
(
eid int,
fname varchar(50),
lname varchar(50),
email varchar(50),
phone varchar(10),
hiredate varchar(10),
jobid varchar(10),
salary int,
comm varchar(5),
mid varchar(5),
did varchar(5)
);
"""
    cur.execute(createTable)
create_table()
def copy_csvfile():
    with open('employee.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute('''
                INSERT INTO employee (eid, fname, lname, email,phone,hiredate,jobid,salary,comm,mid,did) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (row['eid'], row['fname'],row['lname'], row['email'], row['phone'],row['hiredate'],row['jobid'],row['salary'],row['comm'],row['mid'],row['did']))

   
    conn.commit()


def insert_employee():
    msg = "eid, fname, lname, email,phone,hiredate,jobid,salary,comm,mid,did"
    lst = []
    for i in msg.split(","):
        lst.append(input(f"enter {i}"))
    insertQry = """
insert into employee values({}, '{}', '{}', '{}', '{}','{}','{}', '{}', '{}', '{}','{}')
""".format(*lst)
    cur.execute(insertQry)
    conn.commit()
    print(" Employee inserted successfully!")

def show_all_employee():
    # cur.execute("SELECT * FROM employee")
    # for row in cur.fetchall():
    #       print(row)
    # conn.close()
    selectquery = "SELECT * FROM employee"
    cur.execute(selectquery)
    result = cur.fetchall()
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*("eid", "fname", "lname", "email","phone","hiredate","jobid","salary","comm","mid","did")))
    for i in result:
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(*i))

def show_employee_by_eid():
    eid = input("Enter Employee ID (eid) to search: ")
    selectquery = "SELECT * FROM employee WHERE eid = ?"
    cur.execute(selectquery, (eid,))
    result = cur.fetchone()
    if result:
        print("\nEmployee Details:")
        # Print header
        print("{:<5} {:<10} {:<10} {:<25} {:<12} {:<12} {:<10} {:<8} {:<6} {:<6} {:<6}".format(
            "eid", "fname", "lname", "email", "phone", "hiredate", "jobid", "salary", "comm", "mid", "did"
        ))

        # Print the employee record
        print("{:<5} {:<10} {:<10} {:<25} {:<12} {:<12} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*result))
    else:
        print(" No employee found with eid =", eid)
    
def show_employees_by_did():
    did = input("Enter Employee DID (did) to search: ") 
    selectquery = "SELECT * FROM employee WHERE did = ?"
    cur.execute(selectquery, (did,))
    results = cur.fetchall()  

    if results:
        print("\nEmployees in Department ID:", did)
      
        print("{:<5} {:<10} {:<10} {:<25} {:<12} {:<12} {:<10} {:<8} {:<6} {:<6} {:<6}".format(
            "eid", "fname", "lname", "email", "phone", "hiredate", "jobid", "salary", "comm", "mid", "did"
        ))

        for result in results:
            print("{:<5} {:<10} {:<10} {:<25} {:<12} {:<12} {:<10} {:<8} {:<6} {:<6} {:<6}".format(*result))
    else:
        print(" No employees found in department with did =", did)

def delete_employee():
    eid = input("enter eid of the employee")
    deletequery = "DELETE FROM employee where eid = ?"
    cur.execute(deletequery,(eid,))
    conn.commit() 
    
    if cur.rowcount > 0:
        print(f" Employee with eid {eid} has been deleted.")
    else:
        print(f" No employee found with eid {eid}.")

def update_email():
    eid = input("enter eid of employee to update email")  
    email = input("enter updated email : ")
    
    updatequery =f"update employee set email = '{email}' where eid = {eid}"
    cur.execute(updatequery)
    conn.commit()
    if cur.rowcount > 0:
        print(f" Email for employee with eid {eid} has been updated.")
    else:
        print(f" No employee found with eid {eid}.")


while (True):
    choice =int ( input("""
    welcome to the student management system
    main menu
    1. insert new employee ✅
    2. update email id of employee ✅
    3. delete employee on behalf of eid✅
    4. search employee ✅
    5. search according to dept no.✅
    6. show all employees ✅
    7. exit

    enter your choice :- """))
    if (choice == 1) :
        insert_employee()
    elif choice == 2:
        update_email()
    elif choice == 3 :
        delete_employee()
    elif choice == 4 :
        show_employee_by_eid()
    elif choice == 5 :
        show_employees_by_did()
    elif choice == 6 :
        show_all_employee()
    elif choice == 7 :
        break
    else :
        print("Invalid choice")

cur.close()
conn.close()