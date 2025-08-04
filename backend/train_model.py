import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the dataset with proper encoding
df = pd.read_csv("backend/crop_recommendation.csv", encoding="latin1")

# Features and target
X = df.drop('label', axis=1)  # Features: N, P, K, temp, humidity, etc.
y = df['label']               # Target: Crop label

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the model
with open("backend/crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as crop_model.pkl")
