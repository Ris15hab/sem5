import xml.etree.ElementTree as ET
import pandas as pd 
import sqlite3

tree = ET.parse('xml_exp/file.xml')
root = tree.getroot()

FirstName = []
LastName = []
contact_nos = [] 
emails = []       
cities = []
states = []
zips = []

for employee in root.iter('Employee'):
    FirstName.append(employee.find('FirstName').text)
    LastName.append(employee.find('LastName').text)
    contact_nos.append(employee.find('ContactNo').text)
    emails.append(employee.find('Email').text)
    cities.append(employee.find('Address/City').text)
    states.append(employee.find('Address/State').text)
    zips.append(employee.find('Address/Zip').text)

employee = pd.DataFrame({
    'FirstName': FirstName,
    'LastName': LastName,
    'ContactNo': contact_nos,
    'Email': emails,
    'City': cities,
    'State': states,
    'Zip': zips
})

print(employee)

conn = sqlite3.connect(':memory:')
employee.to_sql('data',conn,index=False,if_exists='replace')

query = "SELECT * FROM data WHERE state = 'Florida' "
print(f"\n\n{query}\n\n")
result = pd.read_sql_query(query,conn)
print(result)