from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.employee_service import EmployeeService

employee_bp = Blueprint("employee", __name__)


# Dashboard
@employee_bp.route("/")
def dashboard():

    keyword = request.args.get("search")

    if keyword:
        employees = EmployeeService.search_employee(keyword)
    else:
        employees = EmployeeService.get_all_employees()

    total = EmployeeService.get_total_employees()

    return render_template(
        "dashboard.html",
        employees=employees,
        total=total
    )


# Add Employee
@employee_bp.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":

        EmployeeService.add_employee(
            request.form["name"],
            request.form["email"],
            request.form["phone"],
            request.form["department"],
            request.form["designation"],
            request.form["salary"],
            request.form["joining_date"]
        )

        flash("Employee added successfully!", "success")

        return redirect(url_for("employee.dashboard"))

    return render_template("add_employee.html")


# Edit Employee
@employee_bp.route("/edit/<int:employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):

    employee = EmployeeService.get_employee_by_id(employee_id)

    if not employee:
        return "Employee Not Found", 404

    if request.method == "POST":

        EmployeeService.update_employee(
            employee_id,
            request.form["name"],
            request.form["email"],
            request.form["phone"],
            request.form["department"],
            request.form["designation"],
            request.form["salary"],
            request.form["joining_date"]
        )

        flash("Employee updated successfully!", "success")

        return redirect(url_for("employee.dashboard"))

    return render_template(
        "edit_employee.html",
        employee=employee
    )


# Delete Employee
@employee_bp.route("/delete/<int:employee_id>")
def delete_employee(employee_id):

    EmployeeService.delete_employee(employee_id)

    flash("Employee deleted successfully!", "success")

    return redirect(url_for("employee.dashboard"))