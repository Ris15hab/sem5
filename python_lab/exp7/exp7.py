import re

pattern_email = r'\b[a-zA-Z0-9._+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+\b'
pattern_phone = r'\b[0-9]+-[0-9]+'
pattern_username = r'\b[a-zA-Z0-9_.+-]+@'
pattern_domain = r'@[a-zA-Z]+\.[a-z]+'
pattern_name = r'M\w*\.\s*\w*\s*\w*'

with open('sample.txt','r') as f1:
    data = f1.read()

emails = re.findall(pattern_email,data)
numbers = re.findall(pattern_phone,data)
username = re.findall(pattern_username,data)
domains = re.findall(pattern_domain,data)
name = re.findall(pattern_name,data)

print("-----------Emails----------------\n")
for i in emails:
    print(i)
print("-----------------------------------\n")
print("-----------Numbers----------------\n")
for i in numbers:
    print(i)
print("-----------------------------------\n")
print("-----------Username----------------\n")
for i in username:
    print(i[:-1])
print("-----------------------------------\n")
print("-----------Domains----------------\n")
for i in domains:
    print(i[1:])
print("-----------------------------------\n")
print("-----------Names----------------\n")
for i in name:
    print(i)
print("-----------------------------------\n")