import csv 
import math
from os import read

with open("data.csv", newline="") as f:
    readfile = csv.reader(f)
    file_data = list(readfile)

data = file_data[0]

num = len(data)
total = 0

for x in data:
     total = total + int(x)

mean = total/num
print("Mean is :" + str(mean))

    

squaredList = []
for num in data:
    diff = int(num)-mean 
    diff = diff**2
    squaredList.append(diff)

sum = 0
for i in squaredList:
    sum = sum + i
result = sum/(len(data)-1)

std = math.sqrt(result)
print("Standard Deviation is : " + str(std))
