#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:06:01 2018

@author: yatingupta
"""
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

dataset = "Shah Jahan was widely considered to be the most competent of Emperor Jahangir's four sons and after Jahangir's death in late 1627, when a war of succession ensued, Shah Jahan emerged victorious. He put to death all of his rivals for the throne and crowned himself emperor in January 1628 in Agra under the regnal title Shah Jahan (which was originally given to him as a princely title). Although an able military commander, Shah Jahan is perhaps best remembered for his architectural achievements. The period of his reign is widely considered to be the golden age of Mughal architecture. Shah Jahan commissioned many monuments, the best known of which is the Taj Mahal in Agra, which entombs his beloved wife Mumtaz Mahal             In September 1657, Shah Jahan fell seriously ill, which set off a war of succession among his four sons, in which his third son Aurangzeb, emerged victorious.[10] Shah Jahan recovered from his illness, but Aurangzeb put his father under house arrest in Agra Fort from July 1658 until his death in January 1666.[11] On 31 July 1658, Aurangzeb crowned himself emperor under the title Alamgir"
x = len(dataset)

'''only keeping the letters'''
review = re.sub('[^a-zA-Z]',' ',dataset)
'''lowercase'''
review = review.lower()
''' removing non significant words'''
review = review.split()
review = [word for word in review if not word in set(stopwords.words('english'))]
'''making it a string from the list'''
review = ' '.join(review + "/n")

y = len(review)
