import pandas
import turtle

def place_text(x, y, text):
  t = turtle.Turtle()
  t.penup()
  t.hideturtle()
  t.goto(x,y)
  t.write(arg=text, align="left", font=("Courier", 8, "normal"))

def export_csv(guessed, all_states):
  for state in guessed:
    all_states.remove(state)
  pandas.DataFrame(all_states).to_csv("missed_states.csv")

screen = turtle.Screen()
screen.title("US States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
  user_answer = screen.textinput(title = f"{len(guessed_states)}/50", prompt="Guess a state.").lower().title()
  
  if user_answer in states_list and user_answer not in guessed_states:
    #data[data.state == user_answer]["x"] -> want the x value on the row where data.state equals the user answer
    place_text(int(data[data.state == user_answer]["x"]), int(data[data.state == user_answer]["y"]), user_answer)
    guessed_states.append(user_answer)
  elif user_answer == "Exit":
    export_csv(guessed_states, states_list)
    break