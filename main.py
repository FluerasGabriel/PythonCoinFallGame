import turtle
import random
import time
import winsound

import os


def Run():
 winsound.PlaySound('music.wav', winsound.SND_ASYNC)
 window=turtle.Screen()
 window.title("Game")
 window.setup(width=800,height=600)
 window.bgcolor("white")
 window.addshape("coin.gif")
 window.addshape("pirate.gif")
 window.bgpic("pirateBackground.gif")
 window.addshape("bomb.gif")
 window.tracer(0)




 stop=True
 # Add Player
 player=turtle.Turtle()
 player.speed(0)
 player.shape("pirate.gif")
 player.penup()
 player.goto(0 , -250)
 player.direction="stay"

 points=[]
 # Add Points
 for _ in range(10):
  point=turtle.Turtle()
  point.speed(0)
  point.shape("coin.gif")
  point.color("yellow")
  point.penup()
  randomX = random.randint(10, 350)
  point.goto(randomX,250)
  points.append(point)

 bombs=[]
  # Add Bombs
 for _ in range(5):
   bomb=turtle.Turtle()
   bomb.speed(0)
   bomb.shape("bomb.gif")
   bomb.color("red")
   bomb.penup()
   randomX = random.randint(10, 350)
   bomb.goto(randomX,250)
   bombs.append(bomb)

 scor=0
 lives=3
 # Add Score
 score=turtle.Turtle()
 score.hideturtle()
 score.speed(0)
 score.penup()
 score.goto(0,260)
 font=("Comic Sans MS", 27, "normal")
 score.write("Score: {} Lives: {}".format(scor,lives),align="center",font=font)

 def left():
    player.direction="left"
 def right():
    player.direction="right"
 def Restart():
     window.clearscreen()
     Run()
 window.listen()
 window.onkeypress(left,"a")
 window.onkeypress(right,"d")
 window.onkeypress(Restart,"x")
# Main Game Loop
 while stop:
    window.update()
    # Player move
    if player.direction=="stay":
        x=player.xcor()
        player.setx(x)
    if player.direction=="left":
        x=player.xcor()
        x-=0.8
        player.setx(x)
        #print(x)
    if player.direction=="right":
        x=player.xcor()
        x+=0.8
        player.setx(x)
        #print(x)
      # Player Max View
    if player.xcor()<-380:
        player.setx(-380)
    if player.xcor()>380:
        player.setx(380)
    # Points rain
    for point in points:
     y=point.ycor()
     y-=0.7
     point.sety(y)
     if(y<-300):
        randomX=random.randint(-380,380)
        randomY=random.randint(300,400)
        point.goto(randomX,randomY)

     # Collision
     if(point.distance(player)<30):

        randomX=random.randint(-380,380)
        randomY=random.randint(300,400)
        scor += 30
        score.clear()
        score.write("Score: {} Lives: {}".format(scor,lives),align="center",font=font)
        point.goto(randomX,randomY)
    for bomb in bombs:
        y = bomb.ycor()
        y -= 0.7
        bomb.sety(y)
        if (y < -300):
            randomX = random.randint(-380, 380)
            randomY = random.randint(300, 400)
            bomb.goto(randomX, randomY)
        if (bomb.distance(player) < 20):
            lives-=1
            score.clear()
            score.write("Score: {} Lives: {}".format(scor, lives), align="center", font=font)
            randomX = random.randint(-380, 380)
            randomY = random.randint(300, 400)
            bomb.goto(randomX, randomY)
    if (lives == 0):
        stop = False
        score.clear()
        score.write("You're score was {}".format(scor), align="center", font=font)
        time.sleep(2)
        score.clear()
        score.write("For restart press x", align="center", font=font)

 window.mainloop()
Run()
