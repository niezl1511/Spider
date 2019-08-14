import json
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['medicin_1']['detail_item']
with open('final_rst.jsonlines','r') as f:
    rst = f.readlines()

# for i in rst:
#     try:
#         i = i.replace('\n','')
#         i = json.loads(i)
#         db.insert(i)
#     except:
#         print('error')

for i in rst:
    try:
        i = i.replace('\n', '')
        i = json.loads(i)
        print(i['name'].split(' ')[1])
    except:
        print('error')