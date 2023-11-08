class Employee:
    def __init__(self, name, salary, id):
        self.name = name
        self.salary = salary
        self.id = id

    def change_salary(self, new_salary):
        self.salary = new_salary

    def print_info(self):
        print("Employee Name: ", self.name)
        print("Employee Salary: ", self.salary)
        print("Employee ID: ", self.id)


class Manager(Employee):
    def __init__(self, name, id, department):
        self.name = name
        self.salary = 5000
        self.id = id
        self.department = department
        self.number_of_employees = 0

    def add_employee(self):
        self.number_of_employees += 1

    def remove_employee(self):
        self.number_of_employees -= 1

    def print_info(self):
        print("Manager Name: ", self.name)
        print("Manager Salary: ", self.salary)
        print("Manager ID: ", self.id)
        print("Manager Department: ", self.department)
        print("Manager Employees: ", self.number_of_employees)


class Engineer(Employee):
    def __init__(self, name, id, department, domain, project, manager):
        self.name = name
        self.salary = 4000
        self.id = id
        self.project = project
        self.domain = domain
        self.department = department
        self.manager = manager

    def change_project(self, new_project):
        self.project = new_project

    def change_domain(self, new_domain):
        self.domain = new_domain

    def change_department(self, new_department):
        self.department = new_department

    def change_manager(self, new_manager):
        self.manager = new_manager

    def print_info(self):
        print("Engineer Name: ", self.name)
        print("Engineer Salary: ", self.salary)
        print("Engineer ID: ", self.id)
        print("Engineer Project: ", self.project)
        print("Engineer Domain: ", self.domain)
        print("Engineer Department: ", self.department)


class Salesperson(Employee):
    def __init__(self, name, id, product):
        self.name = name
        self.salary = 3000
        self.id = id
        self.product = product
        self.sales = 0

    def change_product(self, new_product):
        self.product = new_product

    def sale(self):
        self.sales += 1

    def print_info(self):
        print("Salesperson Name: ", self.name)
        print("Salesperson Salary: ", self.salary)
        print("Salesperson ID: ", self.id)
        print("Salesperson Product: ", self.product)
        print("Salesperson Sales: ", self.sales)


manager = Manager("John", 1, "IT")
employee1 = Employee("Jack", 1000, 2)
employee2 = Employee("Ana", 1000, 3)
manager.add_employee()
manager.add_employee()
manager.print_info()
manager.remove_employee()
manager.print_info()

engineer = Engineer("Don", 10, "IT", "Software", "Project 1", manager)
engineer.change_department("HR")
engineer.print_info()

salesperson = Salesperson("Lilo", 23, "Cars")
salesperson.sale()
salesperson.sale()
salesperson.print_info()
