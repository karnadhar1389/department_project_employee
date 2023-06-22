from flask import Flask, jsonify, render_template, request, redirect
import csv

app = Flask(__name__)

# Sample data
departments = []
employees = []
projects = []

# Load data from CSV files
def load_data_from_csv():
    load_departments()
    load_employees()
    load_projects()

def load_departments():
    with open('departments.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            departments.append({'id': int(row['id']), 'name': row['name']})

def load_employees():
    with open('employees.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append({
                'email': row['email'],
                'lastname': row['lastname'],
                'firstname': row['firstname'],
                'age': int(row['age']),
                'department_id': row['department_id']
            })

def load_projects():
    with open('projects.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            projects.append({
                'id': int(row['id']),
                'name': row['name'],
                'client': row['client'],
                'department_id': row['department_id']
            })

# Routes for importing data from CSV files
@app.cli.command()
def import_data():
    load_data_from_csv()
    print('Data imported successfully.')

# Routes for webpages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/departments')
def department_list():
    return render_template('department_list.html', departments=departments)

@app.route('/departments/<int:department_id>')
def department_detail(department_id):
    department = next((dept for dept in departments if dept['id'] == department_id), None)
    if department:
        department_employees = [emp for emp in employees if emp['department_id'] == department_id]
        return render_template('department_detail.html', department=department, employees=department_employees)
    return render_template('404.html')

@app.route('/employees')
def employee_list():
    return render_template('employee_list.html', employees=employees)

@app.route('/employees/<email>')
def employee_detail(email):
    employee = next((emp for emp in employees if emp['email'] == email), None)
    if employee:
        return render_template('employee_detail.html', employee=employee)
    return render_template('404.html')

# Route for the employee detail page with edit option
@app.route('/employees/<email>/edit')
def edit_employee(email):
    employee = next((e for e in employees if e['email'] == email), None)

    if employee:
        return render_template('employee_edit.html', employee=employee)
    else:
        return render_template('404.html'), 404

# Route for handling employee edit form submission
@app.route('/employees/<email>', methods=['POST'])
def update_employee(email):
    employee = next((e for e in employees if e['email'] == email), None)

    if employee:
        employee['lastname'] = request.form['lastname']
        employee['firstname'] = request.form['firstname']
        employee['age'] = int(request.form['age'])
        employee['department_id'] = request.form['department_id']
#        url = f'/employees/' + email
        url = f'/employees'
        return redirect(url)
    else:
        return render_template('404.html'), 404

@app.route('/projects')
def project_list():
    return render_template('project_list.html', projects=projects)

@app.route('/statistics')
def department_statistics():
    department_project_count = {}
    for department in departments:
#        department_id = department['id']
        department_id = department['name']
        project_count = sum(1 for project in projects if project['department_id'] == department_id)
        department_project_count[department_id] = project_count

    return render_template('statistics.html', department_project_count=department_project_count)

# REST API routes
@app.route('/api/employees', methods=['GET'])
def get_all_employees():
    return jsonify(employees)

@app.route('/api/employees/<key_field>', methods=['GET'])
def get_employee(key_field):
    field_names = ['email']  # Add more fields if needed
    employee = next((emp for emp in employees if emp[field_names[0]] == key_field), None)
    if employee:
        return jsonify(employee)
    return jsonify({'error': 'Employee not found'})

@app.route('/api/employees', methods=['POST'])
def create_employee():
    employee_data = request.get_json()
    if 'email' in employee_data:
        employee = next((emp for emp in employees if emp['email'] == employee_data['email']), None)
        if employee:
            return jsonify({'error': 'Employee with the provided email already exists'})
    else:
        return jsonify({'error': 'Email field is required'})

    employees.append(employee_data)
    return jsonify({'message': 'Employee created successfully'})

# REST API route for deleting an employee by email
@app.route('/api/employees/<email>', methods=['DELETE'])
def delete_employee(email):
    employee = next((e for e in employees if e['email'] == email), None)

    if employee:
        employees.remove(employee)
        return jsonify({'message': 'Employee deleted successfully'})
    else:
        return jsonify({'error': 'Employee not found'})

if __name__ == '__main__':
    load_data_from_csv()
    app.run(debug=True, host='localhost', port=9874)
