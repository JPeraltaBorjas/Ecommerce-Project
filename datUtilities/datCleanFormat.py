import pandas as pd

def cleanPercentNaN(dataframe: pd.DataFrame, percent:float):
    """Removes variables from the dataset according to the minimum percentage of null values 
    ​​it contains, this given by analyst"""

    percentNaN = (dataframe.isnull().sum() * 100) / len(dataframe)
    list_remove = percentNaN[percentNaN >= percent].index
    list_remove = list(list_remove)
    pd_removed = dataframe.drop(columns = list_remove)

    return pd_removed
