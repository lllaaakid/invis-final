import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = '/Users/tangxinmeng/Desktop/data/GDP_total/GDP_total.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Removing rows with missing GDP values
cleaned_data = data.dropna(subset=['1998 [YR1998]', '2010 [YR2010]', '2022 [YR2022]'])

# Extracting the cleaned GDP data for the years 1998, 2010, and 2022
gdp_1998_cleaned = cleaned_data['1998 [YR1998]']
gdp_2010_cleaned = cleaned_data['2010 [YR2010]']
gdp_2022_cleaned = cleaned_data['2022 [YR2022]']
countries_cleaned = cleaned_data['Country Name']

num_countries = len(countries_cleaned)
colors = ['#' + format(int(255 - i*255/num_countries), '02x')*3 for i in range(num_countries)]

# Creating pie charts for each year with the cleaned data
fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# Pie chart for 1998
ax[0].pie(gdp_1998_cleaned, labels=countries_cleaned, autopct='%1.1f%%', startangle=140, colors=colors)
ax[0].set_title('GDP Distribution in 1998')

# Pie chart for 2010
ax[1].pie(gdp_2010_cleaned, labels=countries_cleaned, autopct='%1.1f%%', startangle=140, colors=colors)
ax[1].set_title('GDP Distribution in 2010')

# Pie chart for 2022
ax[2].pie(gdp_2022_cleaned, labels=countries_cleaned, autopct='%1.1f%%', startangle=140, colors=colors)
ax[2].set_title('GDP Distribution in 2022')

# Display the pie charts
plt.tight_layout()
plt.show()