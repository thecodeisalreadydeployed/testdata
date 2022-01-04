import numpy as np
import datetime
import time

shape, scale = 36, 5/6
s = list(np.random.gamma(shape, scale, 5))

while True:
    for i in s:
        print(datetime.datetime.now())
        print(i)
        time.sleep(i)
