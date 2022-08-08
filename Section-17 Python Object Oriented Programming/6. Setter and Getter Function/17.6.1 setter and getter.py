class CSStudent :
    dept = "CSE"
    def __init__(self, roll):
        self.roll = roll

    # setter instance method or function
    def setAddress(self, address):
        self.address = address
    # getter  instance method fucntion
    def getAdddress(self):
        return self.address

# creating the class instance
Student = CSStudent(161188)
# accessing the class atrributes value 
print(Student.dept)
# setting the value for instance setAddress() method
Student.setAddress("Dhaka,  Mohammadpur")
# getting the value for instance getAdrress() method
print(Student.getAdddress())
