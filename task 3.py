import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Datasets/Dataset  (1).csv"
df = pd.read_csv(file_path)

# Group by City and Price Range
city_price_counts = df.groupby(['City', 'Price range']).size().unstack(fill_value=0)

# Calculate percentages
city_price_percentages = city_price_counts.div(city_price_counts.sum(axis=1), axis=0) * 100

# Display top 5 cities as example
print("Price Range Count (Top 5 Cities):")
print(city_price_counts.head())

print("\nPrice Range Percentage (Top 5 Cities):")
print(city_price_percentages.round(2).head())

# Optional: Stacked bar chart for top N cities by total restaurant count
top_cities = df['City'].value_counts().head(10).index
top_cities_data = city_price_counts.loc[top_cities]

# Plotting
top_cities_data.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='tab20c')
plt.title('Price Range Distribution by City (Top 10 Cities)')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.legend(title='Price Range')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
