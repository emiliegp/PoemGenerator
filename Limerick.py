import pronouncing 
import Globals
import string
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os


class Limerick:
    def __init__(self, subject=None):
        self.lines = {'line_1': None, 'line_2': None, 'line_3': None, 
                        'line_4': None, 'line_5': None}
        self.stopwords = set(stopwords.words('english'))
        self.stopwords.remove('the')
        self.stopwords.remove('there')
        self.a_rhymes = []
        self.b_rhymes = []
        self.model = Globals.MODEL
        self.lemmatizer = WordNetLemmatizer()
        self.subject = ['NN', 'NNS', 'NNP', 'NNPS']
        self.pronoun = ['PRP', 'PRP$']
        #self.nlp_model = nlp(self.model)
    
    def gen_new_line(self, line_number):
        gen_new = True
        while gen_new:
            line = self.model.make_short_sentence(40)
            line_stripped = line.translate(str.maketrans('', '', string.punctuation))
            words = word_tokenize(line_stripped)
            if line_number == 1:
                if words[0] not in self.stopwords:
                    gen_new = False
            else:
                gen_new = False
        return line


    def gen_poem(self):
        for i in range(1, len(self.lines) + 1):
            line = 'line_' + str(i)
            trial = self.gen_new_line(i)
            self.lines[line] = self.rhyme_scheme(trial, i)
    

    def say_poem(self):
        for line in self.lines.values():
            os.system("say " + line)

    def rhyme_scheme(self, line, line_number):
        line_stripped = line.translate(str.maketrans('', '', string.punctuation))
        words = word_tokenize(line_stripped)
        last_word = words[len(words) - 1]
       
        if line_number in self.a_meter:
            if line_number == 1:
                self.a_rhymes.append(last_word.casefold())
                for word in pronouncing.rhymes(last_word):
                    self.a_rhymes.append(word)
                return line
            if last_word not in self.a_rhymes:
                new_line = self.apply_semantics(words, line_number)
                return new_line
            else:
                return line

        elif line_number in self.b_meter:
            if line_number == 3:
                self.b_rhymes.append(last_word)
                for word in pronouncing.rhymes(last_word):
                    self.b_rhymes.append(word)
                return line
            if last_word not in self.b_rhymes:
                new_line = self.apply_semantics(words, line_number)
                return new_line
            else:
                return line


    def apply_semantics(self, words, line_number):
        part_of_speech = nltk.pos_tag(words)
        last_word = words[len(words) - 1]
    
        if line_number in self.a_meter:
            to_match = part_of_speech[len(part_of_speech) - 1][1]
            rhyme_scheme = nltk.pos_tag(self.a_rhymes)
            new_word, pos = random.choice(rhyme_scheme)
            if len(self.a_rhymes) > 1:
                while (pos != to_match) and new_word == last_word:
                    new_word = random.choice(self.a_rhymes)
            
            words[len(words) - 1] = random.choice(self.a_rhymes)
            new_line = ' '.join(words)
            return new_line
        
        elif line_number in self.b_meter:
            to_match = part_of_speech[len(part_of_speech) - 1][1]
            rhyme_scheme = nltk.pos_tag(self.b_rhymes)
            new_word, pos = random.choice(rhyme_scheme)
            if len(self.a_rhymes) > 1:
                while (pos != to_match) and new_word == last_word:
                    new_word = random.choice(self.b_rhymes)
            
            words[len(words) - 1] = random.choice(self.b_rhymes)
            new_line = ' '.join(words)
            return new_line

    def fix_pronouns(self):
        nouns = []
        counter = 1
        for line in self.lines.values():
            new_words = []
            line_stripped = line.translate(str.maketrans('', '', string.punctuation))
            words = word_tokenize(line_stripped)
            part_of_speech = nltk.pos_tag(words)
            for word, pos in part_of_speech:
                if pos in self.subject:
                    nouns.append(word)
                    new_words.append(word)
                elif pos in self.pronoun:
                    pronoun = word
                    user_help = input('What does \'' + pronoun + '\' need to be ' +\
                        'according to the list of nouns in the poem: ' + ', '.join(nouns)\
                            +'\n')
                    new_words.append(user_help)
                else:
                    new_words.append(word)
            new_line = ' '.join(new_words)
            line = 'line_' + str(counter)
            self.lines[line] = new_line
            counter += 1
        

    def __str__(self):
        """
           
            :return (String) the object's string representation
        """
        poem = self.lines.values()
        print("\nThe Poem Produced: \n")
        return '\n'.join(str(line) for line in poem)

    def __repr__(self):
        """
            Returns the String representation of the Baker object

            :return (String) the object's string representation
        """
        return f'Limerick with {self.subject} as the subject'