# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:19:41 2024

@author: Enes Safa
"""

names=['Ben','Omer','Karen','Celine','Sue','Bora','Rose','Ellen','Bob','Taylor,','Jude']
call_numbers=  [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
average_deal_sizes =  [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues =  [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]


import numpy as np

data = np.array([], dtype = int)


def append_names(name_list):
    global data
    for i in name_list:
        data=np.append(data,names.index(i))
        
    
def append_performance_measures(feature_list):
    global data
    data = np.append(data,feature_list)


append_names(names)
append_performance_measures(call_numbers)
append_performance_measures(average_deal_sizes)
append_performance_measures(revenues)

#print(data)
#print(data.shape)

data =data.reshape(4,11)
#print(data)
#print(data.shape)


def calculate_performance (employe_name):
    idx= names.index(employe_name)
    
    number_of_calls = data[1][idx]
    avg_deal_size = data[2][idx]
    revenue = data[3][idx]
    
    
    score=(avg_deal_size*revenue)/number_of_calls
    
    return score

#print(calculate_performance("Ellen"))
    



performance_scores=[]
for name in names:
    score = int(calculate_performance(name))
    performance_scores.append(score)
    
    
    
data=np.concatenate((data,[performance_scores]),axis=0)
print(data)

idx_best_employe = np.argmax(data[4])
idx_worst_employe = np.argmin(data[4])

print(f" Best Performing Employe: {names[idx_best_employe]}")
print(f" worst performing Employe: {names[idx_worst_employe]}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











































