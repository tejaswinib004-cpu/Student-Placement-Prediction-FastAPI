import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset

df = pd.read_csv("placements.csv")

# Features and target
X = df[['cgpa','iq']]
y = df['placement']

# Split
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model=LogisticRegression()

# Train
model.fit(X_train,y_train)

# Save model
joblib.dump(model,"placement_model.pkl")

print("Model Saved")