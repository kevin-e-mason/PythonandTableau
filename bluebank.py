# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:56:54 2022

@author: Kevin Mason
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#ransform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#working with arrays
#1D array
arr = np.array([1,2,3,4])

#0D array
arr = np.array(43)

#2D array
arr = np.array([[1,2,3,], [4,5,6]])

#Working with IF statements

a = 40
b = 500
if b > a:
    print('b is greater than a')
    
#Let's add more conditions
a = 40
b = 500
c = 1000

if b > a and b < c:
    print('b is greater than a but less than c')

a = 40
b = 500
c = 20

if b > a and b < c:
    print('b is greater than a but less than c')
else:
    print('No conditions met')
    
#another condition, different metrics

a = 40
b = 0
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('No conditions met')
    
    
  #using 'or'  
a = 40
b = 500
c = 30

if b > a or b < c:
    print('b is greater than a or less than c')
else:
    print('No conditions met')
    
    
fico = 250
    
# fico >= 300 and < 400:  'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'  
    
if fico >= 300 and fico < 400:
     ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    fico  = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)
    
   
#for loops   

fruits = ['apple' , 'pear' , 'banana', 'cherry']

for x in fruits:
    print(x)
    y = x +' fruit'
    print(y)

for x in range(0,4):
    y = fruits[x] + ' for sale'
    print(y)

#applying for loops to loan data

#using first 10

#while loops

i = 1
while i < 10:
    print(i)
    i = i + 1


length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
            
    except:
        cat = 'Unknown'
        
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat


    
#df.lock as conditional satements
# df.loc[df[columnname] condition, newcolumnname] = 'value if the condition is met'

#for interest rates, a new column is wanted. if the rate >0.12 then high, else low

loandata.loc[loandata['int.rate']  > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate']  <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()

purposecount.plot.bar()

purposecount.plot.bar(color = 'red', width = 0.2)
plt.show()

#scater plots

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()


#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)

#





























