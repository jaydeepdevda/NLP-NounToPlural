# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:04:04 2017
This script is simple conversion a word from Noun to Plural
@author: Jaydeep

noun to plural

10 Examples:

1. tree -> trees
2. lake -> lakes
3. window -> windows
4. story -> stories
5. butterfly -> butterflies
6. glass -> glasses
7. wish -> wishes
8. pitch -> pitches
9. bus -> buses
10. box -> boxes

"""

#function nounToPlural which take a word as argument and return Plural of that word
def nounToPlural(noun):
    
    if (noun.endswith("y")):
        #remove "y" with "ies"
        return noun[0:-1]+"ies";
    
    elif (noun.endswith("ss") or noun.endswith("sh") or noun.endswith("ch")):
        #append "es"
        return noun+"es";
    
    elif (noun.endswith("s") or noun.endswith("x")):
        #append "es"
        return noun+"es";
    
    else :
        #for general cases append "s"
        return noun+"s";
# end of function nounToPlural
    
print "Please Enter Noun you want to convert to Plural:"
#input word from console
inputNoun = raw_input();
#Convert to lower case
inputNoun = inputNoun.lower();
#input word
print "Noun  : "+inputNoun;
#Output Plural of input Word
print "Plural: "+nounToPlural(inputNoun);
