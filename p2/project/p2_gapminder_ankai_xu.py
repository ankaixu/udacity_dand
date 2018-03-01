
# coding: utf-8

# # Investigate Gapminder World Data - Udacity Data Analyst Nanodegree Project
# ## Ankai Xu | February 14, 2018
# 
# ### Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# This is the final project for the Introduction to Data Analysis course that is part of the Udacity Data Analyst Nanodegree program. For this project, I have chosen to explore data from <a href=https://www.gapminder.org/data/>Gapminder World</a> on indicators relating to populations around the world tracked over time. Specifically, I will be investigating the following datasets, accessed on February 11th, 2018: 
# <ul>
# <li>Life expectancy (years), Version 2016 10 12</li>
# <li>Child mortality (0-5 year-olds dying per 1,000 born), Version 8</li>
# <li>Total health spending per person (US$)</li>
# </ul>
# 
# Below are the questions I'm interested in answering with my data analysis in this project. 
# 
# <ol>
# <li>How has the average life expectancy changed over time globally and in the United States?</li>
# <li>What is the distribution of life expectancies around the world today? Which countries have the lowest and highest life expectancies today? How does the United States compare?</li>
# <li>How has the average child mortality rate changed over time globally and in the United States?</li>
# <li>What is the distribution of child mortality rates around the world today? Which countries have the lowest and highest child mortality rates today? How does the United States compare?</li>
# <li>How has the average per capita health spending changed over time globally and in the United States</li>
# <li>What is the distribution of per capita health spend around the world today? Which countries have the lowest and highest per capita health spend today? How does the United States compare?</li>
# <li>Are there observable correlations between per capita health spending, life expectancy, and child mortality?</li> 
# </ol>
# 

# In[1]:


# import all necessary packages and set plotting defaults

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import seaborn as sns 
sns.set_style('whitegrid')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# In this section, I will assess the general characteristics of the data and clean the data. All data was first downloaded from the Gapminder World website and saved as .csv files using Excel. No data manipulation was performed in Excel.
# 
# ### Life Expectancy Data Assessment and Cleaning

# In[2]:


# Load life expectancy data and print out a few lines
life_exp = pd.read_csv('indicator_life_expectancy_at_birth.csv', encoding='mac_roman')
life_exp.head()


# In[3]:


# Assess the life expectancy data
life_exp.info()


# The life expectancy DataFrame is in wide format but I want it in long format for ease of comparing multiple indicators against east other. The presence of 999 entries indicates that completely blank rows were read during data import. Additionally, I can see from printing the first few lines of the DataFrame that certain countries have missing data. I will drop all rows containing any null values, including countries which may have partial data, for consistency of analysis when calculating global averages over time. I will also check for and remove any duplicated rows. I will then reshape the DataFrame into long format. 

# In[4]:


# Drop rows that contain missing values and determine if there are duplicate entries 
life_exp.dropna(axis=0, how='any', inplace=True)
sum(life_exp.duplicated())


# In[5]:


# Get table info after dropping missing values 
life_exp.info()


# In[6]:


# Unpivot the DataFrame from wide format to long format and clean up column names
life_exp_melt = pd.melt(life_exp, id_vars='Life expectancy', var_name='year', value_name='life_expectancy')
life_exp_melt.rename(columns={'Life expectancy':'country'},inplace=True)
life_exp_melt.head()


# In[7]:


# Get table info after melt operation
life_exp_melt.info()


# In[8]:


# Convert the data type of the "year" column from a string to an integer
life_exp_melt['year'] = life_exp_melt['year'].astype(int)


# In[9]:


# Get descriptive statistics
life_exp_melt.describe()


# The life expectancy DataFrame has been successfully cleaned and melted into long format and is ready for exploratory analysis to follow in the next section.

# ### Child Mortality Data Assessment and Cleaning

# In[10]:


# Load child mortality data and print out a few lines. 
child_mort = pd.read_csv('indicator_gapminder_under5mortality.csv', encoding='mac_roman')
child_mort.head()


# In[11]:


# Assess the child mortality data
child_mort.info()


# The child mortality DataFrame is also in wide format but I want it in long format for ease of comparing multiple indicators against east other. The presence of 999 entries indicates that completely blank rows were read during data import. Additionally, at least the last column is "Unnamed," indicating that one or more blank columns were read as well. I will first drop any null columns.

# In[12]:


# Drop columns that are completely missing values 
child_mort.dropna(axis=1, how='all', inplace=True)
child_mort.info()


# After dropping fully null columns, I can see that each country has at most 216 entries. I will drop all rows containing any null values, including countries which may have partial data, for consistency of analysis when calculating global averages over time. I will also check for and remove any duplicated rows. I will then reshape the DataFrame into long format.

# In[13]:


# Drop rows that contain missing values and determine if there are duplicate entries 
child_mort.dropna(axis=0, how='any', inplace=True)
sum(child_mort.duplicated())


# In[14]:


# Get table info after dropping missing values 
child_mort.info()


# In[15]:


# Unpivot the DataFrame from wide format to long format and clean up column names. 
child_mort_melt = pd.melt(child_mort, id_vars='Under five mortality', var_name='year', value_name='under_5_mortality')
child_mort_melt.rename(columns={'Under five mortality':'country'},inplace=True)
child_mort_melt.head()


# In[16]:


# Get table info after melt operation 
child_mort_melt.info()


# In[17]:


# Convert the data type of the "year" column from a string to an integer
child_mort_melt['year'] = child_mort_melt['year'].astype(int)


# In[18]:


# Get descriptive statistics 
child_mort_melt.describe()


# The child mortality DataFrame has been successfully cleaned and melted into long format and is ready for exploratory analysis to follow in the next section.

# ### Per Capital Total Health Spending Data Assessment and Cleaning 

# In[19]:


# Load per capita total health spending data and print out a few lines. 
health_spend = pd.read_csv('indicator_health_spending_per_person_USD.csv', encoding='mac_roman')
health_spend.head()


# In[20]:


# Assess the total health spending data
health_spend.info()


# The per capita total health spending DataFrame is also in wide format but I want it in long format for ease of comparing multiple indicators against east other. Similar to the handling of the previous two DataFrames, I would like to keep countries that have partial data. I will drop all rows containing any null values, including countries which may have partial data, for consistency of analysis when calculating global averages over time. I will also check for and remove any duplicated rows. I will then reshape the DataFrame into long format. 

# In[21]:


# Drop rows that contain missing values and determine if there are duplicate entries 
health_spend.dropna(axis=0, how='any', inplace=True)
sum(health_spend.duplicated())


# In[22]:


# Get table info after dropping missing values 
health_spend.info()


# In[23]:


# Unpivot the DataFrame from wide format to long format and clean up column names. 
health_spend_melt = pd.melt(health_spend, id_vars='Per capita total expenditure on health at average exchange rate (US$)', var_name='year', value_name='per_capita_health_spend')
health_spend_melt.rename(columns={'Per capita total expenditure on health at average exchange rate (US$)':'country'},inplace=True)
health_spend_melt.head()


# In[24]:


# Get table info after melt operation 
health_spend_melt.info()


# In[25]:


# Convert the data type of the "year" column from a string to an integer
health_spend_melt['year'] = health_spend_melt['year'].astype(int)


# In[26]:


# Get descriptive statistics 
health_spend_melt.describe()


# The per capital health spending DataFrame has been successfully cleaned and melted into long format and is ready for exploratory analysis to follow in the next section. I have refrained from joining these DataFrames at this point in the analysis so as to maintain the integrity of each dataset for first performing independent analysis.  

# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# In this section, I will create visualizations and compute descriptive statistics to explore the cleaned data and answer the questions I posed in the Introduction. 
# 
# ### Life Expectancy Over Time Globally and in the U.S.

# In[27]:


# Calculate the global mean life expectancy each year 
avg_life_exp = life_exp_melt.groupby('year')['life_expectancy'].mean()


# In[28]:


# Extract the mean life expectancy each year in the United States
us_avg_life_exp = life_exp_melt.query('country == "United States"').groupby('year')['life_expectancy'].mean()


# In[29]:


# Plot the average life expectancy each year globally and in the United States 
fig, ax = plt.subplots(figsize=(6,6));
fig1 = ax.plot(avg_life_exp.index, avg_life_exp, 'b', label='Global')
fig2 = ax.plot(us_avg_life_exp.index, us_avg_life_exp, 'grey', label='United States')
plt.xlabel('Year', fontsize = 14);
plt.ylabel('Life Expectancy at Birth (Years)', fontsize = 14);
plt.title('Average Life Expectancy', fontsize = 16);
plt.tick_params(labelsize = 12);
plt.legend()
plt.show()


# In[30]:


# Extract the life expectancy from the year 2016 and plot it as a histogram 
life_exp_2016 = life_exp_melt.query('year == 2016')
plt.figure(figsize=(6,6))
plt.hist(life_exp_2016['life_expectancy']);
plt.xlabel('Life Expectancy at Birth (Years)', fontsize = 14);
plt.ylabel('Frequency', fontsize = 14);
plt.title('Global Life Expectancy in 2016', fontsize = 16);
plt.tick_params(labelsize = 12)
plt.show()


# In[31]:


# Determine descriptive statistics about the life expectancy data in 2016 
life_exp_2016['life_expectancy'].describe()


# In[32]:


# Determine the life expectancy in the United States in 2016 
life_exp_2016.query('country == "United States"')


# In[33]:


# Determine the country with the highest life expectancy in 2016 
life_exp_2016.loc[life_exp_2016['life_expectancy'].idxmax()]


# In[34]:


# Determine the country with the highest life expectancy in 2016 
life_exp_2016.loc[life_exp_2016['life_expectancy'].idxmin()]


# Since 1800, the average life expectancy has increased by approximately 40 years globally as well as in the United States. Life expectancy in the United States has remained consistently higher than the global average. Life expectancies remained fairly constant for much of the 1800s. In the United States, life expectancies began increasing dramatically beginning around 1870. Globally, the dramatic increase began around 1920. It is interesting to note the years where significant drops in life expectancy was observed. In the United States, these drops correspond to the Civil War, lasting between 1861-1865, and WWI, lasting between 1914 and 1918. Globally, the largest drop also corresponds to WWI, with a smaller drop observed during WWII. 
# 
# The distribution of life expectancy data in 2016 (the year for which the most recent data is available) is left-skewed. The difference between the third quartile and the maximum of the data is only 5.3 years, while the difference between the minimum and the first quartile is 18.2 years. The average life expectancy in the United States is above the third quartile. The country with the highest life expectancy is Hong Kong (China), while the country with the lowest life expectancy is Lesotho. These results suggest that although average global life expectancies have risen dramatically over the last century, there are still countries today where life expectancy remains low. 

# ### Child Mortality Rates Over Time Globally and in the U.S.

# In[35]:


# Calculate the global mean child mortality rate each year 
avg_child_mort = child_mort_melt.groupby('year')['under_5_mortality'].mean()


# In[36]:


# Extract the mean child mortality rate each year in the United States
us_avg_child_mort = child_mort_melt.query('country == "United States"').groupby('year')['under_5_mortality'].mean()


# In[37]:


# Plot the average child mortality rate each year globally and in the United States 
fig, ax = plt.subplots(figsize=(6,6));
fig1 = ax.plot(avg_child_mort.index, avg_child_mort, 'b', label='Global')
fig2 = ax.plot(us_avg_child_mort.index, us_avg_child_mort, 'grey', label='United States')
plt.xlabel('Year', fontsize = 14);
plt.ylabel('Under 5 Mortality Rate (Per 1,000 Live Births)', fontsize = 14);
plt.title('Average Child Mortality Rate', fontsize = 16);
plt.tick_params(labelsize = 12);
plt.legend()
plt.show()


# In[38]:


# Extract the child mortality rate from the year 2015 and plot it as a histogram 
child_mort_2015 = child_mort_melt.query('year == 2015')
plt.figure(figsize=(6,6))
plt.hist(child_mort_2015['under_5_mortality']);
plt.xlabel('Under 5 Mortality Rate (Per 1,000 Live Births)', fontsize = 14);
plt.ylabel('Frequency', fontsize = 14);
plt.title('Global Child Mortality Rates in 2015', fontsize = 16);
plt.tick_params(labelsize = 12)
plt.show()


# In[39]:


# Determine descriptive statistics about the child mortality rate data in 2015
child_mort_2015['under_5_mortality'].describe()


# In[40]:


# Determine the child mortality rate in the United States in 2015
child_mort_2015.query('country == "United States"')


# In[41]:


# Determine the country with the lowest child mortality rate in 2015
child_mort_2015.loc[child_mort_2015['under_5_mortality'].idxmin()]


# In[42]:


# Determine the country with the highest child mortality rate in 2015
child_mort_2015.loc[child_mort_2015['under_5_mortality'].idxmax()]


# Since 1800, the average child mortality rate has decreased by approximately 400 per 1000 live births globally. In the United States, the decrease is approximately 450 per 1000 live births. Child mortality rates in the United States were higher than the global average prior to the late 1840s, but have been consistently lower than the global average since then. Life expectancies remained fairly constant for much of the 1800s. Again, it is interesting to note the years where significant increases in child mortality was observed. In the United States, these increases correspond to the Civil War and WWI, like for life expectancy. Globally, however, there are no observable spikes in child mortality.
# 
# The distribution of child mortality rate data in 2015 (the year for which the most recent data is available) is right-skewed. The difference between the third quartile and the maximum of the data is 107.2, while the difference between the minimum and the first quartile is only 6.2. The average child mortality rate in the United States is below the first quartile. The country with the lowest child mortality rates is Luxembourg, while the country with the highest child mortality rates is Angola. Similar to for life expectancy results, these results suggest that although average global child mortality rates have declined dramatically over the last century, there are still countries today where child mortality rates remain high. 

# ### Per Capita Total Health Spend Over Time Globally and in the U.S.

# In[43]:


# Calculate the global mean total health spend each year 
avg_health_spend = health_spend_melt.groupby('year')['per_capita_health_spend'].mean()


# In[44]:


# Extract the mean total health spend each year in the United States
us_avg_health_spend = health_spend_melt.query('country == "United States"').groupby('year')['per_capita_health_spend'].mean()


# In[45]:


# Plot the average total health spend per person each year globally and in the United States 
fig, ax = plt.subplots(figsize=(6,6));
fig1 = ax.plot(avg_health_spend.index, avg_health_spend, 'b', label='Global')
fig2 = ax.plot(us_avg_health_spend.index, us_avg_health_spend, 'grey', label='United States')
plt.xlabel('Year', fontsize = 14);
plt.ylabel('Per Capita Total Health Spend (USD)', fontsize = 14);
plt.title('Average Per Capita Total Health Spend', fontsize = 16);
plt.tick_params(labelsize = 12);
plt.legend()
plt.show()


# In[46]:


# Extract the total health spend data from the year 2010 and plot it as a histogram 
health_spend_2010 = health_spend_melt.query('year == 2010')
health_spend_2010_clean = health_spend_2010.dropna()
plt.figure(figsize=(6,6))
plt.hist(health_spend_2010_clean['per_capita_health_spend']);
plt.xlabel('Per Capita Total Health Spend (USD)', fontsize = 14);
plt.ylabel('Frequency', fontsize = 14);
plt.title('Global Per Capita Health Spending in 2010', fontsize = 16);
plt.tick_params(labelsize = 12)
plt.show()


# In[47]:


# Determine descriptive statistics about the total health spend data in 2010
health_spend_2010['per_capita_health_spend'].describe()


# In[48]:


# Determine the health spend per person in the United States in 2010
health_spend_2010.query('country == "United States"')


# In[49]:


# Determine the country with the lowest health spend per person in 2010
health_spend_2010.loc[health_spend_2010['per_capita_health_spend'].idxmin()]


# In[50]:


# Determine the country with the highest health spend per person in 2010
health_spend_2010.loc[health_spend_2010['per_capita_health_spend'].idxmax()]


# The average global per capital total health spending has approximately doubled over the past 15 years. In that time window, the average per capital total health spending in the United States has been consistently about 8 times greater than the global average. The distribution of per capital total health spending in 2010 is right-skewed. The country with the smallest per capita health spending in 2010 was Eritrea, spending only 11.9 USD per person versus 8361.7 USD per person for the United States

# ### Correlations Between Health Spending, Life Expectancy, and Child Mortality
# In this section, I will join DataFrames to enable multi-variable analysis. 

# In[51]:


# Inner join life expectancy and child mortality tables on country and year to enable comparison 
life_exp_child_mort = life_exp_melt.merge(child_mort_melt, how='inner', left_on=['country', 'year'], right_on=['country', 'year'])
life_exp_child_mort.head()


# In[52]:


# Create a scatter plot of life expectancy vs. child mortality for all countries colored by year 
plt.figure(figsize=(6,6));
sns.lmplot('under_5_mortality', 'life_expectancy', data=life_exp_child_mort, fit_reg=False);
plt.xlabel('Under 5 Mortality Rate (Per 1,000 Live Births)', fontsize = 14);
plt.ylabel('Life Expectancy (Years)', fontsize = 14);
plt.title('Global Life Expectancy Vs. Child Mortality', fontsize = 16);
plt.tick_params(labelsize = 12);
plt.show();


# There is an observable negative correlation between life expectancy and child mortality rates, consistent with the dependence of the life expectancy (at birth) calculation on child mortality rates.

# In[53]:


# Inner join health spend and life expectancy tables on country and year to enable comparison 
health_spend_life_exp = life_exp_melt.merge(health_spend_melt, how='inner', left_on=['country', 'year'], right_on=['country', 'year'])
health_spend_life_exp.head()


# In[54]:


# Create a scatter plot of health spend vs. life expectancy for all countries colored by year 
plt.figure(figsize=(6,6));
sns.lmplot('life_expectancy', 'per_capita_health_spend', data=health_spend_life_exp, hue='year', fit_reg=False);
plt.xlabel('Life Expectancy (Years)', fontsize = 14);
plt.ylabel('Per Capita Health Spend (USD)', fontsize = 14);
plt.title('Global Health Spending Vs. Life Expectancy', fontsize = 16);
plt.tick_params(labelsize = 12);
plt.show();


# Plotting per capita health spending versus life expectancy shows an interesting result. All countries with low life expectancy (less than 70 years) also have low per capita health spending. However, countries with high life expectancy (greater than 70 years) have a wide distribution of per capita health spending. Some countries with very high life expectancies spend no more on health per capita than countries with very low life expectancies. These results suggest that additional factors have measurable impacts on life expectancy than health spending. Further statistical analysis is required to assess the correlation between per capita health spending and life expectancy. 

# In[55]:


# Inner join health spend and child mortality tables on country and year to enable comparison 
health_spend_child_mort = child_mort_melt.merge(health_spend_melt, how='inner', left_on=['country', 'year'], right_on=['country', 'year'])
health_spend_child_mort.head()


# In[56]:


# Create a scatter plot of health spend vs. child mortality for all countries colored by year 
plt.figure(figsize=(6,6));
sns.lmplot('under_5_mortality', 'per_capita_health_spend', data=health_spend_child_mort, hue='year', fit_reg=False);
plt.xlabel('Under 5 Mortality Rate (Per 1,000 Live Births)', fontsize = 14);
plt.ylabel('Per Capita Health Spend (USD)', fontsize = 14);
plt.title('Global Health Spending Vs. Child Mortality', fontsize = 16);
plt.tick_params(labelsize = 12);
plt.show();


# Plotting per capita total health spending versus child mortality shows a similar result as for life expectancy above. All countries with high child mortality rates (greater than 30 deaths per 1000 live births) also have low per capita health spending. However, countries with low child mortality rates (less than 30 deaths per 1000 live births) have a wide distribution of per capita health spending. Some countries with very low child mortality rates spend no more on health per capita than countries with very high child mortality rates. These results suggest that additional factors have measurable impacts on child mortality rates than health spending. Further statistical analysis is required to assess the correlation between per capita health spending and child mortality. 

# <a id='conclusions'></a>
# ## Conclusions
# 
# In this project, I explored data on life expectancy, child mortality, and per capital health spending from <a href=https://www.gapminder.org/data/>Gapminder World</a>. After assessing and cleaning the data for analysis, I performed exploratory data analysis by creating visuals and calculating descriptive statistics to answer some interesting questions about population health outcomes around the world and how they have changed over time. 
# 
# The overall findings from my exploratory data analysis show that life expectancies have risen dramatically over the last 100 years while child mortality rates have dramatically declined. Since life expectancy (calculated at birth) is strongly dependent on child mortality rates, it is consistent that there is a negative correlation between the two variables. For both indicators, the United States performs better than the global average, sitting above the third quartile for life expectancy and below the first quartile for child mortality. However, despite global progress, there are still countries today where low life expectancies and high child mortality rates are observed. Further, my exploratory data analysis suggests that per capita total health spending does not directly correlate with life expectancies or child mortality rates, as there are an abundance of countries with low per capital health spending and good survival outcomes. Follow-up statistical analysis is required to shed additional light on the correlation of per capita health spending and population survival outcomes.  
# 
# This analysis revealed interesting insights on population health data around the world. While this analysis only focused on three indicators, there is a diverse array of indicators that have measurable impacts on population health. In conclusion, I think this analysis brings up a couple of interesting questions, including how best to improve health outcomes in countries with poor life expectancies today and how best to improve health outcomes while lowering healthcare spending. 
