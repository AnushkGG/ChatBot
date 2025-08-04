# backend/train_model.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset (download from Kaggle)
data = pd.read_csv("crop_recommendation.csv")

# Features & target
X = data.drop("label", axis=1)
y = data["label"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as crop_model.pkl")
