import pandas
from sklearn import linear_model

df = pandas.DataFrame({
    'Weight': [1500, 1600, 1700, 1800],
    'Volume': [1000, 1100, 1200, 1300],
    'CO2': [120, 130, 140, 150]})

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

#https://matplotlib.org/stable/plot_types/3D/surface3d_simple.html