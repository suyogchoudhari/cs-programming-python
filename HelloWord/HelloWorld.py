print("Hello Python!!")


class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.fname,self.lname)


ep1 = Employee('suyog', 'choudhari', 50000)

ep2 = Employee('suyog2', 'choudhari2', 60000)

print(ep1.fname)
print(ep2.fullName())
