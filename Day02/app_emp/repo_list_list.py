'''
Employee Management Repo
db = inmemory list of employees, each employee is a list
    employee attr: [name, age]

create_employee(emp_obj) -> add emp
read_all() -> returns the employees 
read_by_name(name) -> returns the emp for given name
update_by_name(name, new_age) -> update employee's new_age for given name 
delete_by_name(name) -> delete employee for given name 
'''

employees = []

def create_emp(emp):
    employees.append(emp)

def read_all():
    return employees

def read_by_name(name):
    for emp in employees:
        if emp[0] == name:
            return emp
        #
    #
    return None

def update_by_name(name, new_age):
    for emp in employees:
        if emp[0] == name:
            emp[1] = new_age
        #
    #

def delete_by_name(name):
    for index, emp in enumerate(employees):
        if emp[0] == name:
            employees.pop(index)
            return
        #
    #

if __name__ == "__main__":
    # test all crud ops 
    create_emp(['Mahesh', 47])
    print(read_all())
    create_emp(['Aparna', 27])
    print(read_all())
    print(read_by_name('Aparna'))
    create_emp(['Aniruth', 23])
    print(read_all())
    update_by_name('Aniruth', 30)
    print(read_all())
    delete_by_name('Mahesh')
    print(read_all())