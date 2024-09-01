# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:29:46 2024

@author: Dell PC
"""

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin123@cluster0.fsqwm.mongodb.net/")

db = client['sample_mflix']

filter={}

n_movies = db.movies.count_documents(filter)
print(n_movies)
 



docs = db.movies.find({'year':{"$gte":1946}},
       projection={"title":1,'year':1,"genres":1}).sort([('year',1)])

for doc in docs[:10]:
    year = doc['year']
    title = doc['title']
    print(f"{year} {title}")






docs = db.movies.find({},
       projection={"title":1,'year':1,'rated':1,'imdb.rating':1}).sort([('imdb.rating',-1)])

for doc in docs[:100]:
    year = doc['year']
    title = doc['title']
    rate = doc.get('rated','Not Rated')
    imdb_rating = doc.get('imdb.rating','Not Rated')
    print(f"{year} {title}\n\t Rated: {rate}, IMDb Rating: " +str(doc['imdb']['rating']))   



docs=db.movies.find({'type':'series','countries':'Japan'},
    projection={"title":1,'year':1,"plot":1,"imdb.rating":1}).sort([("imdb.rating",-1)])

for doc in docs[:10]:
    year = doc['year']
    title = doc['title']
    imdb_rating = doc.get('imdb.rating','Not Rated')
    plot = doc.get('plot','unknown')
    print(f"{year} {title}\n\t IMDb Rating: "+str(doc['imdb']['rating'])+ f"\n\t Plot: "+str(doc['plot'])+"\n")




docs = db.movies.find({"countries":"Thailand"},
                      projection={'year':1,'runtime':1,'title':1}).sort([('year',-1)])

print(f"{'Year':}   {'Runtime':}    {'Title'}")
print("-" * 50)

for doc in docs[:50]:
    year = doc['year']
    title = doc['title']
    runtime = doc.get('runtime','unknown')
    print(f"{year}   {runtime}    {title}")



docs = db.movies.find({"directors.4":{"$exists":True}},
    projection={'year':1,'title':1,'directors':1}).sort([('year',-1)])
print(f"{'Year':}      {'Title'}")
print("-"*50)
for doc in docs[:20]:
    year = doc['year']
    title = doc['title']
    directors = doc.get('directors', []) 
    directors_str = ', '.join(directors)
    print(f"{year:}      {title}")
    print(f"Directors:\t{directors_str}\n")


# Query to find movies with at least 5 directors
docs = db.movies.find(
    {"directors.4": {"$exists": True}},  # Ensure that the fifth director exists, implying at least 5 directors
    projection={'year': 1, 'title': 1, 'directors': 1}  # Project only the required fields
).sort([('year', -1)])  # Sort by year, from most recent to oldest

# Print header
print(f"{'Year':<5} {'Title'}")
print("-" * 50)

# Loop through the results and print them in the desired format
for doc in docs[:20]:  # Limit to the first 20 results
    year = doc['year']
    title = doc['title']
    directors = doc.get('directors', [])  # Get the list of directors or an empty list if missing
    # Join the directors list into a single string separated by commas
    directors_str = ', '.join(directors)

    print(f"{year:<5} {title}")
    print(f"Directors:\t{directors_str}\n")



docs = db.movies.find({"year":{"$gte":2000},"countries":"Cambodia"},
                      projection={"title":1,"year":1,"rated":1,"imdb.rating":1}).sort([('year',1)])
for doc in docs[:10]:
    year = doc['year']
    title = doc['title']
    imdb_rating = doc.get('imdb.rating','Not Rated')
    print(f"{year} {title}\n\t Rated: {rate}, IMDb Rating: " +str(doc['imdb']['rating']))
    













