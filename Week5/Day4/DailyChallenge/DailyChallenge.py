# Daily Challenge: Strategic Analysis of Superstore Performance


# 👩‍🏫 👩🏿‍🏫 What You’ll Learn
# How to translate business objectives into actionable data analysis questions.
# How to use Matplotlib and Seaborn for diagnostic and communicative visualizations.
# How to create interactive widgets for dynamic data exploration.
# How to derive and present actionable insights from retail sales data.
# How to structure a professional analysis notebook and executive summary.


# 🛠️ What You Will Create
# You’ll build a complete business intelligence report in a Jupyter Notebook using the US Superstore dataset. This will include interactive visualizations, deep-dive diagnostics, and strategic recommendations that simulate the role of a data analyst for a national retailer.



# What Will You Use
# Concepts: diagnostic analysis, exploratory vs. explanatory visualizations, profit margin, strategic KPIs
# Libraries: Pandas, Matplotlib, Seaborn, ipywidgets
# Techniques: time-series analysis, geographic analysis, discount strategy diagnostics, interactive dashboards


# Your Task
# 1. Data Scoping and Preparation

# Download and load the US Superstore dataset. Begin with a preliminary data assessment:

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import ipywidgets as widgets
# from ipywidgets import interact, Dropdown, IntSlider
# from IPython.display import display
# import warnings
# warnings.filterwarnings('ignore')

# # Load the dataset
# df = pd.read_csv('superstore_dataset.csv')

# # Basic data exploration
# print("Dataset Shape:", df.shape)
# print("\nColumn Names:")
# print(df.columns.tolist())

# df.info()
# df.describe()
# df.isnull().sum()


# Clean and preprocess your data:

# 🧹 Handle missing values and duplicates
# Use appropriate methods (dropna(), fillna(), or imputation) and justify your choices for each case in markdown cells.

# # Check for duplicates
# print("Duplicate rows:", df.duplicated().sum())

# # Remove duplicates if any
# df = df.drop_duplicates()

# # Handle missing values (example approach)
# print("\nMissing values per column:")
# print(df.isnull().sum())

# # Example: Fill missing postal codes with 0 or remove rows
# if 'Postal Code' in df.columns:
#     df['Postal Code'] = df['Postal Code'].fillna(0)


# 🕓 Fix data types
# Ensure that date columns are converted to datetime objects using pd.to_datetime() for time-series analysis.

# # Convert date columns to datetime
# date_columns = ['Order Date', 'Ship Date']
# for col in date_columns:
#     if col in df.columns:
#         df[col] = pd.to_datetime(df[col])

# # Verify the conversion
# print("Data types after conversion:")
# print(df[date_columns].dtypes)


# 🏗️ Feature engineering
# Create new features to enrich your analysis:
# Profit Margin = (Profit / Sales) * 100
# Order Year (e.g., df['Order Date'].dt.year)
# Order Month (e.g., df['Order Date'].dt.month)


# # Feature engineering
# df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100
# df['Order Year'] = df['Order Date'].dt.year
# df['Order Month'] = df['Order Date'].dt.month
# df['Order Month-Year'] = df['Order Date'].dt.to_period('M')

# # Display sample of new features
# print("New features created:")
# print(df[['Sales', 'Profit', 'Profit Margin', 'Order Year', 'Order Month']].head())


# 2. Deep-Dive Exploratory Analysis (Matplotlib)

# 📈 Time-Series Trend Analysis
# Create a line plot of total monthly Sales across all years using Matplotlib.
# Add interactivity with ipywidgets.Dropdown to select a Product Category, dynamically updating the chart.

# 🔎 Look for patterns: seasonality, year-over-year changes, product-specific trends.

# # Prepare data for time series analysis
# monthly_sales = df.groupby(['Order Month-Year', 'Category'])['Sales'].sum().reset_index()
# monthly_sales['Date'] = monthly_sales['Order Month-Year'].dt.to_timestamp()

# # Interactive time series plot
# def plot_monthly_sales(category='All'):
#     plt.figure(figsize=(12, 6))

#     if category == 'All':
#         # Plot total sales across all categories
#         total_monthly = df.groupby('Order Month-Year')['Sales'].sum()
#         plt.plot(total_monthly.index.to_timestamp(), total_monthly.values, 
#                 marker='o', linewidth=2, markersize=4)
#         plt.title('Monthly Sales Trend - All Categories', fontsize=16, fontweight='bold')
#     else:
#         # Plot sales for specific category
#         category_data = monthly_sales[monthly_sales['Category'] == category]
#         plt.plot(category_data['Date'], category_data['Sales'], 
#                 marker='o', linewidth=2, markersize=4)
#         plt.title(f'Monthly Sales Trend - {category}', fontsize=16, fontweight='bold')

#     plt.xlabel('Date', fontsize=12)
#     plt.ylabel('Sales ($)', fontsize=12)
#     plt.xticks(rotation=45)
#     plt.grid(True, alpha=0.3)
#     plt.tight_layout()
#     plt.show()

# # Create interactive widget
# categories = ['All'] + list(df['Category'].unique())
# category_dropdown = Dropdown(options=categories, value='All', description='Category:')
# interact(plot_monthly_sales, category=category_dropdown);


# 🗺️ Geographic Sales Performance
# Build a horizontal bar chart showing total sales by State, sorted by amount.
# Add a Top N slider widget to dynamically filter the number of displayed states.

# 💬 Identify high-performing states. Are sales centralized or geographically distributed?

# # Prepare geographic sales data
# state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=True)

# # Interactive geographic analysis
# def plot_top_states(top_n=10):
#     plt.figure(figsize=(12, max(6, top_n * 0.4)))

#     # Get top N states
#     top_states = state_sales.tail(top_n)

#     # Create horizontal bar chart
#     bars = plt.barh(range(len(top_states)), top_states.values, color='steelblue')
#     plt.yticks(range(len(top_states)), top_states.index)
#     plt.xlabel('Total Sales ($)', fontsize=12)
#     plt.ylabel('State', fontsize=12)
#     plt.title(f'Top {top_n} States by Sales Performance', fontsize=16, fontweight='bold')

#     # Add value labels on bars
#     for i, (state, value) in enumerate(top_states.items()):
#         plt.text(value + max(top_states.values()) * 0.01, i, f'${value:,.0f}', 
#                 va='center', fontsize=10)

#     plt.grid(axis='x', alpha=0.3)
#     plt.tight_layout()
#     plt.show()

#     print(f"Total states analyzed: {len(state_sales)}")
#     print(f"Top {top_n} states represent: ${top_states.sum():,.0f} in sales")

# # Create interactive slider
# top_n_slider = IntSlider(min=5, max=25, value=10, description='Top N States:')
# interact(plot_top_states, top_n=top_n_slider);


# 3. Communicating Insights (Seaborn)

# 🏆 Top 10 Most Profitable Products
# Use Seaborn’s barplot() to show the top 10 products by total profit.
# - Orient horizontally, label axes clearly, and annotate bars with exact profit values.
# - Give the chart a descriptive title suitable for an executive summary.

# # Analyze top profitable products
# product_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)

# plt.figure(figsize=(12, 8))
# ax = sns.barplot(x=product_profit.values, y=product_profit.index, 
#                 palette='viridis', orient='h')

# # Customize the plot
# plt.title('Top 10 Most Profitable Products\nExecutive Summary - Product Performance Analysis', 
#           fontsize=16, fontweight='bold', pad=20)
# plt.xlabel('Total Profit ($)', fontsize=12, fontweight='bold')
# plt.ylabel('Product Name', fontsize=12, fontweight='bold')

# # Add value annotations
# for i, (product, profit) in enumerate(product_profit.items()):
#     ax.text(profit + max(product_profit.values()) * 0.01, i, f'${profit:,.0f}', 
#             va='center', fontweight='bold', fontsize=10)

# plt.grid(axis='x', alpha=0.3)
# plt.tight_layout()
# plt.show()

# print("Key Insights:")
# print(f"• Most profitable product generates: ${product_profit.iloc[0]:,.0f}")
# print(f"• Top 10 products contribute: ${product_profit.sum():,.0f} total profit")
# print(f"• Average profit per top product: ${product_profit.mean():,.0f}")


# 🔍 Discount vs Profit Scatter Plot
# Use sns.scatterplot() to visualize the relationship between Discount and Profit.
# - Add hue=Product Category to reveal category-level trends.
# - Overlay a regplot() to visualize trend lines.

# ❗ What discount level starts correlating with consistent losses? Varying trends by category?

# # Discount vs Profit Analysis
# plt.figure(figsize=(14, 8))

# # Create the scatter plot with category colors
# sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category', 
#                alpha=0.6, s=50)

# # Add regression line for overall trend
# sns.regplot(data=df, x='Discount', y='Profit', scatter=False, 
#            color='red', line_kws={'linewidth': 2, 'linestyle': '--'})

# # Customize the plot
# plt.title('Discount Strategy Analysis: Impact on Profitability by Category', 
#           fontsize=16, fontweight='bold', pad=20)
# plt.xlabel('Discount Rate', fontsize=12, fontweight='bold')
# plt.ylabel('Profit ($)', fontsize=12, fontweight='bold')

# # Add horizontal line at profit = 0
# plt.axhline(y=0, color='black', linestyle='-', alpha=0.3, linewidth=1)
# plt.text(0.5, 50, 'Break-even line', fontsize=10, alpha=0.7)

# plt.grid(True, alpha=0.3)
# plt.legend(title='Product Category', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.show()

# # Analytical insights
# print("Discount Analysis Insights:")
# high_discount = df[df['Discount'] > 0.2]  # Discounts above 20%
# print(f"• Transactions with >20% discount: {len(high_discount):,}")
# print(f"• Average profit for high discounts: ${high_discount['Profit'].mean():.2f}")
# print(f"• Percentage of high-discount sales with losses: {(high_discount['Profit'] < 0).mean()*100:.1f}%")

# # Category-specific analysis
# print("\nCategory-specific discount impact:")
# for category in df['Category'].unique():
#     cat_data = df[df['Category'] == category]
#     high_disc_cat = cat_data[cat_data['Discount'] > 0.2]
#     if len(high_disc_cat) > 0:
#         avg_loss = high_disc_cat['Profit'].mean()
#         print(f"• {category}: Average profit at >20% discount = ${avg_loss:.2f}")


# 4. Methodology and Tooling Review

# Create a markdown cell with a comparative evaluation of Matplotlib vs. Seaborn:

# # Code to demonstrate library comparison
# print("=== LIBRARY COMPARISON ANALYSIS ===")
# print()

# # Matplotlib strengths demonstrated
# print("MATPLOTLIB STRENGTHS (from our analysis):")
# print("• Fine-grained control over interactive widgets")
# print("• Custom annotations and text positioning") 
# print("• Precise subplot layouts and figure sizing")
# print("• Integration with ipywidgets for dynamic updates")
# print()

# # Seaborn strengths demonstrated  
# print("SEABORN STRENGTHS (from our analysis):")
# print("• Built-in statistical visualizations (regplot)")
# print("• Automatic color palettes and legends")
# print("• Clean, publication-ready default styling")
# print("• Easy categorical data visualization")
# print()

# print("SPEED COMPARISON:")
# import time

# # Time a simple matplotlib plot
# start = time.time()
# plt.figure(figsize=(8, 6))
# plt.plot(df.groupby('Order Year')['Sales'].sum())
# plt.close()
# matplotlib_time = time.time() - start

# # Time a seaborn plot
# start = time.time()
# plt.figure(figsize=(8, 6))
# sns.lineplot(data=df.groupby('Order Year')['Sales'].sum().reset_index(), 
#              x='Order Year', y='Sales')
# plt.close()
# seaborn_time = time.time() - start

# print(f"• Matplotlib basic plot: {matplotlib_time:.4f} seconds")
# print(f"• Seaborn equivalent: {seaborn_time:.4f} seconds")


# Recommendation Template:

# “For rapid exploration, I will use Matplotlib because it offers faster rendering for basic plots and seamless integration with interactive widgets for dynamic analysis.
# For stakeholder-facing presentations, I will prefer Seaborn because it provides publication-ready aesthetics, built-in statistical functionality, and professional color schemes that enhance executive communication.”



# 5. Final Deliverable

# Your Jupyter Notebook should include:

# ✅ Professional structure: Markdown headers, clear code comments
# 📊 Visualizations: Interactive and static, diagnostic and explanatory
# 📝 Executive Summary: Top 3–5 bullet points summarizing key findings
# Enhanced Executive Summary Template:



# # Generate automated insights for executive summary
# print("=== EXECUTIVE SUMMARY - KEY FINDINGS ===")
# print()

# # Sales performance metrics
# total_sales = df['Sales'].sum()
# total_profit = df['Profit'].sum()
# profit_margin = (total_profit / total_sales) * 100

# print(f"📊 BUSINESS PERFORMANCE:")
# print(f"• Total Revenue: ${total_sales:,.0f}")
# print(f"• Total Profit: ${total_profit:,.0f}")
# print(f"• Overall Profit Margin: {profit_margin:.1f}%")
# print()

# # Geographic insights
# top_state = state_sales.index[-1]
# top_state_sales = state_sales.iloc[-1]
# print(f"🗺️ GEOGRAPHIC PERFORMANCE:")
# print(f"• Top performing state: {top_state} (${top_state_sales:,.0f})")
# print(f"• Geographic concentration: Top 5 states = {(state_sales.tail(5).sum()/total_sales)*100:.1f}% of sales")
# print()

# # Product insights
# top_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False).index[0]
# print(f"🏆 PRODUCT PERFORMANCE:")
# print(f"• Leading category: {top_category}")
# print(f"• Most profitable product: {product_profit.index[0]}")
# print()

# # Discount insights
# high_discount_loss_rate = (df[df['Discount'] > 0.2]['Profit'] < 0).mean() * 100
# print(f"💰 DISCOUNT STRATEGY INSIGHTS:")
# print(f"• High discount risk: {high_discount_loss_rate:.1f}% of >20% discounts result in losses")
# print(f"• Recommended max discount threshold: 20% to maintain profitability")


# Example Finding

# “Furniture discounts above 20% lead to average profit losses of 15%.”

# Example Recommendation

# “Limit standard Furniture discounts to a maximum of 20%. Introduce approval steps for exceptions.”



# 🧠 Optional Advanced Challenges
# 📊 Build an interactive dashboard (e.g., using ipywidgets or Voilà) to combine charts.
# # Advanced: Multi-chart dashboard
# def create_dashboard():
#     # Create subplot layout
#     fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

#     # Chart 1: Monthly sales trend
#     monthly_total = df.groupby('Order Month-Year')['Sales'].sum()
#     ax1.plot(monthly_total.index.to_timestamp(), monthly_total.values, marker='o')
#     ax1.set_title('Monthly Sales Trend')
#     ax1.tick_params(axis='x', rotation=45)

#     # Chart 2: Category performance
#     category_sales = df.groupby('Category')['Sales'].sum()
#     ax2.bar(category_sales.index, category_sales.values)
#     ax2.set_title('Sales by Category')

#     # Chart 3: State performance (top 10)
#     top_10_states = state_sales.tail(10)
#     ax3.barh(range(len(top_10_states)), top_10_states.values)
#     ax3.set_yticks(range(len(top_10_states)))
#     ax3.set_yticklabels(top_10_states.index)
#     ax3.set_title('Top 10 States by Sales')

#     # Chart 4: Discount vs Profit
#     for category in df['Category'].unique():
#         cat_data = df[df['Category'] == category]
#         ax4.scatter(cat_data['Discount'], cat_data['Profit'], 
#                    label=category, alpha=0.6)
#     ax4.set_xlabel('Discount')
#     ax4.set_ylabel('Profit')
#     ax4.set_title('Discount vs Profit by Category')
#     ax4.legend()
#     ax4.axhline(y=0, color='black', linestyle='--', alpha=0.5)

#     plt.tight_layout()
#     plt.show()

# # Call the dashboard function
# create_dashboard()


# 🏷️ Annotate outliers in Discount vs. Profit (e.g., label top 3 most and least profitable transactions).
# # Advanced: Outlier analysis with annotations
# plt.figure(figsize=(12, 8))

# # Create base scatter plot
# sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category', alpha=0.6)

# # Identify and annotate outliers
# top_3_profitable = df.nlargest(3, 'Profit')
# bottom_3_profitable = df.nsmallest(3, 'Profit')

# # Annotate top performers
# for idx, row in top_3_profitable.iterrows():
#     plt.annotate(f'Best: ${row["Profit"]:.0f}', 
#                 xy=(row['Discount'], row['Profit']),
#                 xytext=(10, 10), textcoords='offset points',
#                 bbox=dict(boxstyle='round,pad=0.3', facecolor='green', alpha=0.7),
#                 arrowprops=dict(arowstyle='->', connectionstyle='arc3,rad=0'))

# # Annotate worst performers  
# for idx, row in bottom_3_profitable.iterrows():
#     plt.annotate(f'Worst: ${row["Profit"]:.0f}', 
#                 xy=(row['Discount'], row['Profit']),
#                 xytext=(10, -20), textcoords='offset points',
#                 bbox=dict(boxstyle='round,pad=0.3', facecolor='red', alpha=0.7),
#                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

# plt.title('Discount vs Profit Analysis with Outlier Identification')
# plt.show()


# ⚙️ Rebuild one interactive chart with Plotly Express. Briefly compare advantages/disadvantages vs. Matplotlib + ipywidgets.
# # Advanced: Plotly comparison
# import plotly.express as px
# import plotly.graph_objects as go

# # Create interactive Plotly version of discount analysis
# fig = px.scatter(df, x='Discount', y='Profit', color='Category',
#                 hover_data=['Product Name', 'Sales'], 
#                 title='Interactive Discount vs Profit Analysis (Plotly)')

# # Add trendline
# fig.add_traces(px.scatter(df, x='Discount', y='Profit', trendline='ols').data[1])

# fig.show()

# print("PLOTLY vs MATPLOTLIB COMPARISON:")
# print("Plotly Advantages:")
# print("• Built-in interactivity (zoom, pan, hover)")
# print("• Easy to share online")
# print("• Professional tooltips and legends")
# print("• Automatic responsive design")
# print()
# print("Matplotlib + ipywidgets Advantages:")  
# print("• More customization control")
# print("• Better integration with Jupyter workflows")
# print("• Smaller file sizes")
# print("• Familiar to Python data scientists")


# Submit your Daily Challenge
# Upload your polished Jupyter Notebook with full analysis and recommendations to GitHub.


Daily Challenge: Strategic Analysis of Superstore Performance


👩‍🏫 👩🏿‍🏫 What You’ll Learn
How to translate business objectives into actionable data analysis questions.
How to use Matplotlib and Seaborn for diagnostic and communicative visualizations.
How to create interactive widgets for dynamic data exploration.
How to derive and present actionable insights from retail sales data.
How to structure a professional analysis notebook and executive summary.


🛠️ What You Will Create
You’ll build a complete business intelligence report in a Jupyter Notebook using the US Superstore dataset. This will include interactive visualizations, deep-dive diagnostics, and strategic recommendations that simulate the role of a data analyst for a national retailer.



What Will You Use
Concepts: diagnostic analysis, exploratory vs. explanatory visualizations, profit margin, strategic KPIs
Libraries: Pandas, Matplotlib, Seaborn, ipywidgets
Techniques: time-series analysis, geographic analysis, discount strategy diagnostics, interactive dashboards


Your Task
1. Data Scoping and Preparation

Download and load the US Superstore dataset. Begin with a preliminary data assessment:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from ipywidgets import interact, Dropdown, IntSlider
from IPython.display import display
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('superstore_dataset.csv')


print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

df.info()
df.describe()
df.isnull().sum()


Clean and preprocess your data:

🧹 Handle missing values and duplicates
Use appropriate methods (dropna(), fillna(), or imputation) and justify your choices for each case in markdown cells.


print("Duplicate rows:", df.duplicated().sum())


df = df.drop_duplicates()


print("\nMissing values per column:")
print(df.isnull().sum())


if 'Postal Code' in df.columns:
    df['Postal Code'] = df['Postal Code'].fillna(0)


🕓 Fix data types
Ensure that date columns are converted to datetime objects using pd.to_datetime() for time-series analysis.


date_columns = ['Order Date', 'Ship Date']
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col])


print("Data types after conversion:")
print(df[date_columns].dtypes)


🏗️ Feature engineering
Create new features to enrich your analysis:
Profit Margin = (Profit / Sales) * 100
Order Year (e.g., df['Order Date'].dt.year)
Order Month (e.g., df['Order Date'].dt.month)



df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month-Year'] = df['Order Date'].dt.to_period('M')


print("New features created:")
print(df[['Sales', 'Profit', 'Profit Margin', 'Order Year', 'Order Month']].head())


2. Deep-Dive Exploratory Analysis (Matplotlib)

📈 Time-Series Trend Analysis
Create a line plot of total monthly Sales across all years using Matplotlib.
Add interactivity with ipywidgets.Dropdown to select a Product Category, dynamically updating the chart.

🔎 Look for patterns: seasonality, year-over-year changes, product-specific trends.


monthly_sales = df.groupby(['Order Month-Year', 'Category'])['Sales'].sum().reset_index()
monthly_sales['Date'] = monthly_sales['Order Month-Year'].dt.to_timestamp()


def plot_monthly_sales(category='All'):
    plt.figure(figsize=(12, 6))

    if category == 'All':

        total_monthly = df.groupby('Order Month-Year')['Sales'].sum()
        plt.plot(total_monthly.index.to_timestamp(), total_monthly.values, 
                marker='o', linewidth=2, markersize=4)
        plt.title('Monthly Sales Trend - All Categories', fontsize=16, fontweight='bold')
    else:
   
        category_data = monthly_sales[monthly_sales['Category'] == category]
        plt.plot(category_data['Date'], category_data['Sales'], 
                marker='o', linewidth=2, markersize=4)
        plt.title(f'Monthly Sales Trend - {category}', fontsize=16, fontweight='bold')

    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sales ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


categories = ['All'] + list(df['Category'].unique())
category_dropdown = Dropdown(options=categories, value='All', description='Category:')
interact(plot_monthly_sales, category=category_dropdown);


🗺️ Geographic Sales Performance
Build a horizontal bar chart showing total sales by State, sorted by amount.
Add a Top N slider widget to dynamically filter the number of displayed states.

💬 Identify high-performing states. Are sales centralized or geographically distributed?


state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=True)


def plot_top_states(top_n=10):
    plt.figure(figsize=(12, max(6, top_n * 0.4)))


    top_states = state_sales.tail(top_n)


    bars = plt.barh(range(len(top_states)), top_states.values, color='steelblue')
    plt.yticks(range(len(top_states)), top_states.index)
    plt.xlabel('Total Sales ($)', fontsize=12)
    plt.ylabel('State', fontsize=12)
    plt.title(f'Top {top_n} States by Sales Performance', fontsize=16, fontweight='bold')


    for i, (state, value) in enumerate(top_states.items()):
        plt.text(value + max(top_states.values()) * 0.01, i, f'${value:,.0f}', 
                va='center', fontsize=10)

    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.show()

    print(f"Total states analyzed: {len(state_sales)}")
    print(f"Top {top_n} states represent: ${top_states.sum():,.0f} in sales")


top_n_slider = IntSlider(min=5, max=25, value=10, description='Top N States:')
interact(plot_top_states, top_n=top_n_slider);


3. Communicating Insights (Seaborn)

🏆 Top 10 Most Profitable Products
Use Seaborn’s barplot() to show the top 10 products by total profit.
- Orient horizontally, label axes clearly, and annotate bars with exact profit values.
- Give the chart a descriptive title suitable for an executive summary.


product_profit = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 8))
ax = sns.barplot(x=product_profit.values, y=product_profit.index, 
                palette='viridis', orient='h')


plt.title('Top 10 Most Profitable Products\nExecutive Summary - Product Performance Analysis', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Total Profit ($)', fontsize=12, fontweight='bold')
plt.ylabel('Product Name', fontsize=12, fontweight='bold')


for i, (product, profit) in enumerate(product_profit.items()):
    ax.text(profit + max(product_profit.values()) * 0.01, i, f'${profit:,.0f}', 
            va='center', fontweight='bold', fontsize=10)

plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()

print("Key Insights:")
print(f"• Most profitable product generates: ${product_profit.iloc[0]:,.0f}")
print(f"• Top 10 products contribute: ${product_profit.sum():,.0f} total profit")
print(f"• Average profit per top product: ${product_profit.mean():,.0f}")


🔍 Discount vs Profit Scatter Plot
Use sns.scatterplot() to visualize the relationship between Discount and Profit.
- Add hue=Product Category to reveal category-level trends.
- Overlay a regplot() to visualize trend lines.

❗ What discount level starts correlating with consistent losses? Varying trends by category?


plt.figure(figsize=(14, 8))


sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category', 
               alpha=0.6, s=50)


sns.regplot(data=df, x='Discount', y='Profit', scatter=False, 
           color='red', line_kws={'linewidth': 2, 'linestyle': '--'})


plt.title('Discount Strategy Analysis: Impact on Profitability by Category', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Discount Rate', fontsize=12, fontweight='bold')
plt.ylabel('Profit ($)', fontsize=12, fontweight='bold')


plt.axhline(y=0, color='black', linestyle='-', alpha=0.3, linewidth=1)
plt.text(0.5, 50, 'Break-even line', fontsize=10, alpha=0.7)

plt.grid(True, alpha=0.3)
plt.legend(title='Product Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


print("Discount Analysis Insights:")
high_discount = df[df['Discount'] > 0.2]  # Discounts above 20%
print(f"• Transactions with >20% discount: {len(high_discount):,}")
print(f"• Average profit for high discounts: ${high_discount['Profit'].mean():.2f}")
print(f"• Percentage of high-discount sales with losses: {(high_discount['Profit'] < 0).mean()*100:.1f}%")


print("\nCategory-specific discount impact:")
for category in df['Category'].unique():
    cat_data = df[df['Category'] == category]
    high_disc_cat = cat_data[cat_data['Discount'] > 0.2]
    if len(high_disc_cat) > 0:
        avg_loss = high_disc_cat['Profit'].mean()
        print(f"• {category}: Average profit at >20% discount = ${avg_loss:.2f}")


4. Methodology and Tooling Review

Create a markdown cell with a comparative evaluation of Matplotlib vs. Seaborn:


print("=== LIBRARY COMPARISON ANALYSIS ===")
print()


print("MATPLOTLIB STRENGTHS (from our analysis):")
print("• Fine-grained control over interactive widgets")
print("• Custom annotations and text positioning") 
print("• Precise subplot layouts and figure sizing")
print("• Integration with ipywidgets for dynamic updates")
print()

 
print("SEABORN STRENGTHS (from our analysis):")
print("• Built-in statistical visualizations (regplot)")
print("• Automatic color palettes and legends")
print("• Clean, publication-ready default styling")
print("• Easy categorical data visualization")
print()

print("SPEED COMPARISON:")
import time


start = time.time()
plt.figure(figsize=(8, 6))
plt.plot(df.groupby('Order Year')['Sales'].sum())
plt.close()
matplotlib_time = time.time() - start


start = time.time()
plt.figure(figsize=(8, 6))
sns.lineplot(data=df.groupby('Order Year')['Sales'].sum().reset_index(), 
             x='Order Year', y='Sales')
plt.close()
seaborn_time = time.time() - start

print(f"• Matplotlib basic plot: {matplotlib_time:.4f} seconds")
print(f"• Seaborn equivalent: {seaborn_time:.4f} seconds")


Recommendation Template:

“For rapid exploration, I will use Matplotlib because it offers faster rendering for basic plots and seamless integration with interactive widgets for dynamic analysis.
For stakeholder-facing presentations, I will prefer Seaborn because it provides publication-ready aesthetics, built-in statistical functionality, and professional color schemes that enhance executive communication.”



5. Final Deliverable

Your Jupyter Notebook should include:

✅ Professional structure: Markdown headers, clear code comments
📊 Visualizations: Interactive and static, diagnostic and explanatory
📝 Executive Summary: Top 3–5 bullet points summarizing key findings
Enhanced Executive Summary Template:



print("=== EXECUTIVE SUMMARY - KEY FINDINGS ===")
print()


total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100

print(f"📊 BUSINESS PERFORMANCE:")
print(f"• Total Revenue: ${total_sales:,.0f}")
print(f"• Total Profit: ${total_profit:,.0f}")
print(f"• Overall Profit Margin: {profit_margin:.1f}%")
print()


top_state = state_sales.index[-1]
top_state_sales = state_sales.iloc[-1]
print(f"🗺️ GEOGRAPHIC PERFORMANCE:")
print(f"• Top performing state: {top_state} (${top_state_sales:,.0f})")
print(f"• Geographic concentration: Top 5 states = {(state_sales.tail(5).sum()/total_sales)*100:.1f}% of sales")
print()


top_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False).index[0]
print(f"🏆 PRODUCT PERFORMANCE:")
print(f"• Leading category: {top_category}")
print(f"• Most profitable product: {product_profit.index[0]}")
print()


high_discount_loss_rate = (df[df['Discount'] > 0.2]['Profit'] < 0).mean() * 100
print(f"💰 DISCOUNT STRATEGY INSIGHTS:")
print(f"• High discount risk: {high_discount_loss_rate:.1f}% of >20% discounts result in losses")
print(f"• Recommended max discount threshold: 20% to maintain profitability")


Example Finding

“Furniture discounts above 20% lead to average profit losses of 15%.”

Example Recommendation

“Limit standard Furniture discounts to a maximum of 20%. Introduce approval steps for exceptions.”



🧠 Optional Advanced Challenges
📊 Build an interactive dashboard (e.g., using ipywidgets or Voilà) to combine charts.

def create_dashboard():

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))


    monthly_total = df.groupby('Order Month-Year')['Sales'].sum()
    ax1.plot(monthly_total.index.to_timestamp(), monthly_total.values, marker='o')
    ax1.set_title('Monthly Sales Trend')
    ax1.tick_params(axis='x', rotation=45)


    category_sales = df.groupby('Category')['Sales'].sum()
    ax2.bar(category_sales.index, category_sales.values)
    ax2.set_title('Sales by Category')


    top_10_states = state_sales.tail(10)
    ax3.barh(range(len(top_10_states)), top_10_states.values)
    ax3.set_yticks(range(len(top_10_states)))
    ax3.set_yticklabels(top_10_states.index)
    ax3.set_title('Top 10 States by Sales')


    for category in df['Category'].unique():
        cat_data = df[df['Category'] == category]
        ax4.scatter(cat_data['Discount'], cat_data['Profit'], 
                   label=category, alpha=0.6)
    ax4.set_xlabel('Discount')
    ax4.set_ylabel('Profit')
    ax4.set_title('Discount vs Profit by Category')
    ax4.legend()
    ax4.axhline(y=0, color='black', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.show()


create_dashboard()


🏷️ Annotate outliers in Discount vs. Profit (e.g., label top 3 most and least profitable transactions).

plt.figure(figsize=(12, 8))


sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category', alpha=0.6)


top_3_profitable = df.nlargest(3, 'Profit')
bottom_3_profitable = df.nsmallest(3, 'Profit')


for idx, row in top_3_profitable.iterrows():
    plt.annotate(f'Best: ${row["Profit"]:.0f}', 
                xy=(row['Discount'], row['Profit']),
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='green', alpha=0.7),
                arrowprops=dict(arowstyle='->', connectionstyle='arc3,rad=0'))

 
for idx, row in bottom_3_profitable.iterrows():
    plt.annotate(f'Worst: ${row["Profit"]:.0f}', 
                xy=(row['Discount'], row['Profit']),
                xytext=(10, -20), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='red', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

plt.title('Discount vs Profit Analysis with Outlier Identification')
plt.show()


⚙️ Rebuild one interactive chart with Plotly Express. Briefly compare advantages/disadvantages vs. Matplotlib + ipywidgets.

import plotly.express as px
import plotly.graph_objects as go


fig = px.scatter(df, x='Discount', y='Profit', color='Category',
                hover_data=['Product Name', 'Sales'], 
                title='Interactive Discount vs Profit Analysis (Plotly)')


fig.add_traces(px.scatter(df, x='Discount', y='Profit', trendline='ols').data[1])

fig.show()

print("PLOTLY vs MATPLOTLIB COMPARISON:")
print("Plotly Advantages:")
print("• Built-in interactivity (zoom, pan, hover)")
print("• Easy to share online")
print("• Professional tooltips and legends")
print("• Automatic responsive design")
print()
print("Matplotlib + ipywidgets Advantages:")  
print("• More customization control")
print("• Better integration with Jupyter workflows")
print("• Smaller file sizes")
print("• Familiar to Python data scientists")


