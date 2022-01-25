import bs4

with open("/Users/tiago.soaresribeiro/Documents/Personal_Docs/Python-Pro-Bootcamp/100_days_of_code/Intermediate+/day_45/website.html") as file:
    contents = file.read()


soup = bs4.BeautifulSoup(contents, "html.parser")

#print(soup.a)
#print(soup.a.string) imprime o conteudo da primeira anchor tag que encontrar

all_a_tags = soup.find_all(name="a")

for tag in all_a_tags:
    #print(tag.getText())   #imprime o conteudo da anchor tag
    print(tag.get("href"))  #imprime o conteudo do atributo 'href' de cada anchor tag

heading = soup.find(name="h1", id="name")
#heading = soup.find("h1")  isto ia encontrar o primeiro 'h1'
print(heading.string)

section_head = soup.find(name="h3", class_="heading")
print(section_head.get("class"))
print(section_head.getText())
print(section_head.string)

isep_url = soup.select_one(selector="p strong a") #encontra a primeira 'a' tag, dentro de 'strong', dentro de 'p'
print(isep_url.get("href"))

my_name = soup.select_one(selector="#name")     #encontra um elemento com o id 'name'
print(my_name.string)

heads = soup.select(".heading")  #lista de elementos com class 'heading'
print(heads)
