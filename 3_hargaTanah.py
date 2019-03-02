# pip install sklearn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# ================================
# create dataframe

df = pd.read_csv('3_hargaTanah.csv')
print(df)

# ================================
# linear regression

from sklearn import linear_model
model = linear_model.LinearRegression()

# training w/ dataset: mode.fit(dataIndependent[2D], dataDependent[1D])
model.fit(df[['luas']], df['harga'])

# show m(gradient/slope) & b(intercept) of 'best fit line'
print('Slope = ', model.coef_)
print('Intercept = ', model.intercept_)

# ================================

# # plot dataframe
plt.plot(df['luas'], df['harga'], 'r-')

# # plot best fit line
plt.plot(df['luas'], model.predict(df[['luas']]), 'g-')

# scatter dataframe
plt.scatter(df['luas'], df['harga'], color='r', marker='o', s=50)

# scatter best fit line
plt.scatter(df['luas'], model.predict(df[['luas']]), color='g', marker='*', s=50)

plt.legend(['Dataset', 'Best Fit Line'])
plt.xlabel('Luas Tanah (ha)')
plt.ylabel('Harga Tanah (Rp)')
plt.title('Harga Tanah')
plt.show()

# =========================

# prediction harga tanah saya
tanahSaya = {
    'luas': [500, 1234, 4200, 2345]
}
dfTanahSaya = pd.DataFrame(tanahSaya)

print(model.predict(dfTanahSaya))
print(model.predict(dfTanahSaya[['luas']]))

# accuracy:
print(model.score(df[['luas']], df['harga']))