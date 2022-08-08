"""
 # Function Overloading:
   
     # Basically, function overloading is creating different version of the function
      with same function name but with different no. of parameter inside a same class.
     
     # Python doesn't support function overloading , thouugh will get TypeError, if
       the passed argument doesn't matched by latest function parameters.
     

"""

class Account:
    def Create_Accout(self, name, email, password, mobile_no):
        self.name = name
        self.email = email
        self.password = password 
        self.mobile_no = mobile_no
    
    def Create_Account(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def get_account_info(self):
        print(f'Account Holder Name: {self.name}')
        print(f'Account Holder Email: {self.email}')
        print(f'Account Holder Password: {self.password}')
        print(f'Account Holder Mobile No: {self.mobile_no}')

account = Account()
account.Create_Accout('JK', 'jk@gmail.com', 'abc123','0154656548')
account.get_account_info()   

account_1 = Account()
account_1.Create_Accout('JK', 'jk@gmail.com', 'abc123')
account.get_account_info()       