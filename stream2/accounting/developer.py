from employeedetails import Employee_spec


class Developer(Employee_spec):
    def __init__(self, fname, lname, yworked, prog_language):
        self.prog_language = prog_language
        super(Developer, self).__init__(fname, lname, yworked)

    def details(self):
        return super(Developer, self).details() + 'Programming Language: %s' % self.prog_language

    def calculated_salary(self):
        standard = super(Developer, self).calculated_salary()
        if self.prog_language.lower() == 'python':
            bonus = standard * .05
        else:
            bonus = standard * .01

        return standard + bonus
