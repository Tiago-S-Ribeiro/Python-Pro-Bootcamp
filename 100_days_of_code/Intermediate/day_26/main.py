import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

input_invalid = True
user_input = input("Insert a string:\n")

while input_invalid:
  try:
    codes = [phonetic_dict[letter.upper()] for letter in user_input]
    input_invalid = False
  except KeyError:
    print("Only strings allowed.\n")
    user_input = input("Insert a string:\n")
  else:
    print(codes)