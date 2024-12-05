# What do we want to play with today?
# A. Emotions

E = ["happy",
     "sad",
     "neutral",
     "hungry",
     "horrified",
     "anxious",
     "scared",
     "joyful",
     "misc",
     "headstrong",
     "optimistic"]

# sometimes emotions are random

from random import random, choice

print(choice(E)) # see, it can be bad, but exactly how bad

# let us assign a goodness_value to each emotion
# the values maybe subjective

GV = {"happy":1,
      "neutral": 0,
      "misc": -1,
      "hungry": 1,
      "joyful":2,
      "horrified":-2,
      "anxious":-1,
      "scared":-2,
      "sad":-1,
      "headstrong":1,
      "optimistic":1}

# let us now list mood, the cumulative goodness
# it would be nice to see a plot too

import matplotlib.pyplot as plt


days = 100
gv = [0]
D = [-1]

for day in range(days):
    D.append(day)
    gv.append(gv[-1]+GV[choice(E)])
    continue

# let us see 
print(gv[-1])

plt.plot(D,gv)
plt.title("mood")
plt.xlabel("day")
plt.show()
    
