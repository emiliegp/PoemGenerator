import pronouncing 
class Limerick:
    def __init__(self, subject):
        self.lines = []
        self.subject = subject
        self.meter = {'A': [0, 1, 0, 0, 1, 0, 0, 1], 'B': [0, 1, 0, 0, 1]}

        self.lines = {'line_1': None, 'line_2': None, 'line_3': None, 
                        'line_4': None, 'line_5': None}

        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.gen_first_line()
        self.a_rhymes = []
        self.b_rhymes = []
    
    def gen_first_line(self):
        line = ''
        line.append("There once was ")
        if self.subject[0] in self.vowels:
            line.append("an " + self.subject + " ")
        else:
            line.append("a " + self.subject + " ")
        
        total_syllables  = 5
        while total_syllables <= len(self.meter['A']):
            trial = line.copy()
            next_word, syllables = self.gen_next_word(line[len(line) - 1])
            trial.append(next_word)
            if (self.check_meter(trial, 'A')):
                line.append(next_word)
                total_syllables += syllables
        
        if self.check_meter(line):
            self.a_rhymes = pronouncing.rhymes(line[len(line) - 1])
            self.lines['line_1'] = line
        
    def gen_next_word(self, word):
        "do something"

    def gen_next_line(self, line_meter):
        "do something"
    
    def check_meter(self, line, line_meter):
        "do something"

