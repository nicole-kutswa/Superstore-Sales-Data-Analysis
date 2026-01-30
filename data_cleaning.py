import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def clean_data(df):
    print('Missing values:\n', df.isnull().sum())
    print('Duplicate values:\n', df.duplicated().sum())

    # Date formatting
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

    print('\nColumn Date Info:')
    print(df[['Order Date', 'Ship Date']].info())

    #profit margin
    df['Profit Margin']= df['Profit']/ df['Sales']
    print(df[['Sales', 'Profit', 'Profit Margin']])

    #Order Processing Time
    df['Order Processing Time'] = (df['Ship Date'] - df['Order Date']).dt.days
    print(f"Negative order processing times {(df['Order Processing Time']<0).sum()}")
    
    return df
