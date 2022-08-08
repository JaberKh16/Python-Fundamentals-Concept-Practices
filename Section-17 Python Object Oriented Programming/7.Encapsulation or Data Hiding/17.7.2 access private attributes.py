class Adding_class :

    __hiddenvar = 0
    __staff = "Faculty"

    def add(self, increment):
        self.__hiddenvar+=increment
        print(self.__hiddenvar)


my_object = Adding_class()
my_object.add(2)
my_object.add(5)
print(my_object._Adding_class__staff)
print(my_object._Adding_class__hiddenvar)










