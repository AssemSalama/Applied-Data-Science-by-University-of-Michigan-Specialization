import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.colors import TwoSlopeNorm
import seaborn as sns

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

#%% User value and colors
y_val = 40000
norm = TwoSlopeNorm(vmin=df.T.mean().min(), vcenter=y_val, vmax=df.T.mean().max())
red_green_pal = sns.diverging_palette(240, 10, n=9, as_cmap=True)
colors = [red_green_pal(norm(c)) for c in df.T.mean()]

#%% Data manipulation
plt.figure(figsize=(14,8))
sns.set(font_scale=2) 
sns.set_style("white",{'axes.grid' : False})
ax = sns.barplot(data=df.T, estimator=np.mean, capsize=0.2,
        palette=colors)
sns.despine(left=True, bottom=True)

plt.axhline(y=y_val,linewidth=1, color='k')

plt.show()

