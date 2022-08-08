'''
 Encapsulation or Hiding:
   
   # Hiding the implementation details from the end user is called the Encapsulaiton.
   # In Python any attributes can be hide or make it private using double underscore
    (__) before their name or single(_) before their name to make it protected.
   # this hiding means you can't access the data from outside the class

   # Basically nothing in Python , is actually private method/attributes
     we can access them via --->

          created_object._object_class_name__private_attribute_name
          class_name._object_class_name__private_attribute_name

        e.g -->     a._Car__model

'''

class JustCount :
      # private class attribute
      __secretCount = 0
      # public class instance method
      def count(self):
          self.__secretCount+=1
          print(self.__secretCount)


try:
  
  counter = JustCount()
  counter.count()
  counter.count()
  counter.count()
  # cant directly access the __secretCount because it private 
  # typically, can't be accessible outside the class
  print(counter.__secretCount)
except AttributeError as e:
  print(e)

finally:
  # accessing the private attributes in special way
  # first check the directory for the defined class
  print(dir(JustCount))
  
  # getting access to the private attribute
  # accessing via object name will returns the last updated value for the private attributes
  print(f'Accessing via object name: {counter._JustCount__secretCount}')
  # accessing via class name will returns the beginning set value for the private attributes
  print(f'Accessing via class name : {JustCount._JustCount__secretCount}')
  
