"""
 
 Polymorphism:
  
  # Ability of code to take different forms depending on the type with which 
    it is used.
 
 Advantage of Polymorphism:
   
   # Can write generic code that works with objects of different classes.
     When writting generic code programmer doesn't need to think about the
     specific classes that will use the code.
   # Makes the code concise and flexible and provides a sort of abstraction.
   # The code becomes very easy to update also, and can easily add new types,
     means the function that are already written can work with new types that, 
     will be define in future as long as the new types is support the required
     operations. 
   # The behaviour shown by overloaded operator is Polymorphism.
    


"""

class AudioFile:
    def __init__(self, file_name) -> None:
        if not file_name.endswith(self.ext):
            raise Exception('Invalid file format')
        
        self.file_name = file_name

class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print('Playing {} as mp3'.format(self.file_name))

class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print('Playing {} as wav'.format(self.file_name))

class OggFile(AudioFile):
    ext = 'ogg'
    def play(self):
        print('Playing {} as ogg'.format(self.file_name))
        

# creating instance of classes
ogg_file = OggFile('my_file.ogg')
ogg_file.play()

# wav_file = OggFile('my_file.wav')
# wav_file.play()

# mp3_file = OggFile('my_file.mp3')
# mp3_file.play()