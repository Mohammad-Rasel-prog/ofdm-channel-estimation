import numpy as np

rng = np.random.default_rng(0)   # random-number machine; 0 = same "random" numbers every time

h = 0.8                      # the TRUE channel: this lane shrinks the signal to 80%
noise = 0.1 * rng.normal()   # a little random hiss
z = h + noise                # what we measure after sending the pilot "1"

print("true channel h:", h)
print("measured z:    ", round(z, 3))
print("our mistake:   ", round(z - h, 3))