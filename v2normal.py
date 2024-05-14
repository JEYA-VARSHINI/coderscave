import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data Collection
# Assume you have a CSV file containing historical climate data

daily_data = pd.read_csv("C:\\Users\\HP\\Downloads\\climate\\daily_data.csv")
hourly_data = pd.read_csv("C:\\Users\\HP\\Downloads\\climate\\hourly_data.csv")
monthly_data = pd.read_csv("C:\\Users\\HP\\Downloads\\climate\\monthly_data.csv")
three_hour_data = pd.read_csv("C:\\Users\\HP\\Downloads\\climate\\three_hour_data.csv")

# Line plot for a column in daily_data
plt.figure(figsize=(10, 6))
plt.plot(daily_data['DATE'], daily_data['DailyDepartureFromNormalAverageTemperature'])
plt.title('Daily Temperature Variation')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# KDE plot for a column in hourly_data
plt.figure(figsize=(10, 6))
sns.kdeplot(hourly_data['HourlyWetBulbTemperature'], color='orange', shade=True)
plt.title('Temperature Distribution (Hourly)')
plt.xlabel('Wet Bulb Temperature (°C)')
plt.ylabel('Density')
plt.grid(True)
plt.show()

# Line plot for a column in monthly_data
plt.figure(figsize=(10, 6))
plt.plot(monthly_data['DATE'], monthly_data['MonthlyDepartureFromNormalHeatingDegreeDays'], color='green')
plt.title('Monthly Heating Degree Days Trend')
plt.xlabel('Date')
plt.ylabel('Heating Degree Days')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# KDE plot for a column in three_hour_data
plt.figure(figsize=(10, 6))
sns.kdeplot(three_hour_data['HourlyPressureChange'], color='red', shade=True)
plt.title('Pressure Change Distribution (Three-Hourly)')
plt.xlabel('Pressure Change')
plt.ylabel('Density')
plt.grid(True)
plt.show()

