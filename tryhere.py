from time import time

for i in range(0,10):
    rand = str(round(time(),7))
    rand2 = str(rand[::-1])
    print(rand2[0])