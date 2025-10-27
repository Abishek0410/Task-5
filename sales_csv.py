import pandas as pd

data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B'],
    'Sales': [100, 150, 120, 200, 130, 180, 110, 160],
    'Date': ['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20', '2023-01-25', '2023-01-30', '2023-02-01']
}

df = pd.DataFrame(data)
df.to_csv('sales.csv', index=False)

print("sales.csv file created successfully.")
