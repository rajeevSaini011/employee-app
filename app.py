from flask import Flask, flash
from config import SECRET_KEY
from services.employee_service import EmployeeService
from routes.employee_routes import employee_bp

app = Flask(__name__)

# Application Configuration
app.config["SECRET_KEY"] = SECRET_KEY

# Initialize Database
EmployeeService.initialize_database()

# Register Routes
app.register_blueprint(employee_bp)

# Run Application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)