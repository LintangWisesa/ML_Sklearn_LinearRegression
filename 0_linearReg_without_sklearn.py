import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 4, 5, 4, 6, 5, 7, 7, 8]

# create dataframe
df = pd.DataFrame({
    'x': np.array(x),
    'y': np.array(y),
    'x2': np.array(x) ** 2,
    'y2': np.array(y) ** 2,
    'xy': np.array(x) * np.array(y)
})

# sum x, sum y, sum x^2, sum y^2, sum xy
sumx = df.sum(axis=0)[0]
sumy = df.sum(axis=0)[1]
sumx2 = df.sum(axis=0)[2]
sumy2 = df.sum(axis=0)[3]
sumxy = df.sum(axis=0)[4] 
print(sumx, sumy, sumx2, sumy2, sumxy)

# slope / gradient
m = ((len(x)*sumxy)-(sumx*sumy))/((len(x)*sumx2)-(sumx**2))
print(m)

# intercept
c = ((sumy*sumx2)-(sumx*sumxy))/((len(x)*sumx2)-(sumx**2))
print(c)

# y best fit line (y = mx + c)
df['yBest'] = m * np.array(x) + c
print(df)

# predict x = 200 so y - ???
print(m*200 + c)

# plotting
plt.plot(
    df['x'], df['y'], 'g-',
    df['x'], df['yBest'], 'r-'
)
plt.grid(True)
plt.show()