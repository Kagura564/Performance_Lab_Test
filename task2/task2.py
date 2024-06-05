#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import argparse

def readFile(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines
        

def pointCircle(pathCircle, pathPoints):
    
    lines = readFile(pathCircle)
    pointsCircle = list(map(int, lines[0].strip().split()))
    radius = int(lines[1])

    lines = readFile(pathPoints)
    points = [list(map(int, line.strip().split())) for line in lines]
    
    for point in points:
        distance = math.sqrt((point[0] - pointsCircle[0]) ** 2 + (point[1] - pointsCircle[1]) ** 2)
             
        if distance == radius:
            print(0)
        elif distance < radius:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process circle and points file.")
    parser.add_argument("circle", help="Path to the circle file")
    parser.add_argument("points", help="Path to the points file")

    args = parser.parse_args()

    pointCircle(args.circle, args.points)




