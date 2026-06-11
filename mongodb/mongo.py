from pymongo import MongoClient


client = MongoClient("mongodb+srv://Abhiram:ms6q5zWQ13Aur9bH@cluster0.eybperp.mongodb.net/?appName=Cluster0")
db = client['synnfo_school']
collection = db['students']

student = {"name":"Amal","course":"Python","std_id":"SYN001"}
# print(type(student))
students = [
    {"name":"Nijin","course":"MERN","std_id":"SYN002"},
    {"name":"Aswin","course":"Flutter","std_id":"SYN003"},
    {"name":"Tom","course":"Python","std_id":"SYN004"},
    {"name":"George","course":"Data Science","std_id":"SYN005"}
]
# collection.insert_one(student)
# collection.insert_many(students)

# for x in collection.find():
#     print(x)
# for x in collection.find({'course':"Python"}):   #filter
#     print(x)

# print(collection.find_one({'course':'Python'}))

# collection.update_one(
#     {"std_id":"SYN003"},  #filter
#     {"$set":{"name":"Aswin Shaji"}}  #update
# )

# print(collection.find_one({"std_id":"SYN003"}))

# collection.delete_many({"course":"Python"})
# collection.delete_one({"std_id":"SYN003"})
# for x in collection.find({},{"name":1}):
#     print(x)

# for x in collection.find({},{"std_id":0}):
#     print(x)

for x in collection.find({},{"name":1,"_id":0}):
    print(x)