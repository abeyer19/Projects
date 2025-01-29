# Dataset link -> https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data


# Import packages
import pandas as pd


# --- Testing / Tinkering ---
df = pd.read_csv('https://raw.githubusercontent.com/abeyer19/Projects/refs/heads/main/Space/Meteorite%20Landings%20%26%20Predictions/Meteorite_Landings_20250128.csv')

print(df[df['mass (g)'] == df['mass (g)'].max()])


# --- Real Analysis ---
# Add column to convert mass (g) to lbs
df['mass (lbs)'] = round(df['mass (g)'] * 0.00220462262, 2)
print(df.columns)

# Understand statistics
    # 1. Basic statistics
    # 2. Histogram of sizes
    # 3. Bar charts of nametypes

# Visual current data on geomap of globe using reclat and reclong
    # 1. Interactive map showing each point on the map
    # 2. Increase in either size or decrease color oppacity for mass

# Create simulations based on location and mass of meteorites
    # 1. Where are the biggest ones going to hit?
    # 2. Where is the most highly condensed area where they will hit
    # 3. Show visualization of simulations in real time (if possible)
    # 4. 