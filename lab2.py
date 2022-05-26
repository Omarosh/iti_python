import mysql.connector
from mysql.connector import Error

    
       
class Person:
  def __init__(self, full_name, money, sleepmood, healthRate):
    self.full_name = full_name
    self.money = money
    self.sleepmood = sleepmood
    if healthRate>=0 and healthRate <= 100:
      self.healthRate = healthRate

  def sleep():
    print("sleep")
  
  def eat():
    print("eat")
  
  def buy():
    print("buy")




class Employee(Person):
  def __init__(self, id, email, workmood, salary,is_manager):
    self.id = id
    self.email = email
    self.salary = salary if salary>=1000 else 1000
    self.workmood = workmood
    self.is_manager = is_manager

  def sleep(hours):
    if hours == 7:
      print( "happy")
    elif hours < 7:
      print( "tired")
    elif hours > 7:
      print( "lazy")

  def eat(self, meals):
    if meals == 3:
      self.healthRate = 100 
    elif meals == 2:
      self.healthRate = 75
    elif meals == 1:
      self.healthRate = 50

  def buy(self, items): 
    self.money -= len(items) *10
  
  def sendEmail(self, to, suject,body,receiver_name):
    print("Saved email in file")

  def work(self, hours):
    if hours == 8:
      print( "happy")
    elif hours > 8:
      print( "tired")
    elif hours < 8:
      print( "lazy")

  #For printing the emp object
  def __str__(self):
      return f"({self.id}) " + self.email + ", " + self.workmood



class Office :
  def __init__(self, name,employees):
    self.name = name
    self.employees = employees

    
  def get_all_employees(self):
    query = "select * from employees"
    cursor = connection.cursor(buffered=True)
    cursor.execute(query)
    records = cursor.fetchall()
    newList = []
    for record in records:
        emp = Employee(record[0], record[1], record[2], record[3], record[4])
        newList.append(emp)
    self.employees = newList
    
  def print_all_employees(self):
    print("get_all_employees")
    for e in  self.employees:
      print(e)  
      
  def get_employee(self,id):
    id = int(id)
    self.get_all_employees()
    for emp in self.employees:
        if emp.id == id:
            print("Found!")
            return emp
    return "not found"

  def fire(self, id):
      query = f"DELETE FROM employees WHERE id={id};"
      try:
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        connection.commit()
      except Error as e:
        print(e)

  def hire(self,employee):
    print(employee)
    self.employees.append(employee)
    query = f"insert into employees ( email ,  salary , is_manager) VALUES ('{employee.email}' , {employee.salary}, {1 if employee.is_manager else 0})"
    print(query)
    try:
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(e)

def connect():
    try:
        connection = mysql.connector.connect(host='localhost',
                                              database='iti_python',
                                              user='root',
                                              password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection
        
    except Error as e:
        print("Error while connecting to MySQL", e)
def disconnect(connection):
      if connection.is_connected():
            cursor = connection.cursor()  
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def main():
    flag = True
    office = Office("ITI" , [])
 
    global connection  
    connection = connect()
    
    cursor = connection.cursor(buffered=True)
    cursor.execute("select * from employees")
    record = cursor.fetchall()
    print(record)
   
    while(flag):
      print("\n===============")
      print("LAB 2 PYHTON")
      print("1- Hire \n2- get_employee by id\n3- get_all_employees\n4-Fire \nq- Quit")
      choice = input("Enter choice:")
      choice = int(choice) if choice.isnumeric() else "q"
      if choice == 1:
          print("===Hire===\n\n-mngr (If this employee is a a manager)\n-nrml (If this employee is normal)")
          
          is_manager = True if input("Enter choice: ") == "mngr" else False
          email = input("Enter email: ")
          salary = -1
          if not is_manager:
              salary = int(input("Enter salary: "))
          emp = Employee(0, email, "", salary, is_manager)
          office.hire(emp)
          print("Hired!")
      elif choice == 2:
          print("===get_employee by id===\n\n")
          emp_id = input("Enter id")
          emp = office.get_employee(emp_id)
          print(emp)
      elif choice == 3:
          print("===get_all_employees===\n\n")
          emp = office.get_all_employees()
          print(emp)
      elif choice == 4:
          print("===Fire===\n\n")
          office.fire(input("Enter employee id to fire: "))
          print("Fired!")
      elif choice == "q":
          print("Quitting")
          flag = False
      else:
          print("ERROR")
    disconnect(connection)

main()
