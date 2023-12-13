# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:59:43 2023

@author: arbab
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'/content/Climate.csv'
data = pd.read_csv(file_path)

# Select specific indicators for analysis
indicators_to_analyze = ['Renewable energy consumption (% of total final energy consumption)']

# Filter data for selected indicators
selected_data = data[data['Indicator Name'].isin(indicators_to_analyze)]

# Plot time trends for each country
plt.figure(figsize=(16, 10))
for country in selected_data['Country Name'].unique():
    country_data = selected_data[selected_data['Country Name'] == country]
    plt.plot(country_data.columns[2:], country_data.iloc[0, 2:], label=country)

plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Time Trends for Selected Indicators')
plt.legend()

# The y-axis limits are determined automatically

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'/content/Climate.csv'
data = pd.read_csv(file_path)

# Select specific indicators for analysis
indicators_to_analyze = ['Urban population (% of total population)']

# Filter data for selected indicators
selected_data = data[data['Indicator Name'].isin(indicators_to_analyze)]

# Plot time trends for each country
plt.figure(figsize=(16, 10))
for country in selected_data['Country Name'].unique():
    country_data = selected_data[selected_data['Country Name'] == country]
    plt.plot(country_data.columns[2:], country_data.iloc[0, 2:], label=country)

plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Time Trends for Selected Indicators')
plt.legend()

# The y-axis limits are determined automatically

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'/content/Climate.csv'
data = pd.read_csv(file_path)

# Select data for the specific indicators and country
indicators_to_plot = ['Renewable energy consumption (% of total final energy consumption)', 'Urban population (% of total population)']
selected_country = 'France'

# Filter data
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(indicators_to_plot))]

# Extract years and values for the bar chart
years = selected_data.columns[2:]
values1 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[0]].iloc[0, 2:]
values2 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[1]].iloc[0, 2:]

# Plot the bar chart
plt.figure(figsize=(12, 8))
bar_width = 0.35
bar1 = plt.bar(years, values1, width=bar_width, label=indicators_to_plot[0], color='blue')
bar2 = plt.bar(years, values2, width=bar_width, label=indicators_to_plot[1], color='green', bottom=values1)

plt.title(f'{selected_country} - Agricultural Land and Forest Area (1990-2020)')
plt.xlabel('Year')
plt.ylabel('Values')
plt.legend()
plt.grid(axis='y')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'/content/Climate.csv'
data = pd.read_csv(file_path)

# Select data for the specific indicators and country
indicators_to_plot = ['Renewable energy consumption (% of total final energy consumption)', 'Urban population (% of total population)']
selected_country = 'China'

# Filter data
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(indicators_to_plot))]

# Extract years and values for the bar chart
years = selected_data.columns[2:]
values1 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[0]].iloc[0, 2:]
values2 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[1]].iloc[0, 2:]

# Plot the bar chart
plt.figure(figsize=(12, 8))
bar_width = 0.35
bar1 = plt.bar(years, values1, width=bar_width, label=indicators_to_plot[0], color='blue')
bar2 = plt.bar(years, values2, width=bar_width, label=indicators_to_plot[1], color='green', bottom=values1)

plt.title(f'{selected_country} - Agricultural Land and Forest Area (1990-2020)')
plt.xlabel('Year')
plt.ylabel('Values')
plt.legend()
plt.grid(axis='y')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'/content/Climate.csv'
data = pd.read_csv(file_path)

# Select data for the specific indicators and country
indicators_to_plot = ['Renewable energy consumption (% of total final energy consumption)', 'Urban population (% of total population)']
selected_country = 'Indonesia'

# Filter data
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(indicators_to_plot))]

# Extract years and values for the bar chart
years = selected_data.columns[2:]
values1 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[0]].iloc[0, 2:]
values2 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[1]].iloc[0, 2:]

# Plot the bar chart
plt.figure(figsize=(12, 8))
bar_width = 0.35
bar1 = plt.bar(years, values1, width=bar_width, label=indicators_to_plot[0], color='blue')
bar2 = plt.bar(years, values2, width=bar_width, label=indicators_to_plot[1], color='green', bottom=values1)

plt.title(f'{selected_country} - Agricultural Land and Forest Area (1990-2020)')
plt.xlabel('Year')
plt.ylabel('Values')
plt.legend()
plt.grid(axis='y')
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/Climate.csv'
data = pd.read_csv(file_path)

# Select specific indicators for correlation matrix
selected_indicators = ['Renewable energy consumption (% of total final energy consumption)', 'Urban population (% of total population)']

# Filter data for selected indicators
selected_data = data[data['Indicator Name'].isin(selected_indicators)]

# Pivot the data
pivot_data = selected_data.pivot(index='Country Name', columns='Indicator Name', values='2020')

# Create a correlation matrix for selected indicators
correlation_matrix = pivot_data.corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Set the title
plt.title('Correlation Matrix for Selected Indicators')

# Show the plot
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Replace this with the actual path to your CSV file
file_path = '/content/Climate.csv'
data = pd.read_csv(file_path)

# Select countries and indicators of interest
selected_countries = ['China', 'Indonesia', 'France']
selected_indicators = ['Renewable energy consumption (% of total final energy consumption)', 'Urban population (% of total population)']

# Filter data for selected countries and indicators
selected_data = data[(data['Country Name'].isin(selected_countries)) & (data['Indicator Name'].isin(selected_indicators))]

# Set up bar positions and width
bar_positions = range(len(selected_countries))
bar_width = 0.35

# Create subplots
fig, ax = plt.subplots()

# Plot bars for each indicator and country
for i, indicator in enumerate(selected_indicators):
    for j, country in enumerate(selected_countries):
        subset_data = selected_data[(selected_data['Country Name'] == country) & (selected_data['Indicator Name'] == indicator)]
        ax.bar(bar_positions[j] + i * bar_width, subset_data.iloc[0, 2:], width=bar_width, label=f'{country} - {indicator}')

# Set labels and title
ax.set_xticks([pos + bar_width / 2 for pos in bar_positions])
ax.set_xticklabels(selected_countries)
ax.set_xlabel('Country')
ax.set_ylabel('Indicator Value')
ax.set_title('Bar Chart for Selected Indicators and Countries')

# Add legend
ax.legend()

# Show the plot
plt.show()

