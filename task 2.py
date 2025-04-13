import pandas as pd

# Load the dataset
file_path = "Datasets/Dataset  (1).csv"
df = pd.read_csv(file_path)

# 1. City with the highest number of restaurants
city_counts = df['City'].value_counts()
city_most_restaurants = city_counts.idxmax()
count_most_restaurants = city_counts.max()

# 2. Average rating for restaurants in each city
average_ratings_by_city = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

# 3. City with the highest average rating
city_highest_avg_rating = average_ratings_by_city.idxmax()
highest_avg_rating = average_ratings_by_city.max()

# Display results
print("City with most restaurants:", city_most_restaurants, "-", count_most_restaurants)
print("\nTop 5 Cities by Average Rating:\n", average_ratings_by_city.head())
print("\nCity with highest average rating:", city_highest_avg_rating, "-", highest_avg_rating)
