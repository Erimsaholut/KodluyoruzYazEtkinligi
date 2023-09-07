import random

red_balls = ["red"] * 5
green_balls = ["green"] * 4
blue_balls = ["blue"] * 3

balls = red_balls + green_balls + blue_balls

same = 0
for i in range(100):
    if random.choice(balls) == random.choice(balls):
        same += 1

print(same)
