import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def category_bar(df):
    fig, (ax1, ax2)= plt.subplots(1, 2, figsize=(14, 5))
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
    category.plot(kind="bar", ax= ax1)
    plt.title("Total Sales By Category")
    plt.ylabel("Sales")

    market_share= df.groupby(["Category"])["Sales"].sum()
    market_share.plot(kind="pie", autopct= "%1.1f%%")
    plt.title("Sales Share by Category")
    plt.ylabel("")
    fig.savefig("plot.png", dpi= 300, bbox_inches= "tight")
    plt.tight_layout
    plt.show()

def sales_overtime(df):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize= (14,5))
    regions= df.groupby(["Region"])["Sales"].sum()
    regions.plot(kind= "bar", ax= ax1)
    plt.title("Sales By Regions")
    plt.xlabel("Regions")
    
    region_time_summary= df.groupby(["Region", pd.Grouper(key= "Order Date" , freq= "M")])["Sales"].sum().unstack("Region")
    #print(region_time_summary)
    region_time_summary.plot(kind= "line", ax= ax2)
    plt.title("Monthly Sales Trend")
    plt.ylabel("Sales")
    plt.xticks(rotation= 45)
    fig.savefig("plot1.png", dpi= 300, bbox_inches= "tight")

    plt.tight_layout
    plt.show()

def top_products(df):
    fig, (ax1, ax2)= plt.subplots(1, 2, figsize=(14, 5))

    sub_category= df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending = False)
    sub_category.plot(kind= "barh", ax= ax1)
    plt.title("Top Sub-Categories")
    plt.xlabel("Sales")

    df["Sales"].plot(kind= "hist", bins= 30, ax= ax2)
    plt.title("Sales Distribution")
    fig.savefig("plot2.png", dpi= 300, bbox_inches= "tight")

    plt.tight_layout
    plt.show()

def profit_sales(df):

    fig, (ax1, ax2)= plt.subplots(1, 2, figsize= (14, 5))

    res = df.groupby(["Region", pd.Grouper(key="Order Date", freq="M")])["Sales"].sum().reset_index()
    res["Order Date"] = res["Order Date"].dt.strftime('%b-%Y')
    heatmap_data = res.pivot(index="Region", columns="Order Date", values="Sales")

    sns.heatmap(heatmap_data, annot=True, fmt=".0f", ax=ax1, cmap="YlGnBu")
    ax1.set_title("Sales Heatmap by Region and Month")

    ax2.scatter(df["Profit"], df["Sales"])
    ax2.set_title("Relationship of profits and Sales")
    ax2.set_xlabel("Profit")
    ax2.set_ylabel("Sales")
    fig.savefig("plot3.png", dpi= 300, bbox_inches= "tight")

    plt.tight_layout
    plt.show()



    