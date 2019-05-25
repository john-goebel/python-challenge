import csv
import pandas as pd
import os

#csvpath = os.path.join("..", "data", "budget_data.csv")
csvpath2 = "data/budget_data.csv"
profitMax = 0
profitMin = 0
totProfit = 0
profits = []
totMonths = 0

periodProfitMax = ""
periodProfMin = "" 


# print(csvpath2) # for checking filepath of csv data

def average(numbers):
    length = len(numbers)
    total = 0
    for number in numbers:
        total += number
    return total / length


with open(csvpath2, newline='') as dataFile:
    csvreader = csv.reader(dataFile, delimiter=',')
    
    csv_header = next(csvreader)

    for row in csvreader:
        if float(row[1]) > profitMax:
            profitMax = float(row[1])
            periodProfMax = row[0]
        if float(row[1]) < profitMin:
            profitMin = float(row[1])
            periodProfMin = row[0]
        totMonths = totMonths + 1
        totProfit = totProfit + float(row[1])
        
        profits.append(float(row[1]))


print("There are "+ str(totMonths) + " months in the data")    
print("The largest profit was in " + periodProfMax + " and was : $", format(profitMax, ",.2f"))
print("The largest loss was in " + periodProfMin + " and was: $", format(profitMin, ",.2f"))
print("The total profits over the entire period is: $", format(totProfit,",.2f"))
print("The average monthly profit is: $", format(average(profits), ",.2f"))


#print(dailyProfitMax)
#print(dailyProfitMin)



