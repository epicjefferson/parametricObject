import rhinoscriptsyntax as rs
import random

pointList = []
ypointList = []

temp = open("sample.txt", "r")
for line in temp:
    ypointList.append(line)
temp.close()

for i in range(40):
    Y = ypointList[i]
    pt = (i, Y, 0)
    
    pointList.append(pt)
    
curve = rs.AddPolyline(pointList)
rs.AddRevSrf( curve, ((0,0,0), (40,0,0)))
