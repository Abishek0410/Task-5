import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales.csv')

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)
if 'Region' in df.columns and 'Sales' in df.columns:
    region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    print("\nTotal Sales by Region:")
    print(region_sales)

    region_sales.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Total Sales by Region")
    plt.ylabel("Total Sales")
    plt.xlabel("Region")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if 'Product' in df.columns and 'Sales' in df.columns:
    product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
    print("\nTotal Sales by Product:")
    print(product_sales)

    product_sales.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title("Total Sales by Product")
    plt.ylabel("Total Sales")
    plt.xlabel("Product")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
print("\nShape of DataFrame:", df.shape)
print("Columns:", list(df.columns))
print("\nBasic data insights generated successfully ✅")
