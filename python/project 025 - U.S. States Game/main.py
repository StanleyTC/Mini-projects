import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_counter = 0
cinnamon_counter = 0
black_counter = 0

if data[data["Primary Fur Color"]=="Black"]:
    black_counter +1

if data[data["Primary Fur Color"]=="Cinnamon"]:
    cinnamon_counter +1

if data[data["Primary Fur Color"]=="Gray"]:
    gray_counter +1



print(black_counter)