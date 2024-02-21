import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('/Users/tategillespie/Desktop/455 TA/Flask Example/MLR_Model/insurance.csv')
df = df.select_dtypes(include=np.number)

X = df.drop('charges', axis=1)
y = df['charges']

model = LinearRegression()
model.fit(X, y)

print(df.columns)

with open('/Users/tategillespie/Desktop/455 TA/Flask Example/Backend/sample_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

