#!/usr/bin/python
#wDist = [ 100, 200, 400, 800, 1000, 1500, 1600, 2000, 3000, 5000, 10000, 15000, 20000, 21098, 25000, 30000, 42195 ]
#wTime = [ 9.5,  19,  43, 101,  132,  206,  223,  285,  441,  757,  1604,  2473,  3321,  3503,  4345,  5233,  7377 ]
wDist = [400, 800, 1500, 5000]
wTime = [43.03, 100.91, 206,  757.35]
wSpeed = []

myDist = [ 400, 800, 1500, 5000]
myTime = [ 85.5, 206,  422, 1504]          # 15.5, 1:25, 3:26, 7:02, 25:04

def Seconds_To_MMSS(val):
    min = int(val/60)
    sec = int(val - min*60)
    string = str(min) + ":" + str(sec)
    return string

idx = 0
while (idx < len(myDist)):
    print "\nDistance: ", myDist[idx]
    ratio = myTime[idx] / wTime[idx]
    print "Ratio:", round(ratio,2)
    j = 0
    while (j < len(myDist)):
        print myDist[j], "WR :", wTime[j], "MyTime:", round(ratio * wTime[j],2), "MyTime:", Seconds_To_MMSS(ratio * wTime[j])
        j = j + 1
    idx = idx + 1
