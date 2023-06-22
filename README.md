# department_project_employee

Task is as below 
Programming Task Python
Create a webserver in python (feel free to use any python frameworks you want).  
The webserver should fulfil the following functions:
-	Implement a data model with CRUD capability (see ER diagram below and CSV files)
-	Import of the given csv data (the import can be CLI based)
-	Create and serve webpages:
o	Overview for all entities: a table or list of all instances
o	Detail (only for employees): a detailed view of one instance (optionally edit the instance)
-	Create a webpage showing at least the following statistical information:
o	Number of Projects per department
-	Create a REST API for the employee entity with at least the following capabilities:
o	HTTP GET: List of all employees
o	HTTP GET: Get a specific employee by a key field of your choosing
o	Create an employee with HTTP POST
Please upload your code into a git repository and share it to us. Provide a documentation how to run and execute the code. Please upload your final code at least two hours before your interview.
If something is unclear or you have questions, please contact us.
ER-Diagram: 1:N relationship for Department:Employee
	And 1:N relationship for Department:Proejct
Department contains id, name
Employee contains email,lastname,firstname,age
Project contains id,name,client


And to run the code use word file name Task4 or see below 
To access the different functionalities, you can use the following URLs:

Overview for all entities: http://localhost:9874/departments
Detail view for an employee: http://localhost:9874/employees/{email}
Statistical information: http://localhost:9874/statistics
REST API for all employees: http://localhost:9874/api/employees
REST API for a specific employee: http://localhost:9874/api/employees/{key_field}
Create an employee using the REST API: Send a POST request to http://localhost:9874/api/employees with the employee data in the request body as JSON.
To edit individual employee:- http://localhost:9874/employees/{email}
 Example http://localhost:9874/employees/SCosins@phoenixcontact.com
we added a new route /employees/<email>/edit that renders the employee_edit.html template, passing the employee data to the template. The template includes an HTML form for editing the employee details.
When the form is submitted (POST request to /employees/<email>), we retrieve the updated employee data from the form and update the corresponding employee in the employees list. Finally, we redirect the user back to the employee detail page (/employees/<email>).



