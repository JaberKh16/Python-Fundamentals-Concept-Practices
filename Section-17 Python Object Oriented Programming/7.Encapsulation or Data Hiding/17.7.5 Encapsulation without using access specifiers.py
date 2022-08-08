class BMI:
    def calculate_bmi(self):
        print('Enter your weight in kg:')
        self.weight = float(input())
        print('Enter your height in meters:')
        self.height = float(input())
        self.bmi = self.weight/(self.height) * (self.height)
        print('BMI is :', self.bmi)
        
        if self.bmi < 18.5:
            print('Underweight')
        elif self.bmi > 18.5 and self.bmi < 24.9:
            print('Healthy')
        elif self.bmi > 24.9 and self.bmi < 29.9:
            print('Overweight')
        else:
            print('Obese') 

bmi = BMI()
while True:
    print('1. Calocualte the bmi')
    print('2. Exit')
    choice = int(input('Enter the choice:'))
    
    if choice == 1:
        bmi.calculate_bmi()
    elif choice == 2:
        exit()
    