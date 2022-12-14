# PoemGenerator
## Bowdoin CSCI 3725 M6:  A poetry generation system

## Let’s Make A Poem Together: A Collaborative Poem Generation 

## Description 
When first presented with this project, I dreamt of creating an incredibly robust system that could create nuanced metaphors after taking in a subject from the user. This complex idea seemed reasonable to my naïve understanding of the state of NLP; this ignorance was in large part alleviated by Murati’s “Language & Coding Creativity,” which did a wonderful job of explaining the history of NLP, exploring the current state of research, and posing tough questions about what it means to create and evaluate art. With this new understanding in mind, I set out to tackle a more manageable task: in the 3rd grade, my Engish class did a short lesson on Limericks around St. Patrick’ s Day. Since then, I have always found these witty poems humorous and easy to understand when compared to poets like Shakespeare or Homer. Guided by some of the questions of writing and authorship, and after much research, trial, and error, the final version of this poem generator uses the markovify, pronouncing, and nltk python libraries to produce Limerick-like poems. I say Limerick-like, because after much hassle, I could not succeed in changing the structure of the lines produced to fit within the anapestic rhythm signature of Limericks. (A challenge that is approached incredibly differently in a computer as opposed to when humans ‘write’ a poem.) Other than this, all the other rules of the Limericks are followed:
-	The poems produced are five lines long and organized in one stanza
-	The first, second-, and fifth-line end in rhyming words
-	The third and fourth lines rhyme 

Ultimately, this system hopes to be an interactive experience with the user, who helps produce the best poem possible. In many of the poetry generator systems I researched, a corpus was often used as a starting point for lexical and sentiment information, as well as for providing subject matter and direction. The Basque poetry generation system, created by Manex Agirrezabal et al., in addition to the example projects listed in the markovify README were major sources of inspiration. In Basque poetry generation model, I was struck by the ‘Turing-like’ evaluation system which underscored how, for poems, human perception and taste plays a large role in how ‘good’ a poem truly is; gibberish garners a new meaning if it is written by a great poet, and a person can attach meanings to poetic words when compared to prose. Additionally, their use of POS-tags to guide word and line generation also inspired me, when trying to match the Limerick rhyme-scheme. This route differs from Almas Abdibayev et al. in “BPoMP: The Benchmark of Poetic Minimal Pairs – Limericks, Rhyme, and Narrative Coherence” who used bigrams in addition to rhyming words to fit the meter of a Limerick. Though I initially followed this route, I ran into infinite loops when no bigram produced a word that matched the rhyme-scheme. 

## How it Works!
My system works by first generating a Markovify Model of Project Gutenburg's corpus of published Limericks. Markovify is a very popular python library that can be helpful when trying to generate text inspired by a large corpus. What first drew me to this python library was the promise that "markovify.Text tries to generate sentences that do not simply regurgitate chunks of the original text" (markovify README). This relates to the idea of 'mere generation' which we have discussed in length. In this system, I lowered the max_overlap_value of the generated sentence from 15 to 5 since the lines of each poem are short. I experimented with higher and lower values, but 5 struck the balance between producing gibberish and simply copying lines form the corpus. In addition to the markovify library, I also used pronouncing and nltk to fix the semantics of the random lines produced and to follow the rules of a Limerick. Like stated previously, though the system does well when producing rhyming words with the help of pronouncing, since each line is generated in isolation to others, user input is helpful when bringing cohesion to the poem. Thus, the user defines what is a ‘good’ poem by offering input and being a ‘co-collaborator’ in the generation process. 
Ultimately, this project challenged me to take new avenues and not give up. There were many times when ideas did not translate well to code, and the amount I had to scale back was disheartening at times. If I had more time, I would love to revisit the anapestic rhythm of Limerick, because I did not realize how much it plays a role in a user's ability to discern that the poem generated is in fact a Limerick. This project is fairly simple to run—just download the system and run python generator.py in your terminal. From there, the system will prompt you for anything it needs from your end! I hope you enjoy!

## Sources
Abdibayev, Almas & Riddell, Allen & Rockmore, Daniel. (2021). BPoMP: The Benchmark of Poetic Minimal Pairs – Limericks, Rhyme, and Narrative Coherence. 1-9. 10.26615/978-954-452-072-4_001.

Agirrezabal, Manex & Arrieta, Bertol & Hulden, Mans & Astigarraga, Aitzol. (2013). POS-tag based poetry generation with WordNet.

Murati, Ermira. “Language & Coding Creativity.” Daedalus 151, no. 2 (2022): 156–67. https://www.jstor.org/stable/48662033.

https://github.com/jsvine/markovify

https://www.nltk.org

https://pypi.org/project/pronouncing/
