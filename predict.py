import pandas as pd
import pickle
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV, train_test_split

df = pd.read_csv('sampled.csv')

features = [column for column in df.columns if column != 'cover_type']
target = ['cover_type']

X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

if not Path('model.pkl').is_file():
    param_grid = {'criterion': ['gini', 'entropy'],
                  'max_features': [None, 'sqrt', 'log2'],
                  'max_depth': [None, *[i + 3 for i in range(5)]]}

    # model = GridSearchCV(RandomForestClassifier(n_estimators=100), param_grid, cv=5, verbose=100)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
else:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

predictions = model.predict(X_test)

print('Predictions:')
print()

for pair in zip(predictions, y_test['cover_type']):
    print(pair)

print()
print('Overall accuracy:', accuracy_score(predictions, y_test['cover_type']))
