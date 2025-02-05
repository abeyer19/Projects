# Dataset link -> https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data

# Import packages
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import seaborn as sns


# --- Testing / Tinkering ---
# Import dataset
df = pd.read_csv('https://raw.githubusercontent.com/abeyer19/Projects/refs/heads/main/Space/Meteorite_Landings_and_Predictions/Meteorite_Landings_20250128.csv')


# --- Real Analysis ---
def meteorite_graphs(df):
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
        # 2. Histogram of sizes, y in log scale to show outliers
    sns.histplot(df, 
                x='mass (lbs)', 
                bins=100, 
                stat='count', 
                ).set_yscale('log')
    plt.show()
        # 3. TODO: Bar charts of nametypes


    # Visual current data on geomap of globe using reclat and reclong
        # 1. Interactive map showing each point on the map
            # a. Increase in either size or decrease color oppacity for mass
    fig = px.scatter_geo(df, 
                        lat="reclat", 
                        lon="reclong",
                        #animation_frame="year", 
                        opacity= 1, 
                        size= "mass (g)",
                        projection="natural earth",
                        hover_data=["mass (g)", "recclass", "year"]).update_geos(showcoastlines=True, 
                                    coastlinecolor="black",
                                    showland=True, 
                                    landcolor="black",)
    fig.show()
        # 3. TODO: Create seperate scatter_geo for each continent

# Create simulations based on location and mass of meteorites
    # 1. Where are the biggest ones going to hit?
    # 2. Where is the most highly condensed area where they will hit
    # 3. Show visualization of simulations in real time (if possible)