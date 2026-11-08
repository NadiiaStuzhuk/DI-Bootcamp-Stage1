import warnings
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from scipy.stats import chi2_contingency, norm
import seaborn as sns

warnings.filterwarnings('ignore')
sns.set_theme(style='whitegrid')

# =====================================================================
# STEP 1: OOP ARCHITECTURE - DATACLASSES & ENTITIES
# =====================================================================


@dataclass
class UserProfile:
  """Encapsulates individual user preferences and activity records."""

  user_id: int
  name: str
  age: int
  primary_interest: str
  activity_logs: List[str] = field(default_factory=list)


# =====================================================================
# STEP 2: DATA GENERATOR & PIPELINE CLASS
# =====================================================================


class DataLoader:
  """Handles synthetic data creation, preprocessing, and matrix transformations."""

  def __init__(self, num_users: int = 250, seed: int = 42):
    self.num_users = num_users
    self.seed = seed
    np.random.seed(seed)

    self.interests_pool = [
        'technology',
        'fitness',
        'music',
        'gaming',
        'fashion',
    ]
    self.actions_pool = {
        'technology': [
            'watched AI talk',
            'bought headphones',
            'read tech blog',
        ],
        'fitness': ['logged 10k steps', 'bought protein', 'completed yoga'],
        'music': [
            'listened to rock',
            'saved jazz playlist',
            'bought concert ticket',
        ],
        'gaming': ['streamed Twitch', 'bought GPU', 'played RPG game'],
        'fashion': [
            'browsed sneakers',
            'saved summer lookbook',
            'bought jacket',
        ],
    }

  def generate_users(self) -> List[UserProfile]:
    """Generates a synthetic list of UserProfile instances."""
    first_names = [
        'Alex',
        'Jordan',
        'Taylor',
        'Morgan',
        'Sam',
        'Chris',
        'Pat',
        'Casey',
    ]
    last_names = [
        'Smith',
        'Johnson',
        'Williams',
        'Brown',
        'Jones',
        'Miller',
        'Davis',
    ]
    interest_weights = [0.35, 0.25, 0.20, 0.12, 0.08]

    users = []
    for i in range(1, self.num_users + 1):
      name = f'{np.random.choice(first_names)} {np.random.choice(last_names)}'
      age = int(np.random.normal(loc=29, scale=6))
      age = max(18, min(65, age))
      primary = np.random.choice(self.interests_pool, p=interest_weights)

      num_activities = np.random.randint(3, 8)
      logs = []
      for _ in range(num_activities):
        if np.random.rand() < 0.70:
          act = np.random.choice(self.actions_pool[primary])
        else:
          rand_interest = np.random.choice(self.interests_pool)
          act = np.random.choice(self.actions_pool[rand_interest])
        logs.append(act)

      users.append(
          UserProfile(
              user_id=i,
              name=name,
              age=age,
              primary_interest=primary,
              activity_logs=logs,
          )
      )
    return users

  def to_dataframe(self, users: List[UserProfile]) -> pd.DataFrame:
    """Converts user profiles list into a clean Pandas DataFrame."""
    data = []
    for u in users:
      for act in u.activity_logs:
        data.append({
            'user_id': u.user_id,
            'name': u.name,
            'age': u.age,
            'primary_interest': u.primary_interest,
            'activity': act,
        })
    df = pd.DataFrame(data)
    df['activity'] = df['activity'].str.strip().str.lower()
    return df.drop_duplicates()


# =====================================================================
# STEP 3: STATISTICAL ANALYSIS CLASS (SCIPY)
# =====================================================================


class StatisticalAnalyzer:
  """Performs hypothesis testing and distribution fitting using SciPy."""

  @staticmethod
  def chi_square_test(
      df: pd.DataFrame,
  ) -> Tuple[float, float, int, pd.DataFrame]:
    """Chi-Square Test of Independence between Interest and Activity."""
    contingency_table = pd.crosstab(df['primary_interest'], df['activity'])
    chi2, p_val, dof, _ = chi2_contingency(contingency_table)
    return chi2, p_val, dof, contingency_table

  @staticmethod
  def fit_age_distribution(df: pd.DataFrame) -> Tuple[float, float]:
    """Fits a Gaussian normal distribution to user ages using SciPy."""
    unique_users = df[['user_id', 'age']].drop_duplicates()
    return norm.fit(unique_users['age'])


# =====================================================================
# STEP 4: RECOMMENDATION ENGINE (SCIPY SPATIAL SIMILARITY & OOP)
# =====================================================================


class ContentRecommendationEngine:
  """Hybrid Recommendation Engine combining category matching & SciPy Cosine Similarity."""

  def __init__(self, df: pd.DataFrame):
    self.df = df
    self.user_item_matrix = pd.crosstab(df['user_id'], df['activity'])
    self.user_ids = self.user_item_matrix.index.tolist()
    self._compute_similarity_matrix()

  def _compute_similarity_matrix(self):
    """Computes pair-wise Cosine Similarity matrix across users."""
    distance_matrix = pdist(self.user_item_matrix.values, metric='cosine')
    similarity_array = 1.0 - squareform(distance_matrix)
    self.similarity_df = pd.DataFrame(
        similarity_array, index=self.user_ids, columns=self.user_ids
    )

  def recommend_for_user(self, user_id: int, top_n: int = 3) -> Dict:
    """Generates hybrid content recommendations for a target user."""
    if user_id not in self.user_ids:
      return {'error': f'User ID {user_id} not found.'}

    user_info = self.df[self.df['user_id'] == user_id].iloc[0]
    user_interest = user_info['primary_interest']

    sim_scores = self.similarity_df.loc[user_id].drop(user_id)
    similar_users = sim_scores.sort_values(ascending=False).head(3).index.tolist()

    target_activities = set(
        self.df[self.df['user_id'] == user_id]['activity']
    )
    similar_activities = set(
        self.df[self.df['user_id'].isin(similar_users)]['activity']
    )

    recommended_collaborative = list(similar_activities - target_activities)[
        :top_n
    ]

    return {
        'user_name': user_info['name'],
        'primary_interest': user_interest,
        'similar_users_ids': similar_users,
        'collaborative_recommendations': recommended_collaborative,
    }


# =====================================================================
# STEP 5: EXECUTION & VISUALIZATION PIPELINE
# =====================================================================

# 1. Generate and preprocess dataset
loader = DataLoader(num_users=250, seed=42)
users_list = loader.generate_users()
df = loader.to_dataframe(users_list)

# 2. Run Statistical Tests
chi2, p_val, dof, contingency = StatisticalAnalyzer.chi_square_test(df)
mu_age, std_age = StatisticalAnalyzer.fit_age_distribution(df)

# 3. Generate Recommendations
engine = ContentRecommendationEngine(df)
recs = engine.recommend_for_user(user_id=5, top_n=3)

# Print Summary Outputs
print('===================================================================')
print('   PERSONALIZED AI CONTENT GENERATOR - HACKATHON OUTPUT')
print('===================================================================')
print(f'Total Users: {len(users_list)} | Total Interactions: {df.shape[0]}')
print(f'Chi-Square Statistic (χ²): {chi2:.2f} | P-Value: {p_val:.4e}')
print(f'Age Fit (SciPy Normal): Mean = {mu_age:.1f} yrs, Std = {std_age:.1f} yrs')
print(f'Sample Output (User #5): {recs}')
print('===================================================================\n')

# 4. Multi-Panel Visualizations Dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Subplot 1: User Primary Interest Distribution
unique_users_df = df[['user_id', 'primary_interest']].drop_duplicates()
sns.countplot(
    data=unique_users_df,
    x='primary_interest',
    ax=axes[0, 0],
    palette='viridis',
)
axes[0, 0].set_title(
    '1. User Primary Interest Distribution', fontsize=12, fontweight='bold'
)
axes[0, 0].set_xlabel('Interest Category')
axes[0, 0].set_ylabel('User Count')

# Subplot 2: Age Distribution with SciPy Gaussian Normal Overlay
sns.histplot(
    data=df[['user_id', 'age']].drop_duplicates(),
    x='age',
    kde=True,
    ax=axes[0, 1],
    color='teal',
    stat='density',
)
x_axis = np.linspace(15, 55, 100)
axes[0, 1].plot(
    x_axis,
    norm.pdf(x_axis, mu_age, std_age),
    'r--',
    linewidth=2,
    label=f'SciPy Normal Fit (μ={mu_age:.1f})',
)
axes[0, 1].set_title(
    '2. User Age Distribution & Gaussian Fit', fontsize=12, fontweight='bold'
)
axes[0, 1].set_xlabel('Age')
axes[0, 1].legend()

# Subplot 3: User Activity Crosstab Heatmap
sns.heatmap(contingency, cmap='YlGnBu', ax=axes[1, 0], cbar=True)
axes[1, 0].set_title(
    '3. Activity Intensity Heatmap by Interest (Crosstab Matrix)',
    fontsize=12,
    fontweight='bold',
)
axes[1, 0].set_xlabel('Activity Log')
axes[1, 0].set_ylabel('Primary Interest')

# Subplot 4: SciPy Cosine Similarity Matrix (Top 10 Users)
top_10_sim = engine.similarity_df.iloc[:10, :10]
sns.heatmap(
    top_10_sim,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    ax=axes[1, 1],
    cbar=True,
)
axes[1, 1].set_title(
    '4. SciPy Cosine Similarity Matrix (Top 10 Users)',
    fontsize=12,
    fontweight='bold',
)
axes[1, 1].set_xlabel('User ID')
axes[1, 1].set_ylabel('User ID')

plt.tight_layout()
plt.show()