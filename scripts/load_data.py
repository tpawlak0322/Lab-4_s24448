import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def load():
    data = pd.read_csv('dataset_asi/dataset.txt')

    print(data.info())
    print(data.describe())


    print(data.isnull().sum())

    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_cols].hist(bins=15, figsize=(15, 10), layout=(3, 3), edgecolor='black')
    plt.suptitle('Histogramy dla zmiennych liczbowych', fontsize=16)
    plt.show()

    return data



