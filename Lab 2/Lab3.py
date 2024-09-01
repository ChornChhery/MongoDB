# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:13:00 2024

@author: Dell PC
"""

import requests
from pymongo import MongoClient
client = MongoClient()
db = client["Mflix"]

db.movies.distinct('type')


db.movies.find_one({"languages.2":{"$exists":True}})


db.movies.count_documents({"languages.2":{"$exists":True}})

db.movies.distinct("languages")

len(db.movies.distinct("languages"))

db.movies.count_documents({"languages":"Thai"})

db.movies.distinct("genres")

db.movies.count_documents({"languages":{"$all":['Thai','English']}})


result=db.movies.find({"languages":{"$all":['Thai','English']}})
for i in result:
    print(str(i['year'])+' '+i['title'])
    
    
rate=db.movies.find({"imdb.rating":{"$gt":7}})
for i in rate:
    print(str(i['imdb']['rating'])+' '+i['title'])


db.movies.find({"tomatoes.rating":{"$gt":4}})
rat=db.movies.find({"tomatoes.viewer.rating":{"$gt":4}})
for i in rat:
    print(str(i['tomatoes']['viewer']['rating'])+' '+i['title'])

award_win=db.movies.find({"awards.wins":{"$gt":0}})
for j in award_win:
    print(str(j['awards']['wins'])+' '+j['title'])


cursor2 = db.movies.find({"awards.nominations" : {"$gt":0}},
                         {"title":1,'awards':1,'runtime':1,'languages':1,'released':1,'directors':1,'writers':1,'countries':1,'type':1,'year':1})
for x in cursor2:
    print(str(x['awards']['nominations'])+' '+x['title']+' '+str(x['year'])+' ' +str(x['type']))


cast=db.movies.find(
    {"cast":'Focus Jirakul'},
    {"title":1,'languages':1,'award':1,'runtime':1,'year':1,'type':1,'released':1,'directors':1,'writers':1,'countries':1}
    )
for i in cast:
    print(i)
    
db.movies.find_one(
    {"title":{"$regex":'scene','$options':'i'}},
    {"title":1,'languages':1,'released':1,'directors':1,'writers':1,'countries':1}
 )


rating=db.movies.find(
    {"tomatoes.viewer.rating":{"$gte":3,"$lt":4}},
    {"title":1,'languages':1,'released':1,'directors':1,'writers':1,'countries':1}
    )
for x in rating:
    print(x)
    
    
    
runtimes = db.movies.find(
    {"runtime":{"$gte":60,"$lte":90}},
    {"title":1,'languages':1,'released':1,'directors':1,'writers':1,'countries':1}
    )
for x in runtimes:
    print(x)
    
fires = db.movies.find(
    {"fullplot":{"$regex":"fire","$options":'i'}},
    {"title":1,'languages':1,'released':1,'directors':1,'writers':1,'countries':1}
    )
    
for j in fires:
    print(j)
    



 
   
    
