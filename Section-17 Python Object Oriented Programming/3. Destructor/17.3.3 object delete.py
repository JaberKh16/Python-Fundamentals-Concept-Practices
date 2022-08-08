class Calculator:
    name = "Calcu"
    model = "FX 990T"
    battery = 5

    def calculation(self):
        print("I can do calculation")



try:

    c1 = Calculator()
    del c1
    print('Object is being deleted!')
    print(hasattr("Calculator", "c1"))



except:
    print("Specified attribute gets deleted")



