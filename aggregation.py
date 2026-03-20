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
    print('\nCalculating Sales per Region and Time...')
    region_time_summary= df.groupby(["Region", pd.Grouper(key= "Order Date" , freq= "M")])["Sales"].sum()
    print(region_time_summary)

def getting_outliers(df):
    print("Getting Outliers...")
    q1= df["Sales"].quantile(0.25)
    q3= df["Sales"]. quantile(0.75)
    IQR= q3- q1
    outliers= df[(df["Sales"]<=(q1-(1.5*IQR)))&(df["Sales"]>=(q3+(1.5*IQR)))]
    print(outliers)

def growth_rate(df):
    print('\nCalculating Growth Rate')
    growth= df.groupby(pd.Grouper(key="Order Date", freq= "Y"))["Sales"].sum()
    growthrate= growth.pct_change()*100
    print(growthrate)