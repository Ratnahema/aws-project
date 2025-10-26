import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample training data
# Demand ↑ → Price ↑, Inventory ↑ → Price ↓, Competitor Price influences moderately
data = pd.DataFrame({
    'demand': [0.2, 0.5, 0.8, 0.3, 0.9],
    'inventory': [90, 60, 20, 80, 10],
    'competitor_price': [80, 100, 120, 90, 140],
    'price': [85, 110, 155, 95, 180]
})

# Features and target
X = data[['demand', 'inventory', 'competitor_price']]
y = data['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model to disk
joblib.dump(model, 'smv_model.pkl')

print("✅ Model trained and saved successfully as smv_model.pkl")
