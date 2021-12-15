import pandas

data = pandas.read_csv("squirrels.csv")


#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()
#print(data["temp"].max())

#print(data.temp)

#Get data in row

#x = data[data.day == "Monday"]

#print(data[data.day == "Monday"])
#print(data["temp"])

#print(data[data.temp == data.temp.max()])

#create a dataframe from scratch

#dict_test = {
#  "students": ["Amy", "James", "Angela"],
#  "scores": [76, 56, 65]
#}

#x = pandas.DataFrame(dict_test)
#print(x)
#x.to_csv("new_data.csv")
#----------------------------------------------
#gray 2473, red 392, black 103

#print(data["Primary Fur Color"])

#gray = 0
#red = 0
#black = 0
#for x in data["Primary Fur Color"]:
#  if x == "Gray":
#    gray += 1
#  elif x == "Cinnamon":
#    red += 1
#  elif x == "Black":
#    black += 1

colors = data["Primary Fur Color"].dropna().unique()

count_data = []
count_data.append(len(data[data["Primary Fur Color"] == "Gray"]))
count_data.append(len(data[data["Primary Fur Color"] == "Cinnamon"]))
count_data.append(len(data[data["Primary Fur Color"] == "Black"]))

sq_dict = {
  "Fur Color": colors,
  "Count": count_data
}

df = pandas.DataFrame(sq_dict)
df.to_csv("sqs.csv")