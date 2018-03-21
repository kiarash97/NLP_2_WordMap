#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""
from os import path
import operator
from persian_wordcloud.wordcloud import PersianWordCloud, add_stop_words

d = path.dirname(__file__)

emam_text = open(path.join(d, 'emam.txt'), encoding='utf-8').read()
shah_text = open(path.join(d, 'shah.txt'), encoding='utf-8').read()
# Add another stopword
stopwords = add_stop_words([])
# add_stop_words

# Generate a word cloud image
# wordcloud_emam = PersianWordCloud(
#     only_persian=True,
#     max_words=100,
#     stopwords=stopwords,
#     margin=0,
#     width=800,
#     height=800,
#     min_font_size=1,
#     max_font_size=500,
#     background_color="Black"
# ).generate(emam_text)
#
# wordcloud_shah = PersianWordCloud(
#     only_persian=True,
#     max_words=100,
#     stopwords=stopwords,
#     margin=0,
#     width=800,
#     height=800,
#     min_font_size=1,
#     max_font_size=500,
#     background_color="Black"
# ).generate(shah_text)



emamDict = {}
shahDict = {}
emamList = emam_text.split(" ")
shahList = shah_text.split(" ")
junkList = ["." , "-" , "]" , "[" , "،" , "؛" , ":", " " ]
junkWords = ["که","از","با","برای","با","به","را","هم",  "و" , "در"  ,"تا","یا" ]

for word in emamList :
    for char in junkList :
        if char in word :
            word = word.replace(char, "")
    if word not in junkWords :
        if word in emamDict:
            emamDict[word]+=1
        else:
            emamDict[word]=1
sorted_emam = sorted(emamDict.items(), key=operator.itemgetter(1))
print (sorted_emam)

for word in shahList :
    for char in junkList :
        if char in word :
            word = word.replace(char, "")
    if word not in junkWords :
        if word in shahDict:
            shahDict[word]+=1
        else:
            shahDict[word]=1
sorted_shah = sorted(shahDict.items(), key=operator.itemgetter(1))
print (sorted_shah)



#
# image_emam = wordcloud_emam.to_image()
# image_emam.show()
# image_emam.save('emam.png')
#
# image_shah = wordcloud_shah.to_image()
# image_shah.show()
# image_shah.save('shah.png')