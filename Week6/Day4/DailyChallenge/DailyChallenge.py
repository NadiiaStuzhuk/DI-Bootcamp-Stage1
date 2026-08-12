# Objective:
# Apply your knowledge of NumPy, Pandas, and Matplotlib to analyze a real-world dataset. Utilize advanced statistical functions and array operations in NumPy, and integrate these with Pandas for data manipulation and Matplotlib for visualization.



# Dataset:
# You will work with the “Global Power Plant Database” provided by the World Resources Institute, which contains detailed information about power plants worldwide. This dataset is ideal for practicing array manipulations, statistical analysis, and time series data handling.

# Download the dataset here.

# or you can download it directly

# Here.



# Tasks:
# Data Import and Cleaning:

# Import the dataset using Pandas.
# Identify missing values and handle them appropriately.
# Use NumPy to convert relevant columns to numerical types if necessary.
# Exploratory Data Analysis:

# Utilize Pandas to summarize key statistics (mean, median, standard deviation) for numerical columns.
# Explore the distribution of power plants by country and fuel type.
# Statistical Analysis:

# Perform a statistical analysis of power output by fuel type using NumPy’s statistical functions.
# Use hypothesis testing to determine if the mean power output differs significantly between different fuel types.
# Time Series Analysis:

# If the dataset includes time-related data (like year of establishment), use NumPy to analyze trends over time.
# Explore how the mix of fuel types for power generation has evolved over the years.
# Advanced Visualization:

# Create visualizations using Matplotlib and Seaborn to illustrate your findings.
# Consider plotting the geographical distribution of power plants using latitude and longitude data, if available.
# Matrix Operations in Real-World Context:

# Demonstrate matrix operations by analyzing relationships between different attributes (e.g., fuel type, capacity, and geographic location).
# Discuss the relevance of eigenvectors and eigenvalues in this context.
# Integrating NumPy with Pandas and Matplotlib:

# Show how NumPy can be used to enhance data manipulation in Pandas and data visualization in Matplotlib.
# Provide examples, such as using NumPy arrays for complex filtering in Pandas or for creating sophisticated plots in Matplotlib.


import pandas as pd
import numpy as np


df = pd.read_csv('global_power_plant_database.csv')


df['commissioning_year'] = df['commissioning_year'].fillna(df['commissioning_year'].median())


df['generation_gwh_2019'] = df.groupby('primary_fuel')['generation_gwh_2019'].transform(
    lambda x: x.fillna(x.median())
)


capacity_array = np.array(df['capacity_mw'], dtype=np.float64)
generation_array = np.array(df['generation_gwh_2019'], dtype=np.float64)

from scipy import stats

coal_cap = df[df['primary_fuel'] == 'Coal']['capacity_mw'].values
gas_cap = df[df['primary_fuel'] == 'Gas']['capacity_mw'].values
solar_cap = df[df['primary_fuel'] == 'Solar']['capacity_mw'].values


f_stat, p_val = stats.f_oneway(coal_cap, gas_cap, solar_cap)
print(f"ANOVA F-statistic: {f_stat:.4f}, p-value: {p_val:.4e}")


X = df[['capacity_mw', 'generation_gwh_2019', 'commissioning_year']].values


cov_matrix = np.cov(X.T)


eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("Eigenvalues (Variance Explained):", eigenvalues)
print("Eigenvectors (Principal Directions):\n", eigenvectors)


high_efficiency_mask = np.logical_and(
    df['capacity_mw'].values > 100,
    df['primary_fuel'].values == 'Wind'
)
wind_high_cap_df = df[high_efficiency_mask]


log_capacity = np.log1p(df['capacity_mw'].values)
color_map = plt.cm.viridis((log_capacity - log_capacity.min()) / (log_capacity.max() - log_capacity.min()))

plt.figure(figsize=(8, 4))
plt.scatter(df['longitude'], df['latitude'], c=color_map, s=15, alpha=0.7)
plt.title("Vector-Scaled Power Plant Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()

