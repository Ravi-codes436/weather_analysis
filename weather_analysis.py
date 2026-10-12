import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("energy1.csv")
ac= "active_power"
# changing the datatype of date
df["date"] = pd.to_datetime(df["date"])
# correlation between active_power and temp
df[ac].corr(df["temp"])

#assigning category to range of values
df["temp_range"] = pd.cut(
    df["temp"],
    bins = [df["temp"].min()-1,5,15,25,32, df["temp"].max()],
    labels=["Very Cool", "Cold", "Moderate", "Warm", "Hot"]   
)

# now grouping above categories with respect to temperature range column
grp_temp = df.groupby("temp_range", as_index=False, observed=False)[ac].agg(
    mean = "mean",
    median = "median"
)

#print(df)
#print(grp_temp.dtypes)


fig, ax = plt.subplot_mosaic(
    [["A", "B", "B"],
     ["C", "C", "D"]],
    figsize=(16, 10),
    constrained_layout=True,
)
ax["A"].bar(grp_temp["temp_range"], grp_temp["mean"], label = "Mean")
ax["A"].bar(grp_temp["temp_range"], grp_temp["median"], label = "Median")
ax["A"].set_xlabel("Weather")
ax["A"].set_ylabel("Active power")
ax["A"].legend()




grp_main = df.groupby("main", as_index=False)[ac].agg(
    mean = "mean",
    median = "median"
)
ax["B"].bar(grp_main["main"], grp_main["mean"], label = "Mean")
ax["B"].bar(grp_main["main"], grp_main["median"], label = "Median")
ax["B"].set_xlabel("Description")
ax["B"].set_ylabel("Active power")
ax["B"].legend()


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

df["press_range"] = pd.cut(
    df["pressure"],
    bins = [995, 1005, 1013, 1020, 1028, 1036],
    labels = ["Very Low", "Low", "Normal", "High", "Very High"]
)
grp_press = df.groupby("press_range", as_index=False)[ac].agg(
    mean = "mean",
    median = "median"
)
ax["D"].bar(grp_press["press_range"], grp_press["mean"], label= "Mean")
ax["D"].bar(grp_press["press_range"], grp_press["median"], label= "Median")
ax["D"].set_xlabel("Pressure")
ax["D"].set_ylabel("Active Power")
ax["D"].legend()


df["humid_range"]= pd.cut(
    df["humidity"],
    bins=[0, 20, 40, 60, 80, 101],
    labels=["very dry", "dry", "comfortable", "humid", "very humid"]
)
grp_hd = df.groupby("humid_range", as_index=False)[ac].agg(
    mean = "mean",
    median = "median"
)

ax["C"].bar(grp_hd["humid_range"], grp_hd["mean"], label = "Mean")
ax["C"].bar(grp_hd["humid_range"], grp_hd["median"], label = "Median")
ax["C"].set_xlabel("Humidity")
ax["C"].set_ylabel("Active power")
ax["C"].legend()



fig.suptitle("Active power dependence")
plt.savefig("Weather analysis graphs")
plt.show()
