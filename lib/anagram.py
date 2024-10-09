# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        
    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, value):
        if value.isalpha():
            self._word = value.lower()
        else:
            raise ValueError("Word must contain only alphabetic characters.")
        
    def match(self, words):
        return [word for word in words if sorted(self.word) == sorted(word.lower())]
        

    

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))