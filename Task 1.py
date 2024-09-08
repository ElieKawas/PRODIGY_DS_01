#Task 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/hp/Desktop/Intership/Prodigy Task 1/population.csv')
#Data Overview
print(f'''The shape of data: {df.shape}''')
print(df.head(100))
print(df.info())
print(df.describe)

#Data Cleaning
df = df.drop("Country Code", axis=1)
df = df.drop("Series Name", axis=1)

#The data is too big so i want to extract the top 10 countries of the most population and smallest population
#and for the visualization be more clearer

# Filter data for total population
total_population_data = df[df["Series Code"] == "SP.POP.TOTL"]

# Sort data based on the total population for 2022
total_population_sorted = total_population_data.sort_values(by="2022", ascending=False)

# Get the top ten countries with the highest total population for 2022
total_top_ten_countries = total_population_sorted.head(10)
print("Top ten countries of total population")
print(total_top_ten_countries )



#Data Visualization
#BARPLOT

#Top ten countries by total popuplation
"""
plt.figure(figsize=(12, 8))
plt.suptitle("Top Ten Countries by Total Population in 2022, 2016, 2010, and 2001", fontsize=20, y=0.95)
plt.rcParams['axes.facecolor'] = 'black'

# Plot for 2022
plt.subplot(2, 2, 1)
sns.barplot(x="2022", y="Country Name", data=total_top_ten_countries, palette="coolwarm")
plt.title("2022")
plt.xlabel("Total Population")
plt.ylabel("Country")

# Plot for 2016
plt.subplot(2, 2, 2)
sns.barplot(x="2016", y="Country Name", data=total_top_ten_countries, palette="coolwarm")
plt.title("2016")
plt.xlabel("Total Population")
plt.ylabel("Country")

# Plot for 2010
plt.subplot(2, 2, 3)
sns.barplot(x="2010", y="Country Name", data=total_top_ten_countries, palette="coolwarm")
plt.title("2010")
plt.xlabel("Total Population")
plt.ylabel("Country")

# Plot for 2001
plt.subplot(2, 2, 4)
sns.barplot(x="2001", y="Country Name", data=total_top_ten_countries, palette="coolwarm")
plt.title("2001")
plt.xlabel("Total Population")
plt.ylabel("Country")

plt.tight_layout(rect=[0, 0, 1, 0.93])  #Adjusts the layout to ensure the plots and title fit well within the figure
plt.show()
"""

#Bottom ten countries by total population

"""
# Get the bottom ten countries with the highest total population for 2022
total_population_sorted = total_population_data.sort_values(by="2022", ascending=True)
total_bottom_ten_countries = total_population_sorted.head(10)
print("Bottom ten countries of total population")
print(total_bottom_ten_countries )


plt.figure(figsize=(12, 8))
plt.suptitle("Bottom Ten Countries by Total Population in 2022, 2016, 2010, and 2001", fontsize=20, y=0.95)
plt.rcParams['axes.facecolor'] = 'black'

# Plot for 2022
plt.subplot(2, 2, 1)
sns.barplot(x="2022", y="Country Name", data=total_bottom_ten_countries, palette="coolwarm")
plt.title("2022")
plt.xlabel("Total Population")
plt.ylabel("Country")

# Plot for 2016
plt.subplot(2, 2, 2)
sns.barplot(x="2016", y="Country Name", data=total_bottom_ten_countries, palette="coolwarm")
plt.title("2016")
plt.xlabel("Total Population")
plt.ylabel("Country")

# Plot for 2010
plt.subplot(2, 2, 3)
sns.barplot(x="2010", y="Country Name", data=total_bottom_ten_countries, palette="coolwarm")
plt.title("2010")
plt.xlabel("Total Population")
plt.ylabel("Country")

# Plot for 2001
plt.subplot(2, 2, 4)
sns.barplot(x="2001", y="Country Name", data=total_bottom_ten_countries, palette="coolwarm")
plt.title("2001")
plt.xlabel("Total Population")
plt.ylabel("Country")

plt.tight_layout(rect=[0, 0, 1, 0.93]) 
plt.show()
"""


#Extract top ten countries with the highest male population

total_population_data = df[df["Series Code"] == "SP.POP.TOTL.MA.IN"]

total_population_sorted = total_population_data.sort_values(by="2022", ascending=False)
male_top_ten_countries = total_population_sorted.head(10)
print("Top ten countries with the highest male population")
print(male_top_ten_countries )

#Extract top ten countries with the highest female population

total_population_data = df[df["Series Code"] == "SP.POP.TOTL.FE.IN"]

total_population_sorted = total_population_data.sort_values(by="2022", ascending=False)
female_top_ten_countries = total_population_sorted.head(10)
print("Top ten countries with the highest female population")
print(female_top_ten_countries )


#Visualization
plt.figure(figsize=(12, 8))
plt.suptitle("Top Ten Countries with highest male and female population in 2022 and 2012", fontsize=20, y=0.95)
plt.rcParams['axes.facecolor'] = 'black'

# Plot for 2022
plt.subplot(2, 2, 1)
sns.barplot(x="2022", y="Country Name", data=male_top_ten_countries, palette="coolwarm")
plt.title("2022")
plt.xlabel("Total Male Population")
plt.ylabel("Country")

#female

plt.subplot(2, 2, 2)
sns.barplot(x="2022", y="Country Name", data=female_top_ten_countries, palette="coolwarm")
plt.title("2022")
plt.xlabel("Total Female Population")
plt.ylabel("Country")

# Plot for 2012
plt.subplot(2, 2, 3)
sns.barplot(x="2012", y="Country Name", data=male_top_ten_countries, palette="coolwarm")
plt.title("2012")
plt.xlabel("Total Male Population")
plt.ylabel("Country")

#female
plt.subplot(2, 2, 4)
sns.barplot(x="2022", y="Country Name", data=female_top_ten_countries, palette="coolwarm")
plt.title("2012")
plt.xlabel("Total Female Population")
plt.ylabel("Country")

plt.tight_layout(rect=[0, 0, 1, 0.93]) 
plt.show()


#PS: I took random years and it's applicable for all years

#Extract bottom ten countries with the most male population
total_population_data = df[df["Series Code"] == "SP.POP.TOTL.MA.IN"]

total_population_sorted = total_population_data.sort_values(by="2022", ascending=True)
male_bottom_ten_countries = total_population_sorted.head(10)
print("Bottom ten countries with the highest male population")
print(male_bottom_ten_countries )

#Extract bottom ten countries with the most female population

total_population_data = df[df["Series Code"] == "SP.POP.TOTL.FE.IN"]

total_population_sorted = total_population_data.sort_values(by="2022", ascending=True)
female_bottom_ten_countries = total_population_sorted.head(10)
print("Bottom ten countries with the highest female population")
print(female_bottom_ten_countries )


plt.figure(figsize=(12, 8))
plt.suptitle("Bottom Ten Countries with highest male and female population in 2022 and 2012", fontsize=20, y=0.95)
plt.rcParams['axes.facecolor'] = 'black'

# Plot for 2022
plt.subplot(2, 2, 1)
sns.barplot(x="2022", y="Country Name", data=male_bottom_ten_countries, palette="coolwarm")
plt.title("2022")
plt.xlabel("Total Male Population")
plt.ylabel("Country")

#female

plt.subplot(2, 2, 2)
sns.barplot(x="2022", y="Country Name", data=female_bottom_ten_countries, palette="coolwarm")
plt.title("2022")
plt.xlabel("Total Female Population")
plt.ylabel("Country")

# Plot for 2012
plt.subplot(2, 2, 3)
sns.barplot(x="2012", y="Country Name", data=male_bottom_ten_countries, palette="coolwarm")
plt.title("2012")
plt.xlabel("Total Male Population")
plt.ylabel("Country")

#female
plt.subplot(2, 2, 4)
sns.barplot(x="2022", y="Country Name", data=female_bottom_ten_countries, palette="coolwarm")
plt.title("2012")
plt.xlabel("Total Female Population")
plt.ylabel("Country")

plt.tight_layout(rect=[0, 0, 1, 0.93]) 
plt.show()
