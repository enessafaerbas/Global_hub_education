# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:40:16 2024

@author: Enes Safa
"""

file = open("employe_revenue.txt","r")
data = file.read()
#print(data)

lines=data.splitlines()
#print(lines)

string = lines[0]
strnig1=lines[1]
#print(string)

string=string.strip(" ")
strnig1=strnig1.strip(" ")
#print(string)
#print(strnig1)

string = string.lower()
#print(string)

string = string.capitalize()
#print(string)

split_string = string.split(" ")
#print(split_string)

name = split_string[0]
#print(name)

call_number=split_string[2]
#print(call_number)

for i in split_string:
    if "$" in i:
        average_deal_size = i.split("$")[0]
#print(average_deal_size)

dollars_index = split_string.index("dollars")
#print(dollars_index)

revenue_index = dollars_index - 1
#print(revenue_index)

revenue = split_string[revenue_index]
#print(revenue)




names = []
call_numbers = []
average_deal_sizes = []
revenues = []


for employe in lines:
    
    employe = employe.strip(" ")
    employe = employe.lower()
    employe = employe.capitalize()

    split_employe = employe.split(" ")
    
    name = split_employe[0]
    call_number = split_employe[2]
    
    
    for i in split_employe:
        if "$" in i:
            average_deal_size = i
    average_deal_size = average_deal_size.split("$")[0]
    
    
    dollars_index = split_employe.index("dollars")
    revenue_index = dollars_index-1
    revenue = split_employe[revenue_index]    
            
    average_deal_size = int(average_deal_size)
    call_number = int(call_number)
    revenue = int (revenue)
    
    names.append(name)
    call_numbers.append(call_number)
    average_deal_sizes.append(average_deal_size)
    revenues.append(revenue)
    
print("Names:",names)
print("Number of calls: ", call_numbers)
print("Average deal sizes: ", average_deal_sizes)
print("Revenues: ", revenues)
    
    
    
    
    
    
print(len(names))

IDs = list(range(0,11))
print(IDs)


dictionary1 = dict(zip(IDs,names))
print(dictionary1)
    
    
list1=["ben","Omer","karen"]
list2=[300,10,62,654,684]
dic=dict(zip(list1,list2))
print(dic)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









































