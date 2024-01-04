import random
from turtle import Screen, Turtle

sc = Screen()
sc.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
players = []
y = -125
steps = [5, 10, 15]

for _ in colors:
  tim = Turtle(shape="turtle")
  tim.color(_)
  tim.name = {"name": _}
  tim.penup()
  tim.goto(x=-230, y=y)
  players.append(tim)
  y += 50

user_bet = sc.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
  notend = True

while notend:
  for player in players:
    # player.forward(random.choice(steps))
    player.forward(random.randint(1, 10))
    if player.xcor() > 200:
      notend = False
      if player.name["name"] == user_bet.lower():
        print(f"Congratulations {player.name['name']} wins :)")
      else:
        print(
            f"Hard Luck {user_bet.lower()} lost :( , {player.name['name']} wins"
        )

sc.exitonclick()

# print(list(range(2,0,-1)))
