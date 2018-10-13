import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('recoded.csv')

features = [column for column in df.columns if column != 'cover_type']
target = ['cover_type']

X = df[features]
y = df[target]
X_discard, X_keep, y_discard, y_keep = train_test_split(X, y, test_size=0.25, random_state=42)

df_sample = pd.concat([X_keep, y_keep], axis=1)

df_sample.to_csv('sampled.csv', index=False)
