import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE = os.path.join(BASE_DIR, "database", "employees.db")

SECRET_KEY = "employee-management-secret-key"