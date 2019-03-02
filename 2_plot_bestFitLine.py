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
# linear regression

from sklearn import linear_model
model = linear_model.LinearRegression()

# training w/ dataset: mode.fit(dataIndependent[2D], dataDependent[1D])
model.fit(df[['x']], df['y'])

# show m(gradient/slope) & b(intercept) of 'best fit line'
print('Slope = ', model.coef_)
print('Intercept = ', model.intercept_)

# prediction
print(model.predict([[8]]))

# ================================

# plot dataframe
plt.plot(df['x'], df['y'], 'r-')

# plot best fit line
plt.plot(df['x'], model.predict(df[['x']]), 'g-')

# scatter dataframe
plt.scatter(df['x'], df['y'], color='r', marker='o', s=50)

# scatter best fit line
plt.scatter(df['x'], model.predict(df[['x']]), color='g', marker='o', s=50)

plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.title('Linear Regression')
plt.legend(['Dataset', 'Best Fit Line'])
plt.show()

