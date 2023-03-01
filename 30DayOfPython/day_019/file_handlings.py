# Day 19: 30 days of python programming
# importing required libraries
import re, json, csv

'''Write a function which count number of lines and number of words in a text.
All the files are in the data folder: a) Read obama_speech.txt file and count number of lines and words 
b) Read michelle_obama_speech.txt file and count number of lines and words 
c) Read donald_speech.txt file and count number of lines and words 
d) Read melania_trump_speech.txt file and count number of lines and words'''

def count_words_lines(file):
    with open(file) as f:
        lines = f.readlines()
        words = []
        for line in lines:
            # removing all characters that are not whitespace or alphanumeric using regex
            line = re.sub(r'[^\w\s]','',line)
            words.extend(line.split())
    print(f'The number of lines and words in the file are {len(lines)} and {len(words)} respectively')
count_words_lines('day_019/melania_trump_speech.txt')
count_words_lines('day_019/donald_speech.txt')
count_words_lines('day_019/michelle_obama_speech.txt')
count_words_lines('day_019/obama_speech.txt')