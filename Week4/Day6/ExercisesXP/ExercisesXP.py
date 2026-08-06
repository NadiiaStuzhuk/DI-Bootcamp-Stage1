# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# By the end of this notebook, you will be able to:

# Detect and remove duplicate entries from a dataset.
# Apply appropriate strategies for handling missing values.
# Perform basic feature engineering (new attributes, encoding).
# Detect and handle outliers using statistical methods.
# Standardize and normalize features to prepare for modeling.
# Transform and encode features (e.g. Age groups) for improved model input.


# Each exercise builds on the previous one — keep a consistent preprocessing narrative throughout the notebook. Also, be sure to comment your code to explain your decisions, especially when choosing thresholds or methods.



# 💡 Tip: The recommended preprocessing sequence is:

# Handle duplicates
# Address missing values
# Treat outliers
# Encode categorical variables


# For all of the below exercises, you will use the Titanic dataset (train.csv), so load it beforehand on your notebook.
# You will notice in the following exercises that the dataset is already pretty clean but try and understand all of the functions used for preprocessing the data.
# Optionally, if you have time and willing to, you can redo the exercises with a less clean dataset : Weather Data Munich 1954-2022.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Initial Dataset Shape:", df.shape)
df.head()



# 🌟 Exercise 1: Duplicate Detection and Removal
# Instructions
# Objective: Identify and remove duplicate entries in the Titanic dataset.

# Load the Titanic dataset.
# Identify if there are any duplicate rows based on all columns.
# Remove any duplicate rows found in the dataset.
# Verify the removal of duplicates by checking the number of rows before and after the duplicate removal.
# Hint: Use the duplicated() and drop_duplicates() functions in Pandas.


num_duplicates = df.duplicated().sum()
print(f"Total duplicate rows found: {num_duplicates}")

rows_before = len(df)

df = df.drop_duplicates()

rows_after = len(df)
print(f"Rows before: {rows_before}, Rows after: {rows_after}")
print(f"Removed rows: {rows_before - rows_after}")


# 🌟 Exercise 2: Handling Missing Values
# Instructions
# Identify columns in the Titanic dataset with missing values.
# Explore different strategies for handling missing data, such as removal, imputation, and filling with a constant value.
# Apply each strategy to different columns based on the nature of the data.
# Hint: Review methods like dropna(), fillna(), and SimpleImputer from scikit-learn.


missing_info = df.isnull().sum()
print("Missing values per column:\n", missing_info[missing_info > 0])


df['Cabin'] = df['Cabin'].fillna('Unknown')


age_imputer = SimpleImputer(strategy='median')
df['Age'] = age_imputer.fit_transform(df[['Age']])


embarked_imputer = SimpleImputer(strategy='most_frequent')
df['Embarked'] = embarked_imputer.fit_transform(df[['Embarked']]).ravel()

print("\nVerification of missing values after imputation:\n", df.isnull().sum().sum())



# 🌟 Exercise 3: Feature Engineering
# Instructions
# Create new features, such as Family Size from SibSp and Parch, and Title extracted from the Name column.
# Convert categorical variables into numerical form using techniques like one-hot encoding or label encoding.
# You will encode new categorical features (like Title) here, but do not scale numerical features yet — that will come after outlier handling.
# Hint: Utilize Pandas for data manipulation and scikit-learn’s preprocessing module for encoding.


df['FamilySize'] = df['SibSp'] + df['Parch'] + 1


df['IsAlone'] = (df['FamilySize'] == 1).astype(int)


df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)


df['Title'] = df['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 
                                   'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
df['Title'] = df['Title'].replace('Mlle', 'Miss')
df['Title'] = df['Title'].replace('Ms', 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')

print("Title distribution:\n", df['Title'].value_counts())


# 🌟 Exercise 4: Outlier Detection and Handling
# Goal: Detect and cap or transform outliers in columns like Fare and Age.

# 1. Visualize distributions using boxplots or histograms to identify potential outliers.
# 2. Use IQR or Z-score methods to detect them.
# 3. Handle outliers with:

# Quantile capping (e.g. 0.98)
# Log transformation
# Row removal
# 4. Compare the dataset before and after treatment.

# 📌 Note: Small differences between 0.98 and 0.99 quantiles are normal when extreme values are rare or far apart. Use df.quantile() to explore and choose thresholds empirically, backed by visualization.


plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
sns.boxplot(x=df['Fare'])
plt.title('Fare Distribution (Before Capping)')

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Age'])
plt.title('Age Distribution (Before Capping)')
plt.show()


upper_limit_fare = df['Fare'].quantile(0.98)
print(f"98th Percentile Threshold for Fare: {upper_limit_fare:.2f}")
df['Fare'] = np.where(df['Fare'] > upper_limit_fare, upper_limit_fare, df['Fare'])


Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
upper_limit_age = Q3 + 1.5 * IQR
df['Age'] = np.where(df['Age'] > upper_limit_age, upper_limit_age, df['Age'])


plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
sns.boxplot(x=df['Fare'])
plt.title('Fare Distribution (After 0.98 Capping)')

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Age'])
plt.title('Age Distribution (After IQR Capping)')
plt.show()

# 🌟 Exercise 5: Data Standardization and Normalization
# Goal: Scale numerical features to prepare for modeling.

# Use StandardScaler (mean = 0, std = 1) for normally distributed features.
# Use MinMaxScaler (range [0, 1]) for features that are skewed or bounded.
# 📌 Important: Perform this step after outlier treatment to avoid distortion caused by extreme values.


std_scaler = StandardScaler()
df['Age_Scaled'] = std_scaler.fit_transform(df[['Age']])


minmax_scaler = MinMaxScaler()
df['Fare_Scaled'] = minmax_scaler.fit_transform(df[['Fare']])
df['FamilySize_Scaled'] = minmax_scaler.fit_transform(df[['FamilySize']])

print(df[['Age_Scaled', 'Fare_Scaled', 'FamilySize_Scaled']].describe())


# 🌟 Exercise 6: Feature Encoding
# Goal: Finalize categorical variable encoding.

# 1. Identify remaining categorical columns (e.g. Sex, Embarked, Title).
# 2. Apply:

# One-Hot Encoding for nominal variables.
# Label Encoding if any ordinal variables remain.
# 3. Merge encoded columns back into the main dataset.

# 📌 Reminder: Encoding comes after handling missing values and outliers, but before scaling (if applicable).


categorical_cols = ['Sex', 'Embarked', 'Title']


df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)


label_enc = LabelEncoder()
df_encoded['Pclass_Encoded'] = label_enc.fit_transform(df_encoded['Pclass'])

print("Encoded Columns List:\n", df_encoded.columns.tolist())


# 🌟 Exercise 7: Data Transformation for Age Feature
# Goal: Create and encode age groups.

# Use pd.cut() to create bins for life stages (e.g. child, teen, adult, senior).
# Apply one-hot encoding using pd.get_dummies().
# 📌 Example: You might define bins like [0, 12, 18, 60, 100] and label them accordingly.


age_bins = [0, 12, 18, 60, 100]
age_labels = ['Child', 'Teenager', 'Adult', 'Senior']


df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=True)

print("Age Group Counts:\n", df['AgeGroup'].value_counts())


df_age_encoded = pd.get_dummies(df['AgeGroup'], prefix='AgeGroup', drop_first=False)


df_final = pd.concat([df_encoded, df_age_encoded], axis=1)

print("\nFinal Preprocessed Dataset Shape:", df_final.shape)
df_final.head()


