# Object Oriented Programming Intro
# Prompt:
# Employee -> Name, Email, Salary
# |_ Developer -> Language
# |_ Manager -> Salary, Team (Developers)

class Employee:
    # Class Variable
    pay_raise_rate = 1.05
    num_emp = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.email = fname.lower() + "_" + lname.lower() + "@gmail.com"
        self.salary = salary

        # Use overall class variable to keep track of count
        Employee.num_emp += 1

    def display_name(self):
        return "{} {}".format(self.fname, self.lname)

    def apply_raise(self):
        self.salary = int(self.salary * Employee.pay_raise_rate)

    @classmethod
    def set_raise_amt(cls, amount):
        # Class method to change the class variable for all instances
        # Instead of Employee.pay_raise_rate = amount
        cls.pay_raise_rate = amount

    @classmethod
    def from_string(cls, stream_data):
        # Using classmethod as alternative constructor - Amazing!
        fname, lname, salary = stream_data.split("|")
        return cls(fname, lname, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # Magic/Dunder Methods
    def __repr__(self):
        # For a developer to understand the usage
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.salary)

    def __str__(self):
        return "{}, {}".format(self.display_name(), self.email)


class Developer(Employee):
    pay_raise_rate = 1.07

    def __init__(self, fname, lname, salary, lang):
        super().__init__(fname, lname, salary)
        self.lang = lang


class Manager(Employee):

    def __init__(self, fname, lname, salary, team=None):
        # A manager can have no team assigned initially.
        super().__init__(fname, lname, salary)
        if team is None:
            self.team = []
        else:
            self.team = team

    def add_to_team(self, employee):
        if employee not in self.team:
            self.team.append(employee)

    def remove_from_team(self, employee):
        if employee in self.team:
            self.team.remove(employee)

    def print_team(self):
        for employee in self.team:
            print(employee.display_name())


emp1 = Employee("Tea", "Drinker", 112000)
emp2 = Developer("Coffee", "Drinker", 69000, "Python")
mgr1 = Manager("Bar", "Tender", 32000, [emp2])

print(repr(emp1))
print(str(emp1))



######### NOTES #########  NOTES ######### NOTES #########
# Add Attribute - Not the best way
# emp1.explicit_attribute = "explicit_attribute"

# Test Basic Functions
# print(emp1.email, emp1.salary)
# print(emp2.email, emp2.salary)

# Two ways of calling function - Use the first
# print(emp2.display_name())
# print(Employee.display_name(emp1))

# # Apply Salary Raise
# print(emp1.salary)
# emp1.apply_raise()
# print(emp1.salary)
#
# # Change class variable for only one instance
# emp1.pay_raise_rate = 1.1
# print(Employee.pay_raise_rate)
# print(emp1.pay_raise_rate)
# print(emp2.pay_raise_rate)

# Dynamic Class Variable
# print(Employee.num_emp)

# Class Method
# print(emp1.pay_raise_rate)
# Employee.set_raise_amt(1.06)
# print(emp2.pay_raise_rate)

# Class Method - Alternative Constructor
# emp3_data = "Coffee|Grinder|52000"
# emp3 = Employee.from_string(emp3_data)
# print(emp3.email, emp3.salary)

# # Static Method
# import datetime
# test_day = datetime.date(2020, 12, 17)
# print(Employee.is_workday(test_day))

# Method resolution order
# help(Developer)

# Check class variable for different classes inherited
# print(emp1.pay_raise_rate)
# print(emp2.pay_raise_rate)

# Use subclass specific functions
# mgr1.add_to_team(emp2)
# mgr1.print_team()
# print(mgr1.email)
#
# mgr2 = Manager("Barr", "Ista", 18000, [emp1])
# mgr2.add_to_team(emp2)
# mgr2.print_team()

# Check isinstance and issubclass
# print(isinstance(mgr1, Manager))
# print(isinstance(mgr1, Developer))
# print(issubclass(Developer, Employee))
