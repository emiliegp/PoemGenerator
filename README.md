# PoemGenerator
## Bowdoin CSCI 3725 M6:  A poetry generation system

## Description 
After much research and trial and error, the final version of this poem generator uses the markovify, pronouncing, and nltk python libraries to produce Limerick-like poems. I say Limerick-like, because afetr much hassle, I could not succeed in changing the structure of the lines produced to fit within the anapestic rythm signature of Limericks. Other than this, all the other rules of the Limericks are followed:
    - The poems produced are five lines long and organized in one stanza
    - The first, second, and fifth line end in rhyming words
    - The thrid and fourth lines rhyme 

    Ultimately, this systems hopes to be an interactive experience with the user, who helps produce the best poem possible. It works by first generating a Markovify Model of Project Gutenburg's corpus of published Limericks. Markovify is a very popular pyhton library that can helpful when trying to generate text that is similar to a large corpus. What first drew me to this python library was the promise that "markovify.Text tries to generate sentences that do not simply regurgitate chunks of the original text" (markovify README). This relates to the idea of 'mere generation' that we have discussed in length. In this system, I lowered the max_overlap_value of the generated sentence from 15 to 5 since the lines of each poem are fairly short. I experimented with higher and lower values, but 5 struck the balance between producing gibberish and simply copying lines form the corpus. In addition to the markovify library, I also used pronouncing and nltk to fix the sementaics of the random lines produced and follow the rules of a Limerick. Like stated previosuly, though the system does fairly well when producing rhyming words with the help of pronouncing, since each line is generated in isolation to others, user input is helpful when bringing cohesion to the poem. 
