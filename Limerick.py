import pronouncing 
import Globals
import string
import random
from Line_Generator import POSifiedText


class Limerick:
    def __init__(self, subject=None):
        self.lines = []
        self.subject = subject
        self.meters = {'A': [0, 1, 0, 0, 1, 0, 0, 1], 'B': [0, 1, 0, 0, 1]}
        self.lines = {'line_1': None, 'line_2': None, 'line_3': None, 
                        'line_4': None, 'line_5': None}
        self.a_meter = [1, 2, 5]
        self.b_meter = [3, 4]
        self.a_rhymes = []
        self.b_rhymes = []
        self.model = Globals.MODEL
        #self.nlp_model = nlp(self.model)
    
    def gen_new_line(self):
        return self.model.make_short_sentence(40)


    def gen_poem(self):
        for i in range(1, len(self.lines) + 1):
            line = 'line_' + str(i)
            trial = self.gen_new_line()
            self.lines[line] = self.rhyme_scheme(trial, i)
    

    def rhyme_scheme(self, line, line_number):
        line_stripped = line.translate(str.maketrans('', '', string.punctuation))
        words = line_stripped.split()
        last_word = words[len(words) - 1]
       
        if line_number in self.a_meter:
            if line_number == 1:
                self.a_rhymes.append(last_word)
                for word in pronouncing.rhymes(last_word):
                    self.a_rhymes.append(word)
                return line
            if last_word not in self.a_rhymes:
                words[len(words) - 1] = random.choice(self.a_rhymes)
                return ' '.join(words)
            else:
                return line

        elif line_number in self.b_meter:
            if line_number == 3:
                self.b_rhymes.append(last_word)
                for word in pronouncing.rhymes(last_word):
                    self.b_rhymes.append(word)
                return line
            if last_word not in self.b_rhymes:
                words[len(words) - 1] = random.choice(self.b_rhymes)
                return ' '.join(words)
            else:
                return line


    def check_meter(self, line, line_meter):
        """
            DocString
        """
        meter = self.meters[line_meter]

        if line == None:
            return False
        else:
            print(line)
            print(meter)
            counter = 0
            line_stripped = line.translate(str.maketrans('', '', string.punctuation))
            line_stresses = []
            words = line_stripped.split()
            for word in words:
                if len(pronouncing.phones_for_word(word)) > 0:
                    pronun = pronouncing.phones_for_word(word)[0]
                    pronouncing.syllable_count(pronun)
                    num_syllables = pronouncing.syllable_count(pronun)
                    stresses = pronouncing.stresses(pronun)
                    for i in range(num_syllables):
                        line_stresses.append(int(stresses[i]))
                        #if stresses[i] != meter[counter + i]:
                            #return False
                    counter += num_syllables
            print(line_stresses)
                
            return True
        

    def __str__(self):
        """
           
            :return (String) the object's string representation
        """
        poem = self.lines.values()
        return '\n'.join(str(line) for line in poem)

    def __repr__(self):
        """
            Returns the String representation of the Baker object

            :return (String) the object's string representation
        """
        return f'Limerick with {self.subject} as the subject'

def main():
    Globals.init()
    poem = Limerick()
    poem.gen_poem()
    print(poem)
    

if __name__ == "__main__":
    main()
    '''    
    def gen_next_line(self, line_meter, line_number=None):
        """
            DocString
        """
        line = ''
        total_syllables = 0

        #Special Case
        if line_number == 1:
            line.append("There once was ")
            if self.subject[0] in self.vowels:
                line.append("an " + self.subject + " ")
            else:
                line.append("a " + self.subject + " ")
            total_syllables += 5
        
        while total_syllables != len(self.meters[line_meter]):
            trial = line.copy()
            next_word = Word()
            
            if len(line) == 0:
                next_word.gen_first_word()
            else:
                next_word.gen_next_word(line[len(line) - 1])

            trial.append(next_word)

            if (self.check_meter(trial, line_meter)):
                line.append(next_word)
                total_syllables += next_word.syllables
        
        rhymes = pronouncing.rhymes(line[len(line) - 1])
        if line_meter == 'A':
            self.a_rhymes.append(rhymes)
        elif line_meter == 'B':
            self.b_rhymes.append(rhymes)

        return line
    '''

    




