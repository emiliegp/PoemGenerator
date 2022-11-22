# PoemGenerator
## Bowdoin CSCI 3725 M6:  A poetry generation system

## Description 
Afetr much reserach and trial and error, the final poem generator system uses the markovify, pronouncing, and nltk python libraries to produce Limerick-like poems. I say Limerick-like, because afetr much hassle, I could not succeed in changing the structure of the lines produced to fit within the anapestic rythm. Other than this, all the other rules of the LImerick are followed:
    - The poems produced are five lines long and organized in one stanza
    - The first, second, and fifth line end in rhyming words
    - The thrid and fourth lines rhyme 
Ultimately, this systems hopes ot be an intercative experience with the user to produce the best poem possible. It works by by first generating a Markovify Model which pulls from Project Gutenburg's corpus of published Limericks. markovify is a very popular pyhton library that can helpful when trying to generate text that is similar to a large corpus. What first drew me to this python library was the promise that "markovify.Text tries to generate sentences that do not simply regurgitate chunks of the original text" (markovify README). This relates to the idea of 'mere generation' that we have discussed in length. This system changed the max_overlap_value to be 5 since the lines of each poem were fairly short. In addition to the markovify library, I also used pronouncing and nltk to fix the sementaics of the random lines produced and follow the rules of a Limerick. 