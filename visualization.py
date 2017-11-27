#This is for playing with seaborn API

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matchparsing

match_id = [3142390443, 3144097046, 3144175535, 3142994571]


#demo visualization for radiant gold advantage
data = matchparsing.goldadv(3142390443)
plt.plot(data)
plt.ylabel('radiant gold advantage')
plt.xlabel('minutes')
plt.show()

#visualization discussion
