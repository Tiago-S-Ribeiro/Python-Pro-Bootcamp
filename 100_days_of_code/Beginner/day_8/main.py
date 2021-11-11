alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUM_CHARS = 26

#def caesar(text, shift, direction):
#  return_word = ""
#  if direction == "decode":
#    shift *= -1
#  for char in text:
#    if char not in alphabet:
#        return_word += char
#    else:
#      index_char = alphabet.index(char)
#      new_index = index_char + shift
#      return_word += alphabet[new_index]
#  print(f"The {direction}d text is {return_word}")

def caesar(text, shift, direction):
  return_word = ""
  if(direction == "encode"):
    for char in text:
      if char not in alphabet:
        return_word += char
      else:
        index_char = alphabet.index(char)
        new_index = index_char + shift
        if(new_index > NUM_CHARS):
          aux = new_index - NUM_CHARS
          return_word += alphabet[aux]
        else:
          return_word += alphabet[new_index]
    print(f"The encoded text is {return_word}")
  elif(direction == "decode"):
      for char in text:
        if char not in alphabet:
          return_word += char
        else:
          index_char = alphabet.index(char)
          new_index = index_char - shift
          if(new_index < 0):
            aux = NUM_CHARS - new_index
            return_word += alphabet[aux]
          else:
            return_word += alphabet[new_index]
      print(f"The decoded text is {return_word}")
  else:
    print("Type a valid direction")

answer = ""

while answer != "no":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(text, shift, direction)
  answer = input("Type 'yes' if you want to go again. Otherwise type'no'.\n").lower()