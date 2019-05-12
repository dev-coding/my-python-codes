#!/usr/bin/python
#coding:utf-8
import random
mini = int(input("Please input mini value: "))
max = int(input("Please input max value: "))
answer = random.randint(mini,max)
while 1:
    value = int(input("Please input value: "))
    if value > answer :
        print("Is too big")
    if value < answer :
        print("Is too small")
    if value == answer :
        print("Bingo! You win!")
        break