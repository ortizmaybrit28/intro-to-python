# ANALYZING AIR QUALITY DATA
# Part 1.1: LOAD THE DATA
import pandas as pd
file_name = 'global_air_quality.csv' 
df = pd.read_csv(file_name)
print(df)


# Part 1.2: MAKE A NEW COLUMN
import pandas as pd
file_name = 'global_air_quality.csv'
df['PM25_Value'] = df['FactValueNumeric']
print(df[['FactValueNumeric', 'PM25_Value']])


# Part 1.3: CALCULATE AVERAGE PM2.5 CONCENTRATION
import pandas as pd
file_name = 'global_air_quality.csv' 
df['PM25_Value'] = df['FactValueNumeric']
average_pm25 = df.groupby('ParentLocation')['PM25_Value'].mean().reset_index()
average_pm25.rename(columns={'PM25_Value': 'Average_PM25'}, inplace=True)
df = pd.merge(df, average_pm25, on='ParentLocation')
print(df[['Location', 'ParentLocation', 'PM25_Value', 'Average_PM25']])


# Part 1.4: ANALYZE DATA
import pandas as pd
file_name = 'global_air_quality.csv'
df = pd.read_csv(file_name)
df['PM25_Value'] = df['FactValueNumeric']
average_pm25 = df.groupby('ParentLocation')['PM25_Value'].mean().reset_index()
average_pm25.rename(columns={'PM25_Value': 'Average_PM25'}, inplace=True)
max_pollution = average_pm25.loc[average_pm25['Average_PM25'].idxmax()]
print(f"The continent with the highest average PM2.5 concentration is: {max_pollution['ParentLocation']} "
      f"with an average value of {max_pollution['Average_PM25']:.2f}.")
df = pd.merge(df, average_pm25, on='ParentLocation')
print(df[['Location', 'ParentLocation', 'PM25_Value', 'Average_PM25']])
'''
I was more suprised that the code work! But yes, this is an itneresting statistic that 
the continent with the highest average PM2.5 concentration happens to be in the 
Eastern Mediterranean, in Afghanistan. Could aridiness and humidity have a correlation
to the PM2.5 concentration? Eastern Mediterranean tends to be hot and humid/arid.
'''


# Part 1.5: SAVE THE PROCESSED DATA
output_df = df[['Location', 'ParentLocation', 'PM25_Value', 'Average_PM25']]
output_file_name = 'updated_PM25_data.csv'
output_df.to_csv(output_file_name, index=False)
print(f"The updated DataFrame has been saved as '{output_file_name}'.")



# PLANETS, PLANETS, PLANETS!
# Part 2.1: CREATE A SCATTER PLOT
import seaborn as sns
import matplotlib.pyplot as plt

planets = sns.load_dataset('planets')
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    data=planets,
    x='orbital_period',
    y='mass',
    hue='method',
    alpha=0.9 
)
plt.xscale('log')
plt.yscale('log') 
plt.title('Relationship Between Orbital Period and Mass of Exoplanets', fontsize=14)
plt.xlabel('Orbital Period (days)', fontsize=12)
plt.ylabel('Mass (Jupiter masses)', fontsize=12)
plt.legend(title='Discovery Methods', bbox_to_anchor=(1, 1), loc='upper left')
plt.tight_layout()
plt.show()


# Part 2.2: CREATE A BAR CHART
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

planets = sns.load_dataset('planets')
planets = planets.dropna(subset=['method', 'year'])
discovery_counts = planets.groupby(['year', 'method']).size().reset_index(name='count')
pivot_table = discovery_counts.pivot(index='year', columns='method', values='count').fillna(0)
pivot_table.plot(
    kind='bar', 
    stacked=True, 
    figsize=(12, 6), 
    cmap='viridis',
    edgecolor='black'
)
plt.title('Total Number of Exoplanets Discovered per Year by the Discovery Methods', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Exoplanets', fontsize=12)
plt.legend(title='Discovery Method', bbox_to_anchor=(1, 1), loc='upper left')
plt.tight_layout()
plt.show()

