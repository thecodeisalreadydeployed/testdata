import numpy as np
import datetime

shape, scale = 36, 5/6
s = np.random.gamma(shape, scale, 1000)

while True:
    for i in s:
        print(datetime.datetime.now())
        print(s)
        sleep(s)
