# -*- coding: utf-8 -*-
#import requests
from pymongo import MongoClient

client = MongoClient()
db = client["nobel"]

laurest_collection = db.laureates
filter = {}


n_laurestes = db.laureates.count_documents(filter)
print(n_laurestes)

db.names = client.list_database_names()
print(db.names)

laurestes = db.laureates.find_one()
print(laurestes)

prizes = db.prizes.find_one()
print(prizes)

print(type(laurestes))

laurestes_fields = list(laurestes.keys())
print(laurestes_fields)


prizes_field = list(prizes.keys())
print(prizes_field)


db.laureates.count_documents({"born":{"$lt":"1900"}})
db.laureates.count_documents({"born":{"$gt":"1900"}})

db.laureates.count_documents({"diedCountry":"USA"})
db.laureates.count_documents({"diedCountry":"USA","bornCountry":"Germany"})


db.laureates.count_documents({"diedCountry":"USA",
                              "bornCountry":"Germany",
                              "firstname":"Albert"})


db.laureates.find_one({"diedCountry":"USA",
                              "bornCountry":"Germany",
                              "firstname":"Albert"})


for x in db.laureates.find_one({"diedCountry":"USA",
                              "bornCountry":"Germany",
                              "firstname":"Albert"}):
    print(x)

db.laureates.count_documents({"bornCountry":{"$in":["USA","Canada","Mexico"]}})    



db.laureates.count_documents({"diedCountry":"USA","bornCountry":{"$ne":"USA"}})


db.laureates.find_one({"prizes.2":{"$exists":True}})

db.laureates.find_one({"prizes.2":{"$exists":True}})




db.laureates.find_one({"prizes.2":{"$exists":True}})


db.laureates.distinct("gender")

db.laureates.distinct("prizes.category")



db.prizes.find_one()


count = len(db.laureates.distinct("prizes.affiliations.country"))
print(count)



# this prizes will give or share to 4 people
db.laureates.find_one({"prizes.share":"4"})


db.laureates.count_documents({"prizes.category":"physics"})

list(db.laureates.find({"prizes.share":"4"}))


share4 = db.laureates.find({"prizes.share":"4"})
for x in share4:
    print(x)

    
len(list(db.laureates.find({"prizes.share":"4"})))


# in one category share 4 gift in that team
db.laureates.distinct(
    "prizes.category",{"prizes.share":"4"}
    )


db.laureates.count_documents({"prizes.1":{"$exists":True}})



db.laureates.distinct("prizes.category",{"prizes.1":{"$exists":True}})



db.laureates.count_documents({"prizes.category":"physics"})

db.laureates.count_documents({"prizes.category":"medicine"})


db.laureates.count_documents({"prizes.category":{"$ne":"physics"}})

db.laureates.count_documents({"prizes.category":{"$in":["chemistry","physics","medicine"]}})


db.laureates.count_documents({"prizes.category":{"$nin":["chemistry","physics","medicine"]}})




db.laureates.count_documents({"prizes.category":"physics","prizes.share":"1"})



db.laureates.count_documents({"prizes":{"$elemMatch":{"category":"physics","share":"1"}}})


db.laureates.distinct("bornCountry",{"bornCountry":{"$regex":"Poland"}})



assert set(case_sensitve)== set(case_insensitve)




doc=db.laureates.find(filter={
                          "firstname":{"$regex":"^G"},
                          "surname":{"$regex":"^S"}})

print(doc[0])



doc=db.laureates.find(filter={
                          "firstname":{"$regex":"^G"},
                          "surname":{"$regex":"^S"}},
                      projection={'firstname':1,'surname':1}  )

print(doc[1])




docs = db.laureates.find(
    filter={"firstname":{"$regex":"^G"},
            "surname": {"$regex":"^S"}},
    projection=['firstname','surname'])

full_names= [doc['firstname']+" "+ doc['surname'] for doc in docs ]

print(full_names)

print(len(full_names))


db.prizes.find_one({})

prizes= db.prizes.find({},{"laureates.share":1})

for prize in prizes:
    total_share = 0
    for laureate in prize["laureates"]:
        total_share += 1/ float(laureate['share'])
        
    print(total_share)


prizes = db.prizes.find({}, {"laureates.share":1})
print(prizes[1])


doc = list(db.laureates.find(
    {'born': {"$gte":"1900"}, "prizes.year": {"$gte":"1954"}},
    {'born':1, "prizes.year":1, "_id":0}, sort=[('born',-1),('prizes.year',1)]))
for docs in doc[:5]:
    print(docs)
    

docs = db.prizes.find(filter={'category':'physics'},
                       projection=['year','laureates.firstname','laureates.surname'],
                       sort=[('year',1)])
count = 0
for doc in docs:
    print(doc)
    count=count+1
    
print(count)








from operator import itemgetter
def all_laureates(prizes):
    # Sort the laureates by surname
    sorted_laureates = sorted(prizes['laureates'], key=itemgetter('surname'))
    surnames = [laureate['surname'] for laureate in sorted_laureates]
    all_names = " and ".join(surnames)
    return all_names

print(all_laureates)





from operator import itemgetter
def all_laureates(prizes):
    # Sort the laureates by surname
    sorted_laureates = sorted(prizes['laureates'], key=itemgetter('surname'))
    surnames = [laureate['surname'] for laureate in sorted_laureates]
    all_names = " and ".join(surnames)
    return all_names

docs = db.prizes.find(
    filter={"category":"physics"},
    projection= ['year', "laureates.firstname", "laureates.surname"],
    sort=[('year',1)]
    )

for doc in docs:
    print("{year} : {names}".format(year=doc['year'],names=all_laureates(doc)))




index_model = [('category',1),('year',-1)]
db.prizes.create_index(index_model)

report =""
for category in sorted(db.prizes.distinct("category")):
    doc = db.prizes.find_one(
        {'category': category, "laureates.share":"1"},
        sort = [('year',-1)]
        )
    report += "{category} : {year}\n".format(**doc)
    
print(report)



from collections import Counter
db.laureates.create_index([('bornCountry',1)])
n_born_and_affilited = {
    country: db.laureates.count_documents({
        "bornCountry": country,
        "prizes.affiliations.country": country
        })
    for country in db.laureates.distinct("bornCountry")
}

five_most_common = Counter(n_born_and_affilited).most_common(5)
print(five_most_common)



list(db.prizes.find({
     "category": "economics"},
    {"year":1, "_id":0})
    .sort("year").limit(3).limit(5)
    )


from pprint import pprint
filter_ = {"laureates.share":'4'}
projection = ['category','year','laureates.motivation']
cursor = db.prizes.find(filter_, projection).sort('year').limit(5)
print(list(cursor))

