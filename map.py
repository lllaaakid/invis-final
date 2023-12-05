import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the shapefile
gdf = gpd.read_file('/Users/tangxinmeng/Desktop/data/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp')

# Load the updated GDP data
gdp_map_data = pd.read_csv('/Users/tangxinmeng/Desktop/data/GPD_map/GDP_map.csv')

# Rename the columns for easier merging
gdp_map_data.columns = ['country', 'country_code', 'gdp_2022']

# Correcting mismatched country names
name_mapping = {
    'Congo, Rep.': 'Republic of the Congo',
    'Egypt, Arab Rep.': 'Egypt',
    'Russian Federation': 'Russia',
    'United States': 'United States of America'
}
gdp_map_data['country'] = gdp_map_data['country'].replace(name_mapping)

# Merge the GDP data with the GeoDataFrame
# 'ADMIN' is the column in the shapefile that corresponds to country names
merged_gdf = gdf.merge(gdp_map_data, left_on='ADMIN', right_on='country', how='left')

# Plot the choropleth map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
# Plotting countries without data in light grey
gdf.plot(color='white', ax=ax)
# Plotting countries with GDP data
merged_gdf.dropna(subset=['gdp_2022']).plot(column='gdp_2022', ax=ax, legend=True,
                                            legend_kwds={'label': "GDP Per Capita (USD) in 2022",
                                                         'orientation': "vertical",
                                                         'shrink': 0.5},
                                            cmap='bone_r',
                                            )
# Add title and remove axis for a cleaner look
plt.title('Updated Choropleth Map of GDP Per Capita in 2022')
ax.set_axis_off()

# Display the map
plt.show()