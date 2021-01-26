import load_data
import pymongo

values = load_data.data()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sp500"]

mycol = mydb["stock"]

if mycol.count() != 0:
    mycol.drop()


x = mycol.insert_many(values)

print("Done")