"""
    Class Instance Methods Example
"""

# defining the class
class Band_Account:
    # class attributes
    account_count = 0
    
    # class constructor
    def __init__(self, name, id_no, email) -> None:
        self.Name = name
        self.ID_No = id_no
        self.Email = email
        Band_Account.account_count +=1
        
    # class instance methods
    def get_customer_details(Name, ID_No,Email ):
        print(f'Account Holder Name :{Name}')
        print(f'Account Holder ID : {ID_No}')
        print(f'Account Holder Email : {Email}')   
        

# creating class instance    
holder_1  = Band_Account('HK', '34242112', 'hk@gmail.com')
holder_2  = Band_Account('RK', '22424531', 'rk@yahoo.com')

# calling the instance method
holder_1.get_customer_details()
holder_2.get_customer_details()    

# getting the value of class attribute 
print(Band_Account.account_count)
