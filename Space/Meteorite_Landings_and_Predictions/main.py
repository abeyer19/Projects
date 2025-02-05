# Dataset link -> https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data

# Import packages
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import seaborn as sns


# --- Testing / Tinkering ---
# Import dataset
meteors = pd.read_csv('https://raw.githubusercontent.com/abeyer19/Projects/refs/heads/main/Space/Meteorite_Landings_and_Predictions/Meteorite_Landings_20250128.csv')


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

# Show meteorite_graphs
#meteorite_graphs(meteors)


# --- Predictions ---
# Create simulations based on location and mass of meteorites

# Geo Locations Groupings
# North America
n_america_lat = (25, 70)
n_america_long = (-170, -50)

# South America
s_america_lat = (-55, 25)
s_america_long = (-80, -35)

# Europe
euro_lat = (35, 70)
euro_long = (-10, 40)

# Africa
africa_lat = (-35, 35)
africa_long = (-17, 50)

# Asia
asia_lat = (25, 70)
asia_long = (40, 180)

# Australia
australia_lat = (-55, -10)
australia_long = (110, 180)

# Artic
artic_lat = (70, 90)
artic_long = (-180, 180)

# Counts of meteorites in each region
n_america_count = meteors[(meteors['reclat'] >= n_america_lat[0]) & (meteors['reclat'] <= n_america_lat[1]) & (meteors['reclong'] >= n_america_long[0]) & (meteors['reclong'] <= n_america_long[1])].shape[0]
s_america_count = meteors[(meteors['reclat'] >= s_america_lat[0]) & (meteors['reclat'] <= s_america_lat[1]) & (meteors['reclong'] >= s_america_long[0]) & (meteors['reclong'] <= s_america_long[1])].shape[0]
euro_count = meteors[(meteors['reclat'] >= euro_lat[0]) & (meteors['reclat'] <= euro_lat[1]) & (meteors['reclong'] >= euro_long[0]) & (meteors['reclong'] <= euro_long[1])].shape[0]
africa_count = meteors[(meteors['reclat'] >= africa_lat[0]) & (meteors['reclat'] <= africa_lat[1]) & (meteors['reclong'] >= africa_long[0]) & (meteors['reclong'] <= africa_long[1])].shape[0]
asia_count = meteors[(meteors['reclat'] >= asia_lat[0]) & (meteors['reclat'] <= asia_lat[1]) & (meteors['reclong'] >= asia_long[0]) & (meteors['reclong'] <= asia_long[1])].shape[0]
australia_count = meteors[(meteors['reclat'] >= australia_lat[0]) & (meteors['reclat'] <= australia_lat[1]) & (meteors['reclong'] >= australia_long[0]) & (meteors['reclong'] <= australia_long[1])].shape[0]
artic_count = meteors[(meteors['reclat'] >= artic_lat[0]) & (meteors['reclat'] <= artic_lat[1]) & (meteors['reclong'] >= artic_long[0]) & (meteors['reclong'] <= artic_long[1])].shape[0]

print(meteors.count())
print(n_america_count)
print(s_america_count)
print(euro_count)
print(africa_count)
print(asia_count)
print(australia_count)
print(artic_count)
print(n_america_count + s_america_count + euro_count + africa_count + asia_count + australia_count + artic_count)


    # 1. Where are the biggest ones going to hit?
    # 2. Where is the most highly condensed area where they will hit
    # 3. Show visualization of simulations in real time (if possible)