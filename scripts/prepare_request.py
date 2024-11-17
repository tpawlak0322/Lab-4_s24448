from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
def prepare_data_request(data_from_request):
    
    data = pd.read_csv('./dataset_asi/dataset.txt')
    data = data.append(data_from_request, ignore_index=True)

    data = pd.get_dummies(data, drop_first=True)
    
    data.fillna(data.median(), inplace=True)

    scaler = StandardScaler()
    numerical_features = data.select_dtypes(include=['float64', 'int64']).columns
    data[numerical_features] = scaler.fit_transform(data[numerical_features])

    data = data.drop('score', axis=1)
    data = data.iloc[-1:]    
    
    return data