import numpy as np
from sklearn import linear_model
height=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0],[11.0]
weight=[  8, 10 , 12, 14, 16, 18, 20,22]
reg=linear_model.LinearRegression()
reg.fit(height,weight)
X_height=[[12.0]]
print(reg.predict(X_height))
