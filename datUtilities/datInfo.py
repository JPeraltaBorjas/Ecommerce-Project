import pandas as pd

def infoStatistics(dataframe: pd.DataFrame):
    """Show the main statistics values of the dataset for each column"""
    statistics = {
        'Total_elements': dataframe.notnull().sum(),
        'NaN_amount': dataframe.isnull().sum(),
        'NaN_percent': (dataframe.isnull().sum() * 100) / len(dataframe),
        'Duplicated_data': [dataframe.duplicated().sum()] * len(dataframe.columns),
        'Mode': dataframe.apply(lambda x: x.mode().iloc[0] if not x.mode().empty else None),
        'Data_type': dataframe.dtypes
    }
    
    pd_statistics = pd.DataFrame(statistics)
    return pd_statistics


def infoNaN(dataframe: pd.DataFrame):
    """Indicate the amount of NaN values and NaN percent"""
    nan_info = {
        'Total_elements': dataframe.notnull().sum(),
        'NaN_amount': dataframe.isnull().sum(),
        'NaN_percent': (dataframe.isnull().sum() * 100) / len(dataframe)
    }
    pd_nan = pd.DataFrame(nan_info)
    return pd_nan