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

# 1. OOP Data Architecture
@dataclass
class UserProfile:
    user_id: int
    name: str
    age: int
    primary_interest: str
    activity_logs: List[str] = field(default_factory=list)

# 2. Data Generator & Pipeline Class
class DataLoader:
    def __init__(self, num_users: int = 250, seed: int = 42):
        self.num_users = num_users
        self.seed = seed
        np.random.seed(seed)
        self.interests_pool = ['technology', 'fitness', 'music', 'gaming', 'fashion']
        self.actions_pool = {
            'technology': ['watched AI talk', 'bought headphones', 'read tech blog'],
            'fitness': ['logged 10k steps', 'bought protein', 'completed yoga'],
            'music': ['listened to rock', 'saved jazz playlist', 'bought concert ticket'],
            'gaming': ['streamed Twitch', 'bought GPU', 'played RPG game'],
            'fashion': ['browsed sneakers', 'saved summer lookbook', 'bought jacket']
        }

    def generate_users(self) -> List[UserProfile]:
        first_names = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Sam', 'Chris', 'Pat', 'Casey']
        last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis']
        interest_weights = [0.35, 0.25, 0.20, 0.12, 0.08]
        users = []
        for i in range(1, self.num_users + 1):
            name = f"{np.random.choice(first_names)} {np.random.choice(last_names)}"
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
            users.append(UserProfile(user_id=i, name=name, age=age, primary_interest=primary, activity_logs=logs))
        return users

    def to_dataframe(self, users: List[UserProfile]) -> pd.DataFrame:
        data = []
        for u in users:
            for act in u.activity_logs:
                data.append({
                    'user_id': u.user_id,
                    'name': u.name,
                    'age': u.age,
                    'primary_interest': u.primary_interest,
                    'activity': act
                })
        df = pd.DataFrame(data)
        df['activity'] = df['activity'].str.strip().str.lower()
        return df.drop_duplicates()

# Generate and verify initial dataset
loader = DataLoader(num_users=250, seed=42)
users_list = loader.generate_users()
df = loader.to_dataframe(users_list)
print(f"Generated {len(users_list)} users with {df.shape[0]} interaction records.")
print(df.head())