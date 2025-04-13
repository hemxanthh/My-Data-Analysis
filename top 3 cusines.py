# Split the cuisines into individual entries and count their occurrences
cuisine_counts = df['Cuisines'].dropna().str.split(', ').explode().value_counts()

# Display the top 10 most common cuisines
print("Top 10 Most Common Cuisines:\n", cuisine_counts.head(10))
