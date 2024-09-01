# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:29:46 2024

@author: Dell PC
"""

from pymongo import MongoClient

client = MongoClient()

db = client['Mflix']

filter={}

n_movies = db.movies.count_documents(filter)
print(n_movies)
 

db.movies.find({})

