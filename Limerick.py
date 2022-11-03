import pronouncingpy as pronouncing 
class Limerick:
    def __init__(self, subject):
        self.lines = []
        self.subject = subject
        self.meters = {'A': [0, 1, 0, 0, 1, 0, 0, 1], 'B': [0, 1, 0, 0, 1]}

        self.lines = {'line_1': None, 'line_2': None, 'line_3': None, 
                        'line_4': None, 'line_5': None}

        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.gen_first_line()
        self.a_rhymes = set()
        self.b_rhymes = set()

        
    def gen_next_word(self, word=None):
        """
            DocString
        """

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
            if len(line) < 1:
                next_word, syllables = self.gen_next_word()
            else:
                next_word, syllables = self.gen_next_word(line[len(line) - 1])

            trial.append(next_word)

            if (self.check_meter(trial, line_meter)):
                line.append(next_word)
                total_syllables += syllables
        
        rhymes = pronouncing.rhymes(line[len(line) - 1])
        if line_meter == 'A':
            self.a_rhymes.append(rhymes)
        elif line_meter == 'B':
            self.b_rhymes.append(rhymes)

        return line


    def check_meter(self, line, line_meter):
        """
            DocString
        """
        meter = self.meters[line_meter]
        counter = 0
        for word in line:
            pronun_list = pronouncing.phones_for_word(word)
            num_syllables = pronouncing.syllable_count(pronun_list[0])
            stresses = pronouncing.stresses(pronun_list[0])
            for i in range(num_syllables):
                if stresses[i] != meter[counter + i]:
                    return False
            counter += num_syllables
        return True




