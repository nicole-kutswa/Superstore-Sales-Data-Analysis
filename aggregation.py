import pandas as pd
import numpy as np

def category(df):
    category_summary= df.groupby("Category").agg({
        "Sales":"sum",
        "Profit":"sum",
        "Quantity":"sum",
    })
    total_sales= df["Sales"].sum()
    category_percentage= (category_summary["Sales"]/total_sales)*100
    
    print(category_summary)
    print(category_percentage)

def region_time(df):
    region_time_summary= df.groupby(["Region", pd.Grouper(key= "Order Date" , freq= "M")])["Sales"].sum()
    print(region_time_summary)