# import csv
# with open("weather.csv") as f:
#     data=csv.reader(f)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#             temp=row[1]
#             temperatures.append(int(temp))
#     print(temperatures)

import pandas
#
# data=pandas.read_csv("weather.csv")
# # hey=(data["temp"])
# # templist=data["temp"].to_list()
# # print(templist)
# # sum=0
# # for i in templist:
# #     sum+=i
# # average=float(sum/len(templist))
# # print(average)
# # high=hey.max()
# # print(high)
# hey =data.temp
# print(hey)
# max1=hey.max()
#
# print(data[data.temp==max1])

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251104.csv")
hey=data["Primary Fur Color"]
print(hey)
list1=data["Primary Fur Color"].to_list()
count1=list1.count("Gray")
print(count1)
count2=list1.count("Cinnamon")
print(count2)
count3=list1.count("Black")
print(count3)
colors=["Black","Gray","Cinnamon"]
dict1={"Colors": ["Black","Gray","Cinnamon"],
       "counts": [count3,count1,count2] }
print(dict1)
data1=pandas.DataFrame(dict1)
data1.to_csv("new.csv")

