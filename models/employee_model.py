import sqlite3
from config import DATABASE


class EmployeeModel:

    @staticmethod
    def get_connection():
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def create_table():
        conn = EmployeeModel.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            department TEXT NOT NULL,
            designation TEXT NOT NULL,
            salary REAL NOT NULL,
            joining_date TEXT NOT NULL

        )
        """)

        conn.commit()
        conn.close()

    @staticmethod
    def add_employee(name, email, phone, department,
                     designation, salary, joining_date):

        conn = EmployeeModel.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO employees
        (name, email, phone, department, designation, salary, joining_date)

        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            name,
            email,
            phone,
            department,
            designation,
            salary,
            joining_date
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_employees():

        conn = EmployeeModel.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM employees
        ORDER BY id DESC
        """)

        employees = cursor.fetchall()

        conn.close()

        return employees

    @staticmethod
    def get_total_employees():

        conn = EmployeeModel.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*) AS total
        FROM employees
        """)

        total = cursor.fetchone()["total"]

        conn.close()

        return total

    @staticmethod
    def get_employee_by_id(employee_id):

        conn = EmployeeModel.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM employees
        WHERE id = ?
        """, (employee_id,))

        employee = cursor.fetchone()

        conn.close()

        return employee

    @staticmethod
    def update_employee(employee_id, name, email, phone,
                        department, designation,
                        salary, joining_date):

        conn = EmployeeModel.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        UPDATE employees
        SET
            name = ?,
            email = ?,
            phone = ?,
            department = ?,
            designation = ?,
            salary = ?,
            joining_date = ?
        WHERE id = ?
        """, (
            name,
            email,
            phone,
            department,
            designation,
            salary,
            joining_date,
            employee_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_employee(employee_id):

        conn = EmployeeModel.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM employees
        WHERE id = ?
        """, (employee_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def search_employee(keyword):

        conn = EmployeeModel.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM employees
        WHERE
            name LIKE ?
            OR email LIKE ?
            OR department LIKE ?
        ORDER BY id DESC
        """, (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        ))

        employees = cursor.fetchall()

        conn.close()

        return employees