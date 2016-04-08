class Employee_spec(object):
    BASE_SALARY = 5000
    employee_number = 0

    def __init__(self, fname, lname, yworked):
        self.first_name = fname
        self.last_name = lname
        self.years_worked = yworked
        Employee_spec.employee_number += 1
        self.employee_number = Employee_spec.employee_number

    def calculated_salary(self):
        if self.years_worked < 3:
            return self.BASE_SALARY * 1.1
        elif self.years_worked <= 5:
            return self.BASE_SALARY * 1.2
        else:
            return self.BASE_SALARY * 1.25

    def details(self):
        return "First Name: %s\n Surname: %s\n Yeard Worked: %s\n Employee Number: %s\n Salary: %s\n " % (
            self.first_name, self.last_name, self.years_worked, self.employee_number, calculated_salary())