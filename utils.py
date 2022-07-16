#Imports
# Data structures
import pandas as pd
# Sampling
from imblearn.over_sampling import RandomOverSampler
# Preprocessing
from sklearn.model_selection import train_test_split

# data set is avialable at: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

class DataHandler():
    def __init__(self):
        self.data = None
    
    def load_data(self, path):
        self.data = pd.read_csv(path)
        
    def preprocess(self):
        # drop id because it is not relevant for the prediction
       self.data.drop(['id'], axis=1, inplace=True)
       # drop rows with NaN
       self.data.dropna(inplace = True)

    # create dummies for categorical variables
    def get_dummies(self):
        self.data = pd.get_dummies(self.data)

    # split data into train and test set with test size of 0.3
    def split_data(self):
        y = self.data['stroke']
        X = self.data.drop(['stroke'], axis=1)
        
        return train_test_split(X, y, test_size=0.3,random_state=42)

    # Oversample the data since the data is imbalanced
    def oversample(self, X_train, y_train):
        ros = RandomOverSampler(random_state=42)
        X_train_resample, y_train_resample = ros.fit_resample(X_train, y_train)

        return X_train_resample, y_train_resample

