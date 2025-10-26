from flask import Flask, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = joblib.load('smv_model.pkl')

@app.route('/')
def home():
    # Example input data
    data = pd.DataFrame({
        'demand': [0.85, 0.45, 0.65],
        'inventory': [20, 70, 50],
        'competitor_price': [130, 95, 110]
    }, index=['AI Product 1', 'AI Product 2', 'AI Product 3'])

    # Predict prices
    prices = model.predict(data)
    data['recommended_price'] = [f"${p:.2f}" for p in prices]

    # Format for HTML
    table = data.reset_index().rename(columns={'index': 'product'}).to_dict(orient='records')

    return render_template('smv_index.html', table=table)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
