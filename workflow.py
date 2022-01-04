import numpy as np
shape, scale = 36, 5/6
s = np.random.gamma(shape, scale, 1000)
print(s)
