import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "test_db"
)

mycursor = db.cursor()

first_name = input("First name   : ")
last_name = input("Last name     : ")
hourly_pay = float(input("Hourly pay    : "))

mycursor.execute("""
    INSERT INTO employees (first_name, last_name, hourly_pay, hire_date)
    VALUES (%s, %s, %s, NOW())
""", (first_name, last_name, hourly_pay))

db.commit()


# mycursor.execute("""
#     CREATE TABLE employees(
#         employee_id INT PRIMARY KEY AUTO_INCREMENT,
#         first_name VARCHAR(50) NOT NULL,
#         last_name VARCHAR(50) NOT NULL,
#         hourly_pay DECIMAL(3,2),
#         hire_date DATE
#     );
# """)