"""
Pseudocode:
1. user input for subject of Limerick & 2 nouns for metaphors/comparisons
2. Generates first line of poem in keeping with meter using pronoucing
    library
3. tracks the last word in first line and uses pronouncing library to generate
    list of words that rhyme with it, A
4. randomly chooses a word from A and reverse engineers line 2  
5. generates third line of poem incorperating one noun for metaphor
6. tracks the last word of the third line and uses prounoucing library to 
    generate list of words that rhyme with it, B
7. randomly chooses a word from B and reverse engineers line 4 while also 
    including the second noun from the poem
8. randomly chooses a word from A and reverse engineers line 5

TODO:
1. import pronoucing library
2. incode meter rules of a limerick and define a word genertaions method 
3. use ConceptNet to 
"""