import json

data = '''{
  "name" : "chuck",
  "phone" : {
   "type" : "intl",
   "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }
} '''

info = json.loads(data)
print('Name:', info["name"])
#print('phone:', info["number"])
print('Hide:',info["email"]["hide"])



particular = '''{
  "name" : "Catherine",
  "phone" : {
  "type" : "float",
  "number" : "0.05"
  },
  "email" : {
  "hide" : "yes"
  }
}'''

info = json.loads(particular)
print(info["name"])
print(info["phone"])
print(info["email"])