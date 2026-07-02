from models.employee_model import EmployeeModel


class EmployeeService:

    @staticmethod
    def initialize_database():
        EmployeeModel.create_table()

    @staticmethod
    def add_employee(name, email, phone,
                     department, designation,
                     salary, joining_date):

        EmployeeModel.add_employee(
            name,
            email,
            phone,
            department,
            designation,
            salary,
            joining_date
        )

    @staticmethod
    def get_all_employees():
        return EmployeeModel.get_all_employees()

    @staticmethod
    def get_total_employees():
        return EmployeeModel.get_total_employees()

    @staticmethod
    def get_employee_by_id(employee_id):
        return EmployeeModel.get_employee_by_id(employee_id)

    @staticmethod
    def update_employee(employee_id, name, email, phone,
                        department, designation,
                        salary, joining_date):

        EmployeeModel.update_employee(
            employee_id,
            name,
            email,
            phone,
            department,
            designation,
            salary,
            joining_date
        )

    @staticmethod
    def delete_employee(employee_id):
        EmployeeModel.delete_employee(employee_id)

    @staticmethod
    def search_employee(keyword):
        return EmployeeModel.search_employee(keyword)