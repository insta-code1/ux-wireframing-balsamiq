from employeedetails import Employee_spec


class salesrep(Employee_spec):
    def __init__(self, fname, lname, service, location):
        self.location = location
        super(salesrep, self).__init__(fname, lname, service)

    def salcalc(self):
        standardSal = self.calculated_salary()
        if self.location == 'Ireland':
            return standardSal * 1.05
        else:
            return standardSal