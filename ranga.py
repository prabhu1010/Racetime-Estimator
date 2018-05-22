#!/usr/bin/python
#wDist = [ 100, 200, 400, 800, 1000, 1500, 1600, 2000, 3000, 5000, 10000, 15000, 20000, 21098, 25000, 30000, 42195 ]
#wTime = [ 9.5,  19,  43, 101,  132,  206,  223,  285,  441,  757,  1604,  2473,  3321,  3503,  4345,  5233,  7377 ]
wDist = [ 100, 400, 800, 1500, 5000, 10000, 15000, 20000, 21098, 25000, 30000, 42195 ]
wTime = [ 9.5, 43, 101,  206,  757,  1604,  2473,  3321,  3503,  4345,  5233,  7377 ]
wSpeed = []

mDist = [ 100, 400, 800, 1500, 5000, 10000]
mTime = [ 15.5, 85, 206,  422, 1504, 3254]

def MMSS(val):
    min = int(val/60)
    sec = int(val - min*60)
    string = str(min) + ":" + str(sec)
    return string

i = 0
while (i < len(wDist)):
    s = float(wDist[i]) / wTime[i]
    s = round(s,2) 
    wSpeed.append(s)
    i = i + 1
print wSpeed

mSpeed= []
idx = 0
while (idx < len(mDist)):
    print mDist[idx]
    msp = float(mDist[idx]) / mTime[idx]
    msp = round(msp, 2) 
    mSpeed.append(msp)

    ratio = wSpeed[idx] / mSpeed[idx]
    j = 0
    while (j < len(mDist)):
        print mDist[j], wTime[j], round(ratio,2), round(ratio * wTime[j],2), MMSS(ratio * wTime[j])
        j = j + 1
    
    idx = idx + 1

