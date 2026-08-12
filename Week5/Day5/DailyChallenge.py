# Daily Challenge: Interactive Data Visualization with Matplotlib and Seaborn


# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Advanced data visualization techniques.
# Interactive chart creation using Matplotlib.
# Elegant static data presentation with Seaborn.


# Your Task


# 1. Data Preparation:
# Download and explore the US Superstore data.
# Perform basic data cleaning and preprocessing.


# 2. Data Visualization with Matplotlib:
# Create an interactive line chart to show sales trends over the years.
# Build an interactive map to visualize sales distribution by country.


# 3. Data Visualization with Seaborn:
# Use Seaborn to generate a bar chart showing top 10 products by sales.
# Create a scatter plot to analyze the relationship between profit and discount.


# 4. Comparative Analysis:
# Compare the insights gained from Matplotlib and Seaborn visualizations.
# Document your observations about the ease of use and effectiveness of both tools.


# 5. Code and Insights:
# Write clear, well-documented Python code.
# Include your analysis and insights as comments or markdown cells in your Jupyter notebook.

import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

warnings.filterwarnings('ignore')

# 1. Load Dataset
filepath = 'US Superstore data.xls'
df = pd.read_excel(filepath)

# 2. Basic Exploration & Validation
print("Dataset Shape:", df.shape)
print("\nMissing Values per Column:\n", df.isnull().sum())

# 3. Data Cleaning & Type Formatting
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 4. Feature Engineering
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month_Year'] = df['Order Date'].dt.to_period('M').dt.to_timestamp()
df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100

print("\nPreprocessed Data Sample:")
display(
    df[[
        'Order Date',
        'Category',
        'Sales',
        'Profit',
        'Year',
        'Profit Margin (%)',
    ]].head()
)

from ipywidgets import Dropdown, interact


# Interactive line chart function using ipywidgets & Matplotlib
def plot_sales_trend(region='All'):
  plt.figure(figsize=(10, 5))

  if region == 'All':
    data = df.groupby('Year')['Sales'].sum()
    title = 'US Superstore: Annual Sales Trends (All Regions)'
  else:
    data = df[df['Region'] == region].groupby('Year')['Sales'].sum()
    title = f'US Superstore: Annual Sales Trends ({region} Region)'

  plt.plot(
      data.index,
      data.values,
      marker='o',
      linewidth=2.5,
      color='#1f77b4',
      markersize=8,
  )
  plt.title(title, fontsize=14, fontweight='bold', pad=15)
  plt.xlabel('Year', fontsize=12, fontweight='bold')
  plt.ylabel('Total Sales ($)', fontsize=12, fontweight='bold')
  plt.xticks(data.index)

  for x, y in zip(data.index, data.values):
    plt.annotate(
        f'${y:,.0f}',
        (x, y),
        textcoords='offset points',
        xytext=(0, 10),
        ha='center',
        fontweight='bold',
    )

  plt.grid(True, linestyle='--', alpha=0.5)
  plt.tight_layout()
  plt.show()


# Display Interactive Widget in Jupyter
region_dropdown = Dropdown(
    options=['All'] + list(df['Region'].unique()),
    value='All',
    description='Region:',
)
interact(plot_sales_trend, region=region_dropdown)

from ipywidgets import IntSlider


# Interactive Top N State Geographic Sales Plot
def plot_top_states_map(top_n=10):
  state_sales = (
      df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(top_n)
  )

  plt.figure(figsize=(10, max(5, top_n * 0.4)))
  bars = plt.barh(
      state_sales.index[::-1],
      state_sales.values[::-1],
      color='#3182bd',
      height=0.7,
  )

  plt.title(
      f'Top {top_n} US States by Total Sales Revenue',
      fontsize=14,
      fontweight='bold',
      pad=15,
  )
  plt.xlabel('Total Sales ($)', fontsize=12, fontweight='bold')
  plt.ylabel('State', fontsize=12, fontweight='bold')

  for i, (val, name) in enumerate(
      zip(state_sales.values[::-1], state_sales.index[::-1])
  ):
    plt.text(
        val + (max(state_sales.values) * 0.01),
        i,
        f'${val:,.0f}',
        va='center',
        fontsize=9,
    )

  plt.grid(axis='x', linestyle='--', alpha=0.5)
  plt.tight_layout()
  plt.show()


# Display Slider Widget
interact(
    plot_top_states_map,
    top_n=IntSlider(min=5, max=25, value=15, description='Top N States:'),
)

# Aggregate Top 10 Products by Revenue
top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=top_products, x='Sales', y='Product Name', palette='viridis')

plt.title(
    'Top 10 Products by Total Sales Revenue',
    fontsize=14,
    fontweight='bold',
    pad=15,
)
plt.xlabel('Total Sales ($)', fontsize=12, fontweight='bold')
plt.ylabel('Product Name', fontsize=12, fontweight='bold')

for p in ax.patches:
  width = p.get_width()
  ax.annotate(
      f'${width:,.0f}',
      (width + 500, p.get_y() + p.get_height() / 2),
      ha='left',
      va='center',
      fontsize=9,
      fontweight='bold',
  )

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# Scatter Plot colored by Product Category
sns.scatterplot(
    data=df,
    x='Discount',
    y='Profit',
    hue='Category',
    alpha=0.7,
    s=60,
    palette='Set2',
)

# Linear Trendline overlay
sns.regplot(
    data=df,
    x='Discount',
    y='Profit',
    scatter=False,
    color='red',
    line_kws={'linewidth': 2, 'linestyle': '--'},
)

plt.axhline(0, color='black', linestyle='-', alpha=0.5)
plt.title(
    'Profitability vs. Discount Rate Analysis by Category',
    fontsize=14,
    fontweight='bold',
    pad=15,
)
plt.xlabel('Discount Rate', fontsize=12, fontweight='bold')
plt.ylabel('Profit ($)', fontsize=12, fontweight='bold')
plt.legend(title='Category', bbox_to_anchor=(1.02, 1), loc='upper left')

plt.tight_layout()
plt.show()

Key Observations
Dynamic Interactivity (Matplotlib): Matplotlib excels when building user-driven exploratory interfaces inside Jupyter Notebooks (e.g., interactive region dropdowns and dynamic state sliders).

Statistical Elegance (Seaborn): Seaborn is better for rapid, publication-grade multivariate analysis. Expressing complex groupings (hue='Category') and trend regressions requires far less boilerplate code.

5. Key Business Insights
Revenue Growth: Annual store revenue expanded steadily from $484,247 (2014) to $733,215 (2017), proving consistent multi-year demand expansion.

Geographic Dependency: California ($457,688) and New York ($310,876) account for over 33% of total US Superstore sales combined.

Product Drivers: The Canon imageCLASS 2200 Advanced Copier generated $61,600 in revenue, making it the single highest-grossing product in the catalog.

Discounting Thresholds: Discounts exceeding 20% consistently force transaction profit margins into negative territory across all product categories.