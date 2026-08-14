import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# Fetch data from the API
url = "https://gbfs.baywheels.com/gbfs/en/station_status.json"
response = requests.get(url)
data = response.json()
# Convert to DataFrame
stations = data['data']['stations']
df = pd.DataFrame(stations)
low_bikes = df.nsmallest(20, 'num_bikes_available')
high_bikes = df.nlargest(20, 'num_bikes_available')
# Low Bike Stations Visualization
plt.figure(figsize=(10, 5))
sns.barplot(x=low_bikes['station_id'], y=low_bikes['num_bikes_available'], palette='Reds_r')
plt.xticks(rotation=90)
plt.xlabel("Station ID")
plt.ylabel("Available Bikes")
plt.title("Top 20 Stations with Too Few Bikes")

plt.show()  # Show image in the notebook
plt.savefig("low_bike_stations.png")  # Save image
plt.close()
# High Bike Stations Visualization
plt.figure(figsize=(10, 5))
sns.barplot(x=high_bikes['station_id'], y=high_bikes['num_bikes_available'], palette='Blues')
plt.xticks(rotation=90)
plt.xlabel("Station ID")
plt.ylabel("Available Bikes")
plt.title("Top 20 Stations with Too Many Bikes")

plt.show()  # Show image in the notebook
plt.savefig("high_bike_stations.png")  # Save image
plt.close()
# System Health Visualization
plt.figure(figsize=(12, 6))
sns.histplot(df['num_bikes_available'], bins=20, kde=True, color='green')
plt.xlabel("Number of Available Bikes")
plt.ylabel("Frequency")
plt.title("System Health - Distribution of Available Bikes")

plt.show()
plt.savefig("system_health.png")
plt.close()