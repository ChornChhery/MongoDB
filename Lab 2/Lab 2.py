# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:46:01 2024

@author: Dell PC
"""

import requests
from pymongo import MongoClient

client = MongoClient()
db = client["Mflix"]

movies_collection = db.movies
filter={}
#Count all of document in movies
n_movie = db.movies.count_documents(filter)
print(n_movie)

db_names = client.list_database_names()
print(db_names)

movies = db.movies.find_one()
print(movies)

movie_fields = list(movies.keys())
print(movie_fields)


count_moive = {"languages":"English"}
count = db.movies.count_documents(count_moive)
print(count)


db.movies.count_documents({"year":{"$gte":2015}})


genres_field = db.movies.distinct("genres");
for x in genres_field:
   print(x)
print(len(genres_field))
print(genres_field)


genres_movie = {"genres":{"$in":["Action","Comeday","Fantasy"]}}
count_genres = db.movies.count_documents(genres_movie)
print(count_genres)


rated_field = db.movies.distinct("rated")
for i in rated_field:
    print(i)
print(len(rated_field))



rated_movie = {"rated":"PG"}
count_rated = db.movies.count_documents(rated_movie)
print(count_rated)



db.movies.count_documents({"rated":"PG"})
rate_movie = db.movies.find({"rated":"PG"})
for j in rate_movie:
    print(j['title'])

print(len(rate_movie))


musical = {"genres":"Musical"}
count_muscial = db.movies.count_documents(musical)
print(count_muscial)


db.movies.count_documents({"genres":"Musical"})
title_movie = db.movies.find({"genres":"Musical"})
for k in title_movie:
    print(k['title'])


thailand = {"countries":"Thailand"}
count_thai = db.movies.count_documents({"countries":"Thailand"})
print(count_thai)


thailand = {"countries":"Thailand"}
title_thai = db.movies.find({"countries":"Thailand"}).sort({"year":-1})
for m in title_thai:
    print("Title: "+ m["title"])
    print("Years: "+ str(m["year"])+"\n")





