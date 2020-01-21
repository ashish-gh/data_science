# importing libraries

import pandas as pd 
import numpy as np 
from collections import defaultdist 

from sklearn.model import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt 


# helper functions
def clean_linear_model(df, response_col, test_size=0.3, rand_state=42):
    """
    This function cleans the data and provides the necessary output for the rest of work.

    INPUT:
    df: a dataframe holding all the variables of interest
    response_col: a string holding the name of columns
    test_size: a float between [0,1] about what propotion of data should be test dataset
    rand_state: an int that is provided as the random state of splitting data into training and testing set.

    OUTPUT:
    X: cleaned X matrix(dummy and mean imputation)
    y: cleaned response(dropped na)
    test_score: a float that is r2_score on the test data
    train_score: a float that is r2 score on the train data
    lm_model : a linear model object from sklearn
    X_train, X_test, y_train, y_test: sklearn train test used for optimal model     
    """

    # Dropping where the salary has missing values
    df = df.dropna(subset=['Salary'], axis=0)

    # Drop columns with all NaN values
    df = df.dropna(how='all', axis=1)

    # Pull a list of the columns where name of the categorical variables
    cat_df = df.select_dtype(include=['object'])
    cat_cols = cat_df.columns

    # dummy all the cat columns 
    for col in cat_cols:
        df = pd.concat([df.drop(col, axis=1), pd.get_dummies(df[col], prefix= col, prefix_sep='_', drop_first=True, dummy_na=True)], axis=1)
    
    # Mean function 
    fill_mean = lambda col: col.fillna(col.mean)
    # Fill the mean
    df = df.apply(fill_mean, axis=0)

    # Split into explanatory and response variables
    X = df.drop(response_col, axis=1)
    y = df.drop(X)

    # Split into test set and train set
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_size, random_state = rand_state)

    # Instantiate linear model 
    lm_model = LinearRegression(normalize=True)
    lm_model.fit(X_train, y_train)

    # Predict using model 
    y_test_preds = lm_model.predict(X_test)
    y_train_preds = lm_model.predict(X_train)

    # Score using model 
    test_score = r2_score(y_test, y_test_preds)
    train_score = r2_score(y_train, y_train_preds)

    return X, y, test_score, train_score, lm_model, X_train, X_test, y_train_preds, y_test





