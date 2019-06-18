# pip install sklearn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# ================================
# create dataframe

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
df = pd.DataFrame({
    'x': x,
    'y': y
})
print(df)

# ================================
# plot dataframe

plt.plot(df['x'], df['y'], 'r-')
plt.scatter(df['x'], df['y'], color='r', marker='o', s=50)

plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.title('Tes')
plt.show()