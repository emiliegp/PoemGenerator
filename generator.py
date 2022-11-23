"""
Emilie Grand'Pierre 
Computational Creativity (CSCI 3725)
M6: Poetry Slam
9/15/2022

This file works as the main method of the poetry generator, Using the Liemrick 
class and user input, this system produces a Liemrick-like poem inspried by 
the publichsed Limericks within Porject Gutenburg. 
"""

import Globals
import Limerick 

def main():
    gen_more_poems = True
    Globals.init()
    poem = Limerick.Limerick()
    print("This is an interactive poem generation experience. From a corpus" + \
        "\nof about 3000 lines of Limericks gathered from Project Gutenburg," +\
        "\nthis systems builds Limerick-like poems!\n")
    
    print("\nFirst lets see where the system begins...")
    while gen_more_poems:
        poem.gen_poem()
        print(poem)
        poem.say_poem()

        user_input = input("\nDid you like the poem generated? (Y/N) \n")
        if user_input == "N":
            print("\nAlirght let's try to change some things... \n")
            poem.fix_pronounsa()
            print(poem)
            poem.say_poem()
            print('\nHopefully that was better! \n \n')

        more_poems = input("Thank you for using the Poem Generator! Would you" +\
            " like to generate a new poem? (Y/N)\n")
        if more_poems == "N":
            gen_more_poems = False
    
    print("Thank you for creating poems with us!")
    

if __name__ == "__main__":
    main()
