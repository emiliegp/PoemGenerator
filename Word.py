import pronouncingpy as pronouncing 
import markovify
import Globals

class Word:
    def __init__(self, word=None):
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.name = word
        self.pronuncitation = None
        self.syllables = None
        self.stresses = None

        if self.name != None:
            self.pronuncitation = pronouncing.phones_for_word(self.name)[0]
            self.syllables = pronouncing.syllable_count(self.pronuncitation)
            self.stresses = pronouncing.stresses(self.pronuncitation)
        
            


    def gen_first_word(self):
        """
            DocString
        """
        



    def gen_next_word(self, word):
        """
            DocString
        """
    
def main():
    new_word = Word()
    for line in new_word.corpus:
        print(line)

if __name__ == "__main__":
    main()