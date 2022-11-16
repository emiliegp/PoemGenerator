import spacy
import markovify

nlp = spacy.load('en_core_web_sm')
    
class POSifiedText(markovify.NewlineText):
    
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence