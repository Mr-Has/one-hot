import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

dataset = pd.read_csv('research.csv')
X = dataset.iloc[:, :].values
Y = pd.DataFrame(X)

labelencoder_X = LabelEncoder()
X[:,1]= labelencoder_X.fit_transform(X[:,1])
Y = pd.DataFrame(X)
