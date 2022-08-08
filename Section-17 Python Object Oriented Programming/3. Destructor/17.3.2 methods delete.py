class Calculator:
    name = "Calcu"
    model = "FX 990T"
    battery = 5

    def calculation(self):
        print("I can do calculation")


c1 = Calculator()

try:

    del c1.calculation



except:
    print("Specified method gets deleted")
    print(hasattr("Calculator", "calculation"))



