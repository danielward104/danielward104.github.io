import numpy as np

x1 = 753; y1 = 684
x2 = 578; y2 = 460
x3 = 720; y3 = 780

#x1 = 810; y1 = 626
#x2 = 960; y2 = 960
#x3 = 960; y3 = 960

x1 = 960; y1 = 960
x2 = 960; y2 = 960
x3 = 960; y3 = 960

padding = 3.5

r1 = x1/y1; r2 = x2/y2; r3 = x3/y3

y_per = (100 - padding*4)/(r1 + r2 + r3)
x1_per = r1*y_per
x2_per = r2*y_per
x3_per = r3*y_per

print(x1_per,x2_per,x3_per)
