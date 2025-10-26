import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------
# Step 1: Create sample CSV
# -------------------------
csv_file = 'sample_data.csv'

if not os.path.exists(csv_file):
    print("Creating sample_data.csv ...")
    data = {
        'id': [1, 2, 3],
        'name': ['Lipstick', 'Foundation', 'Eyeliner'],
        'price': [399, 799, 299]
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)
    print("sample_data.csv created successfully!")
else:
    print("sample_data.csv already exists.")

# -------------------------
# Step 2: Load CSV Data
# -------------------------
print("\nLoading CSV data ...")
df = pd.read_csv(csv_file)
print("CSV loaded successfully.")

# -------------------------
# Step 3: Data Cleaning
# -------------------------
print("\nCleaning data ...")
df.dropna(inplace=True)                  # Remove missing values
df['price'] = df['price'].astype(int)    # Ensure price is integer
print("Data cleaned successfully.")

# -------------------------
# Step 4: Display Summary
# -------------------------
print("\nDataset Preview:")
print(df)

print("\nDataset Summary:")
print(df.describe())

# -------------------------
# Step 5: Generate Bar Chart
# -------------------------
print("\nGenerating bar chart ...")
plt.figure(figsize=(8,5))
plt.bar(df['name'], df['price'], color='skyblue')
plt.title('Product Price Comparison')
plt.xlabel('Product')
plt.ylabel('Price (₹)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
bar_chart_file = 'price_bar_chart.png'
plt.savefig(bar_chart_file)
plt.show()
print(f"Bar chart saved as '{bar_chart_file}'")

# -------------------------
# Step 6: Generate Pie Chart
# -------------------------
print("\nGenerating pie chart ...")
plt.figure(figsize=(6,6))
colors = ['#ff9999','#66b3ff','#99ff99']
plt.pie(df['price'], labels=df['name'], autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Product Price Distribution')
pie_chart_file = 'price_pie_chart.png'
plt.savefig(pie_chart_file)
plt.show()
print(f"Pie chart saved as '{pie_chart_file}'")

# -------------------------
# Step 7: Finish
# -------------------------
print("\nAll steps completed successfully!")
print("You now have:")
print(f"1. sample_data.csv")
print(f"2. {bar_chart_file}")
print(f"3. {pie_chart_file}")
