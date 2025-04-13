import pandas as pd
from fontTools.ttLib.tables.otTables import AATState

file_path = "Datasets/Dataset  (1).csv"
df = pd.read_csv(file_path)
print(df.head())

#finding the most common cuisines from the datasets
cuisine_count = df['Cuisines'].dropna().str.split(', ').explode().value_counts()
print("The most common Cuisines are",cuisine_count.head(10))

#findin the most 3 common cuisines
top_cuisines = cuisine_count.head(3)
total_restaurants = len(df)
top_cuisines_percentage = (top_cuisines / total_restaurants) * 100
print("The most common cuisines with their percentages are:")
print(top_cuisines_percentage)



city_counts = df['City'].value_counts()
top_city_by_count = city_counts.idxmax()

