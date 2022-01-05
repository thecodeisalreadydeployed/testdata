import numpy as np
import datetime
import time
import subprocess

shape, scale = 36, 5/6

# TODO(trif0lium): set size to 5
s = list(np.random.gamma(shape, scale, 1))

for i in s:
    print(datetime.datetime.now())
    print(i)

    # TODO(trif0lium): change i/2 to i
    time.sleep(i/2)

    subprocess.run(["git", "config", "user.name"], capture_output=True)
