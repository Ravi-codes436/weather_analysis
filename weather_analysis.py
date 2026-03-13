import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("energy1.csv")
ac= "active_power"
# changing the datatype of date
df["date"] = pd.to_datetime(df["date"])
# correlation between active_power and temp
df[ac].corr(df["temp"])

df["temp_range"] = pd.cut(
    df["temp"],
    bins = [df["temp"].min()-1,5,15,25,32, df["temp"].max()],
    labels=["Very Cool", "Cold", ",Moderate", "Warm", "Hot"]   
)
grp_temp = df.groupby("temp_range", as_index=False, observed=False)[ac].agg(
    mean = "mean",
    median = "median"
)
plt.bar(grp_temp["temp_range"], grp_temp["mean"], label = "Mean")
plt.bar(grp_temp["temp_range"], grp_temp["median"], label = "Median")
plt.legend()
plt.show()




grp_main = df.groupby("main", as_index=False)[ac].agg(
    mean = "mean",
    median = "median"
)
plt.bar(grp_main["main"], grp_main["mean"], label = "Mean")
plt.bar(grp_main["main"], grp_main["median"], label = "Median")
plt.legend()
plt.xticks(rotation = 45)
plt.show()

weather_map = {
    "clear sky": "Clear",

    "few clouds": "Cloudy",
    "scattered clouds": "Cloudy",
    "broken clouds": "Cloudy",
    "overcast clouds": "Cloudy",

    "mist": "Low Visibility",
    "haze": "Low Visibility",
    "fog": "Low Visibility",

    "drizzle": "Light Rain",
    "light intensity drizzle": "Light Rain",
    "light rain": "Light Rain",

    "moderate rain": "Heavy Rain",
    "heavy intensity rain": "Heavy Rain",
    "very heavy rain": "Heavy Rain",

    "thunderstorm": "Thunderstorm",
    "thunderstorm with rain": "Thunderstorm"
}

df["weather_group"] = df["description"].map(weather_map)
grp_desc = df.groupby("weather_group", as_index=False)[ac].agg(
    mean = "mean",
    median = "median"
)
plt.bar(grp_desc["weather_group"], grp_desc['mean'],label = "Mean")
plt.bar(grp_desc["weather_group"], grp_desc['median'],label = "Median")
plt.legend()
plt.xticks(rotation = 45)
plt.show()



df["press_range"] = pd.cut(
    df["pressure"],
    bins = [995, 1005, 1013, 1020, 1028, 1036],
    labels = ["Very Low", "Low", "Normal", "High", "Very High"]
)
grp_press = df.groupby("press_range", as_index=False)[ac].agg(
    mean = "mean",
    median = "median"
)
plt.bar(grp_press["press_range"], grp_press["mean"], label= "Mean")
plt.bar(grp_press["press_range"], grp_press["median"], label= "Median")
plt.legend()
plt.show()


df["humid_range"]= pd.cut(
    df["humidity"],
    bins=[0, 20, 40, 60, 80, 101],
    labels=["very dry", "dry", "comfortable", "humid", "very humid"]
)
grp_hd = df.groupby("humid_range", as_index=False)[ac].agg(
    mean = "mean",
    median = "median"
)
plt.bar(grp_hd["humid_range"], grp_hd["mean"], label = "Mean")
plt.bar(grp_hd["humid_range"], grp_hd["median"], label = "Median")
plt.legend()
plt.show()
