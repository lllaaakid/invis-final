
import pandas as pd

import matplotlib.pyplot as plt

# The file has been uploaded. Let's read it and then plot the chart line graphic
df = pd.read_csv('/Users/tangxinmeng/Desktop/data/GDP_per_capita/GDP_capita.csv', delimiter=',')

# Inspecting the first few rows of the dataframe to understand its structure
df.head()

# Plotting the chart line graphic for GDP per capita for each country over the years

# Dropping the 'Country Code' column as it's not needed for the plot
df.drop('Country Code', axis=1, inplace=True)

# Setting the 'Country Name' column as the index
df.set_index('Country Name', inplace=True)

# Transposing the dataframe for easier plotting
df_transposed = df.T

# Plotting
plt.figure(figsize=(50, 8))
for country in df_transposed.columns:
    x_values = df_transposed.index
    y_values = df_transposed[country]
    plt.plot(x_values, y_values, label=country, marker='o')
    # plt.plot(df_transposed.index, df_transposed[country], label=country)

plt.xlabel('Year')
plt.ylabel('GDP Per Capita (USD)')
plt.title('GDP Per Capita Over Time by Country')
plt.legend()
plt.xticks(rotation=0)
plt.grid(True)
plt.show()

