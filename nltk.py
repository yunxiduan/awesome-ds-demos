# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:38:44 2017

@author: lduan
"""
import nltk
nltk.download()

from nltk.book import *

# Introductory Examples for the NLTK Book ***
#Type the name of the text or sentence to view it.
#Type: 'texts()' or 'sents()' to list the materials.
text1
text2

# There are many ways to examine the context of a text apart from simply reading it. 
# A concordance view shows us every occurrence of a given word, together with some context. 
# Here we look up the word monstrous in Moby Dick by entering text1 followed by a period, then the term concordance, 
# and then placing "monstrous" in parentheses:
    
text1.concordance("monstrous")

# A concordance permits us to see words in context. For example, we saw that monstrous occurred in contexts such as the ___ pictures and a ___ size . What other words appear in a similar range of contexts? We can find out by appending the term similar to the name of the text in question, then inserting the relevant word in parentheses:

text1.similar("monstrous")

# Austen uses the word differently from Melville
text2.similar("monstrous")

#The term common_contexts allows us to examine just the contexts that are shared by two or more words, such as monstrous and very. We have to enclose these words by square brackets as well as parentheses, and separate them with a comma:
text2.common_contexts(["monstrous", "very"])    

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

#Counting Vocabulary
len(text3) #44764 words
#Tokenize
sorted(set(text3)) 
len(set(text3)) #2789 tokens
#Calculate lexical diversity:
len(text3)/len(set(text3)) 
#16.050197203298673
#Each word is used about 16 times

#Take a look at specific words
text3.count("smote")

text5.count("lol")

100*text5.count("lol")/len(text5)
#"lol" is 1.6% of all words appearing in chat log

#Some functions
def lexical_diversity(text):
    return len(set(text))/len(text)

print (lexical_diversity(text5))
#number of distinct words is 13% of total words

def percentage(count, total):
    return 100*count/total

print (percentage(text4.count('a'),len(text4)))
#'a' is 1.5% of the corpus of the Inaugural Addresses    
    