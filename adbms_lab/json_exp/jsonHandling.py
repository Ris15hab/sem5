import json
with open('./data.json','r') as file:
    data = json.load(file)
if data:
    print ("Name\t\tEmail\t\t\tPhone\t\tCity\t\tState\t\tZip")
    for id,info in data.get('users').items():
        print(f"{info['name']}\t{info['email']}\t\t{info['phone']}\t{info['address']['city']}\t\t{info['address']['state']}\t\t{info['address']['zip']}")
else:
    print("No Data")