# Inheritance:
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, Exhale")
#
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("But underwater")
#
#     def swim(self):
#         print("Move in water")
#
#
# fish = Fish()
# fish.swim()
# fish.breathe()
# print(fish.num_eyes)

# Slicing:
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# print(piano_keys[2:5]) -> c, d, e
# print(piano_keys[2:]) -> c, d, e, f, g
# print(piano_keys[:5]) -> a, b, c, d, e
# print(piano_keys[2:5:2]) ->c, e
# print(piano_keys[::2]) -> a, c, e, g
# print(piano_keys[::-1]) -> g, f, e, d, c, b, a

from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.change()

    def change(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(y=280, x=0)
        self.score = 0
        self.write(arg="Score: 0", move=False, align="center", font=('Courier', 14, 'normal'))
        self.hideturtle()

    def update(self):
        self.clear()
        self.score+=1
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Consolas', 14, 'normal'))

    def over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER!", move=False, align="center", font=('Consolas', 24, 'normal'))

