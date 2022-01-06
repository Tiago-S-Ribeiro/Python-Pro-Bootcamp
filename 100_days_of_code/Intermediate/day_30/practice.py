#try -> dentro do try, mete-se o código que pode causar exceções
# except -> fazer isto SE houver uma exceção (equivalente ao catch do java)
# else -> faz isto SE NÃO apanhou exceções
# finally -> faz isto INDEPENDENTEMENTE se apanhou exceção ou não
#---------------------------------------------------------------------
try:
    file = open("test.txt")
    a_dict = {"key": "val"}
    value = a_dict["key"]
except FileNotFoundError:
    file = open("test.txt", "w")
    file.write("VR46")
except KeyError as error_msg:
    print(f"The key {error_msg} doesn't exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    #raise TypeError("A made up error. For no reason at all.")
#---------------------------------------------------------------------
h = float(input("Height: "))
w = int(input("Weight: "))

if h > 3:
    raise ValueError("Human height should not be > 3 meters")

bmi = w / h ** 2
print(bmi)
#---------------------------------------------------------------------
#IndexError
#f_list = ["A", "B", "C"]
#f = f_list[4]

#TypeError
#text = "cenas"
#print(text + 46)
#---------------------------------------------------------------------