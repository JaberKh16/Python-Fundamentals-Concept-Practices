"""
    Class Based Iterator Example
    ============================ 
    Two things to be reminded when making a class an iterator object
    which are the following-
    
    1) need to define __iter__() method to make the class an iterator object.
    2) need to define __next__() method so that this class iterator can be accessed. 
"""

class Sentence :
    # class constructor
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split() # spliting the sentence 

    # making the class an iterator using the __iter__() method
    def __iter__(self):
        return self
    
    # __next__() method so that this class iterator values can be accessed upon 
    def __next__(self):
        if self.index >= len(self.words):
            raise  StopIteration
        index = self.index
        self.index +=1
        return  self.words[index]

my_sentence = Sentence("This is good test for iterators")

for word in my_sentence:
    print(word)

print("-----------------------------------------------------")

# making a generator for the same
# generator does have the __next__() method work for us automatically
def sentence (sentence):
    for word in sentence.split():
        yield word

my_sentence = sentence("this is good thing")
# show the object type
print(my_sentence)

for word in my_sentence:
    print(word)

