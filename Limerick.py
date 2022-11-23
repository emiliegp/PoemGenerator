"""
Emilie Grand'Pierre 
Computational Creativity (CSCI 3725)
M6: Poetry Slam
9/15/2022

In this file, I define the Limerick class, which includes methods to 
generate a poem that seeks to follow the rhyming rules of Limerick and the 
semantics rules of english grammer with the help fo the user. As such, this
class enables a co-collaberative processs between computer and user to produce
the best possible poem. Within the methods the pronouncing, markovify, and 
nltk python libraries are used. 
"""

import pronouncing 
import Globals
import string
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

class Limerick:
    #Limerick object
    def __init__(self):
        '''
            A represnetaion of a LImerick object, equiped with fields that 
            represnet the rules,markovify modelf of the inspiring corpus, 
            and a modifed list of nltk stopwords. 
        '''
        #lines of the gernated poem
        self.lines = {'line_1': None, 'line_2': None, 'line_3': None, 
                        'line_4': None, 'line_5': None}
        
        #modifed nltk stopwords 
        self.stopwords = set(stopwords.words('english'))
        self.stopwords.remove('the')
        self.stopwords.remove('there')

        #encoding the rhyme scheme of a Limerick poem
        self.a_meter = [1,2,5]
        self.b_meter = [3,4]
        self.a_rhymes = []
        self.b_rhymes = []

        #inspiring corpus 
        self.model = Globals.MODEL

        #ncodes semantic understanding 
        self.subject = ['NN', 'NNS', 'NNP', 'NNPS']
        self.pronoun = ['PRP', 'PRP$']
        
    
    def gen_new_line(self, line_number):
        '''
            Generates a new line of less than 40 characters using the markovify 
            model of the Project Gutenburg corpus. The line genrated will have 
            less than five words in common with the corpus

            :return (str) generate poem line
        '''
        gen_new = True
        while gen_new:
            line = self.model.make_short_sentence(40, max_overlap_total=5)
            line_stripped = line.translate(str.maketrans('', '', string.punctuation))
            words = word_tokenize(line_stripped)
            #if generating the first line of the poem, ensures that it does not 
            #begin with a stopword (see nltk stopwords for complete list)
            if line_number == 1:
                if words[0] not in self.stopwords:
                    gen_new = False
            else:
                gen_new = False
        return line


    def gen_poem(self):
        '''
            Simulates a poet that generates a poem line by line using the 
            gen_new_line() funciton and ensures that each line produced follows 
            the rhyme scheme of a Limerick using the rhyme_scheme() fucniton. 
            a patchwork quilt. 
            
            Populates self.lines
        '''
        for i in range(1, len(self.lines) + 1):
            line = 'line_' + str(i)
            trial = self.gen_new_line(i)
            self.lines[line] = self.rhyme_scheme(trial, i)
    

    def say_poem(self):
        '''
            Using the os library for text to speech, speaks the generated poem]
            line by line
        '''
        for line in self.lines.values():
            os.system("say " + line)

    def rhyme_scheme(self, line, line_number):
        '''
           Employs nltk tokenization to split the line parameter into a list of 
           words. Then using the fields of a Limerick object, a_meter and 
           b_meter to ensure that the line follows the rhyming rules of a Limerick

            :param line: (str) line from a poem
            :param line_number: (int) the line number of a given line
                                    (i.e. 1st, 2nd, 3rd, 4th, 5th)
        '''
        line_stripped = line.translate(str.maketrans('', '', string.punctuation))
        words = word_tokenize(line_stripped)
        last_word = words[len(words) - 1]
       
        #if the 1st, 2nd, or 5th line
        if line_number in self.a_meter:
            #determines the 'a' rhyme scheme of the poem
            if line_number == 1:
                self.a_rhymes.append(last_word.casefold())
                for word in pronouncing.rhymes(last_word):
                    self.a_rhymes.append(word)
                return line
            #if the automatically generated word does not fit the rhyme scheme:
            if last_word not in self.a_rhymes:
                #see apply_semantics doc
                new_line = self.apply_semantics(words, line_number)
                return new_line
            else:
                return line

        #if the 3rd or 4th line
        elif line_number in self.b_meter:
            #determines the 'b' rhyme scheme of the poem
            if line_number == 3:
                self.b_rhymes.append(last_word)
                for word in pronouncing.rhymes(last_word):
                    self.b_rhymes.append(word)
                return line
            #if the automatically generated word does not fit the rhyme scheme:
            if last_word not in self.b_rhymes:
                #see apply_semantics doc
                new_line = self.apply_semantics(words, line_number)
                return new_line
            else:
                return line


    def apply_semantics(self, words, line_number):
        '''
            A helper method to the rhyme_scheme() fucntion which ensures that
            the word switched out to fit the rhyme scheme works semtaically. 
            Using nltk's pos_tag() function, this function ensures that the 
            swapped word is the same part of speech as the word it is replacing

            :param words: (list) str words in a line
            :param line_number: (int) indication of which rhyme scheme to enforce 

            :return (str) line of poetry the fits the rhyme scheme of the poem 
        '''
        part_of_speech = nltk.pos_tag(words)
        last_word = words[len(words) - 1]
    
        #following the 'a' rhyme scheme of the poem
        if line_number in self.a_meter:
            #the part of speech of the word that is being replaced 
            to_match = part_of_speech[len(part_of_speech) - 1][1]
            #gathering the part of speech of every word that rhymes in the scheme
            rhyme_scheme = nltk.pos_tag(self.a_rhymes)
            new_word, pos = random.choice(rhyme_scheme)
            #ensuring there are mutliplle words that fit the rhyme scheme 
            if len(self.a_rhymes) > 1:
                #until new_word is the correct part of speech and is not the last word
                while (pos != to_match) and new_word == last_word:
                    new_word = random.choice(self.a_rhymes)
            
            words[len(words) - 1] = random.choice(self.a_rhymes)

            #return a string
            new_line = ' '.join(words)
            return new_line
        
        #following the 'b' rhyme scheme of the poem (same logic)
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
        '''
            With user input, ensures that all the pronouns with the generated
            poem match with each other to increse the cohesion between the lines.
            Works by tracking the porper nouns and nouns in the poem, and cross-
            checking every pornoun to folow grammatical rules. Employing the idea
            that poems garner some of their meaning from the person who is 
            reaidng it, this funciton enables co-collaboration between user
            and system
        '''
        #a list that when populated includes all the nouns found in the poem
        nouns = []
        counter = 1
        for line in self.lines.values():
            #a list that when poluated with replace the old line of the poem
            new_words = []
            line_stripped = line.translate(str.maketrans('', '', string.punctuation))
            words = word_tokenize(line_stripped)
            part_of_speech = nltk.pos_tag(words)
            for word, pos in part_of_speech:
                #if the part of speech of the word is a noun/proper noun:
                if pos in self.subject:
                    nouns.append(word)
                    new_words.append(word)
                #id the part of speech fo the word is a pronouns:
                elif pos in self.pronoun:
                    pronoun = word
                    #input from the suer to ensure grammatical cohesion
                    user_help = input('What does \'' + pronoun + '\' need to be ' +\
                        'according to the list of nouns in the poem: ' + ', '.join(nouns)\
                            +'\n')
                    new_words.append(user_help)
                else:
                    new_words.append(word)
            new_line = ' '.join(new_words)

            #replace old line of the poem to the line with user input 
            line = 'line_' + str(counter)
            self.lines[line] = new_line
            counter += 1
        

    def __str__(self):
        """
            :return (String) the poems's string representation
        """
        poem = self.lines.values()
        print("\nThe Poem Produced: \n")
        return '\n'.join(str(line) for line in poem)

    def __repr__(self):
        """
            Returns the String representation of the Lierick object

            :return (String) the object's string representation
        """
        return f'Limerick generated with a markvoify model of the Porject Gutenburg corpus'
