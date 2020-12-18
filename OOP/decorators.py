class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    @property
    def email(self):
        # Adding property will let you use it as __init__
        # and will change if there's a change in fname or lname
        return "{}_{}@gmail.com".format(self.fname.lower(), self.lname.lower())

    @property
    def display_name(self):
        # Takes fname and lname and sets it as self.display_name
        return "{} {}".format(self.fname, self.lname)

    @display_name.setter
    def display_name(self, name):
        # I have to use a setter to change a @property,
        # because they're bound to fname and lname.
        # I can't directly change display_name
        fname, lname = name.split(" ")
        self.fname = fname
        self.lname = lname

    @display_name.deleter
    def display_name(self):
        # del emp.display_name
        print("Name deleted")
        self.fname = None
        self.lname = None


# Create Employee instance
emp1 = Employee("Earl", "Gray", 135000)
print(emp1.display_name)
print(emp1.email)

# Works, because of @display_name.setter
emp1.display_name = "Green Tea"
print(emp1.display_name)
print(emp1.email)

# Works because of @display_name.deleter
del emp1.display_name
print(emp1.display_name)

# Additionally, setaddr/getattr can be used
setattr(emp1, "display_name", "Sleep Deprivation")
print(emp1.display_name, emp1.email)

setattr(emp1, "fname", "Water")
print(emp1.display_name, emp1.email, emp1.salary)

# Directly get an attribute using getattr
attribute_name = "fname"
fname = getattr(emp1, attribute_name, emp1)
print(fname)

# To pass all information as a dictionary
# This is particularly useful to pass a raw info
employee_info = {"fname":"Caramel", "lname":"Macchiato", "salary": 25000}
for key, val in employee_info.items():
    setattr(emp1, key, val)
print(emp1.display_name, emp1.email, emp1.salary)
