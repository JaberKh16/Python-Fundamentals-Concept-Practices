
class Band_Account:
    # class attributes
    Name = None
    ID_No = None
    Email = None      

# creating class instance    
holder_1  = Band_Account()
holder_2  = Band_Account()

# setting instance attributes for the class
# 'HK', '34242112', 'hk@gmail.com'
setattr(holder_1, 'Name', 'HK')
setattr(holder_1, 'ID_NO', '34242112')
setattr(holder_1, 'Email', 'hk@gmail.com')

# RK', '22424531', 'rk@yahoo.com'
setattr(holder_2, 'Name', 'RK')
setattr(holder_2, 'ID_NO', '22424531')
setattr(holder_2, 'Email', 'rk@yahoo.com')

# getting the instance attribute using getattr(obj_name, attr_name)
# getattr(obj_name, attr_name) is like - obj_name.attr_name
print(getattr(holder_1, 'Name'))
print(getattr(holder_1, 'ID_No'))
print(getattr(holder_1, 'Email'))

print(getattr(holder_2, 'Name'))
print(getattr(holder_2, 'ID_No'))
print(getattr(holder_2, 'Email'))


