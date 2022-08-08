class Bird :

    def __int__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class Penguin(Bird) :
    
    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
# check object-peggy, class info
print(peggy)

# accessing peggy class instance methods though had specified
# working mechanism is here, is like if peggy class doesn't have the
# instance method whoisThis() then , peggy object will search the same method
# from its parent class.
peggy.whoisThis() # accessing own class method
peggy.swim() # accessing parent class method
peggy.run() # accessing own class method


bird = Bird()
# check object-bird, class info
print(bird)
# accessing Bird class methods
bird.whoisThis()
bird.swim()