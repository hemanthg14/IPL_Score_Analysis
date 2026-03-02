import pandas as pd

print("Loading IPL Dataset...")

# Read CSV File
data = pd.read_csv('ipl.csv')

# Display first 5 rows
print("\nFirst 5 Records:")
print(data.head())

# Total Runs scored by each Team
total_runs = data.groupby('Team')['Runs'].sum()
print("\nTotal Runs by Each Team:")
print(total_runs)

# Average Runs scored by each Team
average_runs = data.groupby('Team')['Runs'].mean()
print("\nAverage Runs by Each Team:")
print(average_runs)

# Highest Runs scored by each Team
highest_runs = data.groupby('Team')['Runs'].max()
print("\nHighest Runs by Each Team:")
print(highest_runs)

print("\nIPL Score Analysis Completed!")