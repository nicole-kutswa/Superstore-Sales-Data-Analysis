import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def category_bar(df):

    category_summary= df.groupby("Category").agg({
        "Sales":"sum",
        "Profit":"sum",
        "Quantity":"sum",
    })
    total_sales= df["Sales"].sum()
    category_percentage= (category_summary["Sales"]/total_sales)*100
    
    print(category_summary)
    print(category_percentage)
    category= df.groupby("Category")["Sales"].sum()
    category.plot(kind="bar")
    plt.title("Total Sales By Category")
    plt.ylabel("Sales")
    plt.show()

def sales_overtime(df):
    region_time_summary= df.groupby(["Region", pd.Grouper(key= "Order Date" , freq= "M")])["Sales"].sum()
    print(region_time_summary)
    region_time_summary.plot(kind= "line")
    plt.title("Monthly Sales Trend")
    plt.ylabel("Sales")
    plt.show()