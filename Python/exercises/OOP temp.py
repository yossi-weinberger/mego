class Try1:
    pass

    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = last_name + "." + first_name + "@company.com"

    def full_name(self):
        return self.first_name + " " + self.last_name


emp1 = Try1("yossi","weinberger","0527123417","")

print (emp1.full_name())

