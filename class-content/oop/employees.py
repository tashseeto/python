class Employee:

    def __init__(self, name, salary, phone_number, start_date, not_for_rehire):
        self.name = name
        self.salary = salary
        self.phone_number = phone_number
        self.start_date = start_date
        self.not_for_rehire = not_for_rehire

    def get_employment_details(self):
        return (self.name, self.salary, self.start_date, self.not_for_rehire)

    def get_contact_details(self):
        return (self.name, self.phone_number)

    def __str__(self):
        return self.name


fran = Employee("Fran Person", 78000, "0924791712", "1st June 2020", False)
print(fran)
print(fran.name)

roary = Employee("Roary", 1200000, "0924791712", "1st June 2020", True)
print(roary.not_for_rehire)
print(roary)
print(roary.get_employment_details())