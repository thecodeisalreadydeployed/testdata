import numpy as np
import datetime
import time
import subprocess

shape, scale = 36, 5/6

s = list(np.random.gamma(shape, scale, 5))

for i in s:
    print(datetime.datetime.now())
    print(i)

    time.sleep(i * 60)

    process = subprocess.run(["/bin/sh", "run.sh"], capture_output=True)
    print(process.stdout)
