import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

def getData():
    return pd.read_csv('G:/_DATA/data.csv')

def getPreData():
    return pd.read_csv('G:/_DATA/cleandata.csv')

def getTestData():
    return "How many cities in USA?"

