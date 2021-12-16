import random

# LIST COMPREHENSION PRACTICE
numbers = [1, 2, 3]
new_list = [n*2 for n in numbers]
print(new_list)
#-----------------------------------------------------------------

times_two = [i*2 for i in range(1,5)]
print(times_two)
#-----------------------------------------------------------------

names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
new = [name.upper() for name in names if len(name) > 4]
print(new)
#-----------------------------------------------------------------

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in nums]
print(squared_numbers)
#-----------------------------------------------------------------

random_nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in random_nums if n % 2 == 0]
print(result)
#-----------------------------------------------------------------

with open("file1.txt") as file_1:
    list_1 = file_1.readlines()

with open("file2.txt") as file_2:
    list_2 = file_2.readlines()

result = [int(n) for n in list_1 if n in list_2]

print(result)
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# DICTIONARY COMPREHENSION PRACTICE

student_names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
students_scores = {person:random.randint(0,20) for person in student_names}
print(students_scores)

passed_students = {name:score for (name,score) in students_scores.items() if score >= 10}
print(passed_students)
#-----------------------------------------------------------------

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split(" ")}
print(result)
#-----------------------------------------------------------------

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:((temp*9/5)+32) for (day,temp) in weather_c.items()}
print(weather_f)

# ITERATE A PANDAS DATAFRAME

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
for (key, value) in student_dict.items():   #Looping through dictionaries:
    print(key)
    print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student)
    print(row.score)
#-----------------------------------------------------------------