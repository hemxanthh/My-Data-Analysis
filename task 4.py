import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Datasets/Dataset  (1).csv")

# 1. Percentage of restaurants offering online delivery
online_delivery_counts = df['Has Online delivery'].value_counts()
online_delivery_percentage = (online_delivery_counts / len(df)) * 100

# 2. Average ratings comparison
avg_rating_by_delivery = df.groupby('Has Online delivery')['Aggregate rating'].mean()

# --- Visualization ---

# Pie chart for delivery availability
plt.figure(figsize=(6, 6))
plt.pie(online_delivery_percentage, labels=online_delivery_percentage.index,
        autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=140)
plt.title('Percentage of Restaurants Offering Online Delivery')
plt.axis('equal')
plt.show()

# Bar chart for average rating comparison
plt.figure(figsize=(6, 4))
bars = plt.bar(avg_rating_by_delivery.index, avg_rating_by_delivery.values, color=['#ff9999','#66b3ff'])
plt.title('Average Ratings: Online Delivery vs No Delivery')
plt.ylabel('Average Rating')
plt.ylim(0, 5)

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 2), ha='center', va='bottom')

plt.tight_layout()
plt.show()
