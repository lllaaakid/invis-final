
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from a CSV file
gdp_growth_data = pd.read_csv('/Users/tangxinmeng/Desktop/data/GDP_growth/GDP_growth.csv', index_col='Country Name')

# Drop the 'Country Code' column as it's not needed for the heatmap
gdp_growth_data.drop('Country Code', axis=1, inplace=True)

# Set the context for the plot to ensure it is legible
sns.set_context('talk', font_scale=0.8)

# Create the heatmap with a diverging color palette
plt.figure(figsize=(18, 8))
sns.heatmap(gdp_growth_data, cmap='RdBu', center=0, annot=False, fmt='.1f',
            linewidths=.5, cbar_kws={'shrink': .5, 'label': 'GDP Per Capita Growth (%)'})

# Customize the plot to make it more informative and appealing
plt.xticks(rotation=90)  # Rotate x-axis labels for better legibility
plt.yticks(rotation=0)  # Ensure y-axis labels are horizontal for readability
plt.title('Heatmap of GDP Per Capita Growth (%) from 1998 to 2022')
plt.xlabel('Year')
plt.ylabel('Country')

# Remove the axes spines if desired
sns.despine()

# Show the plot
plt.tight_layout()
plt.show()