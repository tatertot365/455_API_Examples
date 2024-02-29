import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

import onnx
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType, Int32TensorType

df = pd.read_csv('/Users/tategillespie/Desktop/455 TA/Flask Example/MLR_Model/insurance.csv')
df = df.select_dtypes(include=np.number)

X = df.drop('charges', axis=1)
y = df['charges']

model = LinearRegression()
model.fit(X, y)

print(df.columns)

with open('/Users/tategillespie/Desktop/455 TA/Flask Example/MLR_Model/sample_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

initial_type = [('float_input', FloatTensorType([None, 3]))]
onnx_model = convert_sklearn(model, initial_types=initial_type) 

with open('/Users/tategillespie/Desktop/455 TA/Flask Example/MLR_Model/sample_model.onnx', 'wb') as onnx_file:
    onnx_file.write(onnx_model.SerializeToString())
