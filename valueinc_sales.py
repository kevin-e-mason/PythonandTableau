# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:08:17 2022

@author: Kevin Mason
"""

import pandas as pd
# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction.csv') 

data = pd.read_csv('transaction.csv',sep=';') 

#summary of the datat
data.info()

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem  - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem  * NumberOfItemsPurchased 
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']

NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem  * NumberofItemsPurchased

#adding a new colun to a dataframe

data['CostPerTransaction'] = CostPerTransaction

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem']* data['NumberOfItemsPurchased']

#Profi per Transaction

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction'] 

#Markup = (Sales - Cost)/Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction'] 

data['Markup'] = (data['ProfitPerTransaction']) / data['CostPerTransaction'] 

#Rounding Marking

roundmarkup = round(data['Markup'], 2)


data['Markup'] = round(data['Markup'], 2) 


#Combining data fields

my_name = 'Kevin' + 'Mason'

my_date = 'Day' + '-' + 'Month' + '-' +'Year'

#my_date = data['Day'] + '-'

#checking columns data type
print(data['Day'].dtype)

#Change colunns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)



print(year.dtype)


my_date = data['Month'] + '-' +day + '-' + year

data['date'] = my_date


#Using iloc to view specific columns/rows

data.iloc[0] #views the row with index = 0


data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last five rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows in the 2nd column

data.iloc[4,2] #brings in the value for the 4th rou, 2nd column



#using split to spliet the client keyworks field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' ,  expand = True)

#creating new columns for the split coluns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]


#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')


#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset


seasons = pd.read_csv('value_inc_seasons.csv', sep = ';') 

#mering files: merge_dr = pd.merge(dr_old, df_new, on = 'key')

data = pd.merge(data,seasons, on = 'Month')

#dropping columns

# df = dr.drop('columnname', axis = 1)

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)

#data = data.drop(['Year' , 'Month' , 'LenghtofContract'], axis = 1)

#Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)

#index =  false means the index column will not be transferred.





























