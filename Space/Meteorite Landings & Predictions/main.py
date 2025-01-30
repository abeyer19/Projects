# Dataset link -> https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data


# Import packages
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import seaborn as sns


# --- Testing / Tinkering ---
# Import dataset
df = pd.read_csv('https://raw.githubusercontent.com/abeyer19/Projects/refs/heads/main/Space/Meteorite%20Landings%20%26%20Predictions/Meteorite_Landings_20250128.csv')

print(df['mass (g)'].max())


# --- Real Analysis ---
# Replace nan's with 0
df['mass (g)'] = df['mass (g)'].fillna(0)
# Add column to convert mass (g) to mass (lbs)
df['mass (lbs)'] = round(df['mass (g)'] * 0.00220462262, 2)
# Change columns to numeric
df['mass (g)'] = pd.to_numeric(df['mass (g)'])
df['mass (lbs)'] = pd.to_numeric(df['mass (lbs)'])


# Understand statistics
    # 1. Basic statistics
print(df.describe())
    # 2. Histogram of sizes
sns.histplot(df, 
             x='mass (lbs)', 
             bins=100, 
             binrange=(-2.5,df['mass (lbs)'].mean()), 
             stat='probability',)
plt.show()

sns.histplot(df, 
             x='mass (lbs)', 
             bins=100, 
             binrange=(1000,df['mass (lbs)'].max()), 
             stat='probability',)             

plt.show()
    # 3. Bar charts of nametypes

# Visual current data on geomap of globe using reclat and reclong
    # 1. Interactive map showing each point on the map
    # 2. Increase in either size or decrease color oppacity for mass
fig = px.scatter_geo(df, 
                     lat="reclat", 
                     lon="reclong",
                     #animation_frame="year", 
                     opacity= 1, 
                     size= "mass (g)",
                     projection="natural earth",)
fig.show()

# Create simulations based on location and mass of meteorites
    # 1. Where are the biggest ones going to hit?
    # 2. Where is the most highly condensed area where they will hit
    # 3. Show visualization of simulations in real time (if possible)