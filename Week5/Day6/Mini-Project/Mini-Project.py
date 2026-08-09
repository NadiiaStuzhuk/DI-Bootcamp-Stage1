# Mini-Project : Data Analysis for Marketing Strategy


# Introduction
# In this mini-project, we will perform data analysis to devise a marketing strategy based on various aspects like area analysis, customer analysis, product category analysis, and sales and profit time series.



# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# How to load and preprocess a dataset.
# Techniques for area analysis to identify key markets.
# Methods for customer analysis to determine high-value customers.
# Strategies for product category analysis to identify top-performing products.
# How to analyze sales and profit trends over time.
# Application of the Pareto Principle to prioritize key drivers of sales and profit.


# Dataset
# The US Superstore Dataset contains the following attributes:

# Row ID: Unique ID for each row.
# Order ID: Unique Order ID for each Customer.
# Order Date: Order Date of the product.
# Ship Date: Shipping Date of the Product.
# Ship Mode: Shipping Mode specified by the Customer.
# Customer ID: Unique ID to identify each Customer.
# Customer Name: Name of the Customer.
# Segment: The segment where the Customer belongs.
# Country: Country of residence of the Customer.
# City: City of residence of the Customer.
# State: State of residence of the Customer.
# Postal Code: Postal Code of every Customer.
# Region: Region where the Customer belongs.
# Product ID: Unique ID of the Product.
# Category: Category of the product ordered.
# Sub-Category: Sub-Category of the product ordered.
# Product Name: Name of the Product.
# Sales: Sales of the Product.
# Quantity: Quantity of the Product.
# Discount: Discount provided.
# Profit: Profit/Loss incurred.


# Task
# First load the dataset in a notebook and preprocess it. Then use visualisations to address the following questions:

# Which states have the most sales?
# What is the difference between New York and California in terms of sales and profit? (Compare the total sales and profit between New York and California.)
# Who is an outstanding customer in New York?
# Are there any differences among states in profitability?
# The Pareto Principle, also known as the 80/20 rule, is a concept derived from the work of Italian economist Vilfredo Pareto. It states that roughly 80% of the effects come from 20% of the causes. For instance, identifying the top 20% of products that generate 80% of sales or the top 20% of customers that contribute to 80% of profit can help in prioritizing efforts and resources. This focus can lead to improved efficiency and effectiveness in business strategies. Can we apply Pareto principle to customers and Profit ? (Determine if 20% of the customers contribute to 80% of the profit.)
# What are the Top 20 cities by Sales ? What about the Top 20 cities by Profit ? Are there any difference among cities in profitability ? (Identify the top 20 cities based on total sales and total profit and analyze differences in profitability among these cities.)
# What are the Top 20 customers by Sales?
# Plot the Cumulative curve in Sales by Customers. Can we apply Pareto principle to customers and Sales ?
# Based on the analysis, make decisions on which states and cities to prioritize for marketing strategies.


import pandas as pd
import numpy as np


filepath = 'US Superstore data.xls'
xls = pd.ExcelFile(filepath)
print("Sheet names:", xls.sheet_names)

df = pd.read_excel(filepath)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head(2))

import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")


state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
state_profit = df.groupby('State')['Profit'].sum()
state_summary = pd.DataFrame({'Sales': state_sales, 'Profit': state_profit, 'Profit Margin (%)': (state_profit/state_sales)*100}).sort_values(by='Sales', ascending=False)

print("--- Top 10 States by Sales ---")
print(state_summary.head(10))

print("\n--- Bottom 5 States by Profit ---")
print(state_summary.sort_values(by='Profit').head(5))


ny_ca = state_summary.loc[['California', 'New York']]
print("\n--- NY vs CA Comparison ---")
print(ny_ca)


ny_df = df[df['State'] == 'New York']
ny_cust = ny_df.groupby(['Customer ID', 'Customer Name'])[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
print("\n--- Top Customers in New York by Sales ---")
print(ny_cust.head(5))
ny_cust_profit = ny_df.groupby(['Customer ID', 'Customer Name'])[['Sales', 'Profit']].sum().sort_values(by='Profit', ascending=False)
print("\n--- Top Customers in New York by Profit ---")
print(ny_cust_profit.head(5))


total_states = len(state_summary)
unprofitable_states = state_summary[state_summary['Profit'] < 0]
print(f"\nNumber of loss-making states: {len(unprofitable_states)} out of {total_states}")
print("Unprofitable states:\n", unprofitable_states)


cust_profit = df.groupby('Customer ID')['Profit'].sum().sort_values(ascending=False)
total_cust = len(cust_profit)
top_20_percent_cust_count = int(np.ceil(0.20 * total_cust))

total_overall_profit = cust_profit.sum()


top_20_cust_profit = cust_profit.head(top_20_percent_cust_count).sum()
pct_profit_top_20 = (top_20_cust_profit / total_overall_profit) * 100

print(f"\n--- Pareto Check: Customers & Profit ---")
print(f"Total Unique Customers: {total_cust}")
print(f"Top 20% Customers Count: {top_20_percent_cust_count}")
print(f"Total Overall Profit: ${total_overall_profit:,.2f}")
print(f"Profit from Top 20% Customers: ${top_20_cust_profit:,.2f}")
print(f"Percentage of Total Profit from Top 20% Customers: {pct_profit_top_20:.2f}%")


pos_cust_profit = cust_profit[cust_profit > 0]
top_20_pos_cust_count = int(np.ceil(0.20 * len(pos_cust_profit)))
top_20_pos_profit = pos_cust_profit.head(top_20_pos_cust_count).sum()
pct_pos_profit = (top_20_pos_profit / pos_cust_profit.sum()) * 100
print(f"Percentage of Positive Profit from Top 20% Profitable Customers: {pct_pos_profit:.2f}%")


city_summary = df.groupby('City')[['Sales', 'Profit']].sum()
city_summary['Profit Margin (%)'] = (city_summary['Profit'] / city_summary['Sales']) * 100

top_20_cities_sales = city_summary.sort_values(by='Sales', ascending=False).head(20)
top_20_cities_profit = city_summary.sort_values(by='Profit', ascending=False).head(20)

print("\n--- Top 5 Cities by Sales ---")
print(top_20_cities_sales.head(5))

print("\n--- Top 5 Cities by Profit ---")
print(top_20_cities_profit.head(5))


bottom_cities_profit = city_summary.sort_values(by='Profit').head(10)
print("\n--- Bottom 5 Cities by Profit (Worst losses) ---")
print(bottom_cities_profit.head(5))


cust_sales = df.groupby(['Customer ID', 'Customer Name'])[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
top_20_cust_sales = cust_sales.head(20)

print("\n--- Top 20 Customers by Sales ---")
print(top_20_cust_sales)


cust_sales_only = df.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False)
total_sales_all = cust_sales_only.sum()
top_20_cust_sales_sum = cust_sales_only.head(top_20_percent_cust_count).sum()
pct_sales_top_20 = (top_20_cust_sales_sum / total_sales_all) * 100

print(f"\n--- Pareto Check: Customers & Sales ---")
print(f"Total Overall Sales: ${total_sales_all:,.2f}")
print(f"Sales from Top 20% Customers: ${top_20_cust_sales_sum:,.2f}")
print(f"Percentage of Total Sales from Top 20% Customers: {pct_sales_top_20:.2f}%")


top_20_cities_sales_list = city_summary.sort_values(by='Sales', ascending=False).head(20)[['Sales', 'Profit', 'Profit Margin (%)']]
top_20_cities_profit_list = city_summary.sort_values(by='Profit', ascending=False).head(20)[['Sales', 'Profit', 'Profit Margin (%)']]

print("=== TOP 20 CITIES BY SALES ===")
print(top_20_cities_sales_list)

print("\n=== TOP 20 CITIES BY PROFIT ===")
print(top_20_cities_profit_list)


sales_cities_set = set(top_20_cities_sales_list.index)
profit_cities_set = set(top_20_cities_profit_list.index)

print("\nCities in Top 20 Sales but NOT in Top 20 Profit:")
print(sales_cities_set - profit_cities_set)

print("\nCities in Top 20 Profit but NOT in Top 20 Sales:")
print(profit_cities_set - sales_cities_set)

import matplotlib.pyplot as plt


cust_sales_sorted = df.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False).reset_index()
cust_sales_sorted['Cumulative Sales'] = cust_sales_sorted['Sales'].cumsum()
cust_sales_sorted['Cumulative Sales %'] = (cust_sales_sorted['Cumulative Sales'] / cust_sales_sorted['Sales'].sum()) * 100
cust_sales_sorted['Customer Rank %'] = ((cust_sales_sorted.index + 1) / len(cust_sales_sorted)) * 100


cust_profit_sorted = df.groupby('Customer ID')['Profit'].sum().sort_values(ascending=False).reset_index()
cust_profit_sorted['Cumulative Profit'] = cust_profit_sorted['Profit'].cumsum()
cust_profit_sorted['Cumulative Profit %'] = (cust_profit_sorted['Cumulative Profit'] / cust_profit_sorted['Profit'].sum()) * 100
cust_profit_sorted['Customer Rank %'] = ((cust_profit_sorted.index + 1) / len(cust_profit_sorted)) * 100

fig, axes = plt.subplots(1, 2, figsize=(14, 5))


axes[0].plot(cust_sales_sorted['Customer Rank %'], cust_sales_sorted['Cumulative Sales %'], color='blue', linewidth=2)
axes[0].axvline(x=20, color='red', linestyle='--', label='20% Customers')
sales_at_20 = cust_sales_sorted.loc[int(0.2*len(cust_sales_sorted)), 'Cumulative Sales %']
axes[0].axhline(y=sales_at_20, color='green', linestyle='--', label=f'{sales_at_20:.1f}% Sales')
axes[0].set_title('Cumulative Sales by Customer % (Pareto Analysis)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('% of Customers')
axes[0].set_ylabel('% of Cumulative Sales')
axes[0].legend()
axes[0].grid(True)


axes[1].plot(cust_profit_sorted['Customer Rank %'], cust_profit_sorted['Cumulative Profit %'], color='purple', linewidth=2)
axes[1].axvline(x=20, color='red', linestyle='--', label='20% Customers')
profit_at_20 = cust_profit_sorted.loc[int(0.2*len(cust_profit_sorted)), 'Cumulative Profit %']
axes[1].axhline(y=profit_at_20, color='green', linestyle='--', label=f'{profit_at_20:.1f}% Profit')
axes[1].set_title('Cumulative Profit by Customer % (Pareto Analysis)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('% of Customers')
axes[1].set_ylabel('% of Cumulative Profit')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('pareto_curves.png')
plt.show()

print(f"Sales contributed by top 20% customers: {sales_at_20:.2f}%")
print(f"Profit contributed by top 20% customers: {profit_at_20:.2f}%")

print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
print("Total Orders:", df['Order ID'].nunique())
print("Total Rows:", len(df))

print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
print("Total Orders:", df['Order ID'].nunique())
print("Total Rows:", len(df))