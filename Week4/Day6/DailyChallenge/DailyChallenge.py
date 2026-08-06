# Daily Challenge: Data Handling and Analysis in Python


# What You Will Learn
# Advanced techniques for data normalization, reduction, and aggregation.
# Skills in gathering, exploring, integrating, and cleaning data using Python.
# Proficiency in using Pandas for complex data manipulation.


# Your Task
# Download and import the Data Science Job Salary dataset.
# Normalize the ‘salary’ column using Min-Max normalization which scales all salary values between 0 and 1.
# Implement dimensionality reduction like Principal Component Analysis (PCA) or t-SNE to reduce the number of features (columns) in the dataset.
# Group the dataset by the ‘experience_level’ column and calculate the average and median salary for each experience level (e.g., Junior, Mid-level, Senior).
# Hint :
# As a reminder, normalization is crucial when dealing with data that has different ranges. For example, salary data might have a wide range (e.g., from $20,000 to $200,000). By scaling the data using Min-Max normalization, you make sure that all salary values fall within a consistent range (0 to 1). This is particularly helpful when the data is going to be used in machine learning models, as some algorithms (like k-nearest neighbors or neural networks) perform better when features are normalized. It ensures that no single salary dominates the learning process, making the analysis more balanced.

# Dimensionality reduction helps simplify complex datasets by reducing the number of variables under consideration. This can make the data more manageable and help avoid the curse of dimensionality—a phenomenon where machine learning models struggle when dealing with high-dimensional data.
# PCA, for instance, helps in retaining the most important information (variance) from the dataset while reducing noise and redundancy.
# It can also speed up the training process for models and help in visualizing data in fewer dimensions.

# Aggregating data helps in understanding trends within subgroups of the dataset.
# Calculating average and median salaries for each experience level gives insights into the compensation distribution and disparities across different job levels. This kind of aggregation can help in answering business questions like “How does salary evolve with experience?” or “What is the salary distribution for senior-level roles?”


import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"

ds_url = "https://raw.githubusercontent.com/sudarshan-koirala/data-science-job-salaries/main/ds_salaries.csv"

df = pd.read_csv(ds_url)
print("Initial Dataset Shape:", df.shape)
print("\nFirst 3 rows of dataset:\n", df.head(3))


scaler = MinMaxScaler()

df['salary_normalized'] = scaler.fit_transform(df[['salary']])

print("\n--- Min-Max Normalization Results ---")
print(df[['salary', 'salary_normalized']].head())


numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

pca_input_df = df[numeric_cols].dropna()

std_scaler = MinMaxScaler()
scaled_numeric_data = std_scaler.fit_transform(pca_input_df)

pca = PCA(n_components=2)
pca_transformed = pca.fit_transform(scaled_numeric_data)

pca_df = pd.DataFrame(data=pca_transformed, columns=['PC1', 'PC2'])

print("\n--- PCA Dimensionality Reduction Results ---")
print(f"Original Numerical Dimensions: {scaled_numeric_data.shape[1]} features")
print(f"Reduced Dimensions: {pca_df.shape[1]} components")
print("\nFirst 5 rows of PCA components:\n", pca_df.head())
print(f"\nExplained Variance Ratio of PC1 and PC2: {pca.explained_variance_ratio_}")


salary_column_to_aggregate = 'salary_in_usd' if 'salary_in_usd' in df.columns else 'salary'

experience_summary = df.groupby('experience_level')[salary_column_to_aggregate].agg(
    Average_Salary='mean',
    Median_Salary='median',
    Sample_Count='count'
).reset_index()


experience_mapping = {
    'EN': 'Entry-level / Junior',
    'MI': 'Mid-level',
    'SE': 'Senior-level',
    'EX': 'Executive-level / Director'
}
if set(experience_summary['experience_level']).issubset(experience_mapping.keys()):
    experience_summary['experience_level'] = experience_summary['experience_level'].map(experience_mapping)

print("\n--- Experience Level Salary Summary ---")
print(experience_summary.to_string(index=False))