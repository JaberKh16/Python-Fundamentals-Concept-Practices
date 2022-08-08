"""
    Class Static Method Concept
    ===========================
    To declare a static method inside a class need to specify the
    @staticmethod descriptor before the name of the method.
    
    To access static method no need to create a class instance instead
    can be accessed using the class name. But if wanted then can create
    a class instance and then can be accessed with the class instance 
    name.
    
    It is important to mention that static methods can only access 
    class attributes in Python.
    
"""

# defining the class
class Band_Account:
    # class attributes
    account_count = 0
    account_type = 'Saving'
    bank_name = "Chartered Association"
    
    # class constructor
    def __init__(self, name, id_no, email) -> None:
        self.Name = name
        self.ID_No = id_no
        self.Email = email
        Band_Account.account_count +=1
    
    # class method
    def getting_customer_details(self):
        print(f'Account Holder Name :{self.Name}')
        print(f'Account Holder ID : {self.ID_No}')
        print(f'Account Holder Email : {self.Email}')   
    
    # class static method
    @staticmethod
    def getting_bank_information():
        # static methods can be only access the class attributes
        print(f'Bank Name: {Band_Account.bank_name}')
        print(f'Account Type: {Band_Account.account_type}')
        

# creating class instance    
holder_1  = Band_Account('HK', '34242112', 'hk@gmail.com')
# holder_2  = Band_Account('RK', '22424531', 'rk@yahoo.com')

# calling the static method
# holder_1.getting_customer_details() # can be accessed via class instance name also
Band_Account.getting_bank_information()
    

# calling the instance method
holder_1.getting_customer_details()
# holder_2.getting_customer_details()    

# getting the value of class attribute
print("Accounts created: ", Band_Account.account_count)
