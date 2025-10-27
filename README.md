Task 5: Data Analysis on CSV Files

Objective

To analyze a CSV file containing sales data using Python. The goal is to clean, process, and visualize the data to identify insights such as total sales by region and product using Pandas and Matplotlib.

Tools Used:

Python 3 – Programming language
Pandas – Data manipulation and cleaning
Matplotlib – Data visualization
Google Colab – Code execution environment
Steps Performed

1. Import Libraries
   Imported `pandas` and `matplotlib.pyplot` for data handling and visualization.

2. Load Dataset
   Loaded `sales.csv` using `pd.read_csv()` and viewed sample rows with `df.head()`.

3. Explore Data
   Used `df.info()` and `df.describe()` to understand column types and key statistics.

4. Handle Missing Values
   Checked for missing data using `df.isnull().sum()` and replaced numeric nulls with the mean using `df.fillna()`.

5. Analyze and Visualize Sales

    Grouped and summed sales by Region and Product using `groupby()` and `sum()`.
    Plotted bar charts to visualize total sales across regions and products.

6.Additional Insights
   Displayed dataset shape and column names to confirm structure.

Results and Conclusion

The dataset was successfully cleaned, analyzed, and visualized.
Insights showed how sales varied by region and product.
This task demonstrates a complete data analysis process using Python — from loading and cleaning data to summarizing and visualizing results.
