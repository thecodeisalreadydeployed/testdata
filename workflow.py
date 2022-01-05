import numpy as np
import datetime
import time
import subprocess

shape, scale = 36, 5/6

# TODO(trif0lium): set size to 5
s = list(np.random.gamma(shape, scale, 2))

for i in s:
    print(datetime.datetime.now())
    print(i)

    # TODO(trif0lium): change i/2 to i
    time.sleep(i * 60 /2)

    process = subprocess.run(["/bin/sh", "run.sh"], capture_output=True)
    print(process.stdout)
