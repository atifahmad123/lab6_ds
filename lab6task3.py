import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Date": [
        "2026-03-01", "2026-03-02", "2026-03-03",
        "2026-03-04", "2026-03-05", "2026-03-06",
        "2026-03-07", "2026-03-08", "2026-03-09",
        "2026-03-10", "2026-03-11", "2026-03-12",
        "2026-03-13", "2026-03-14", "2026-03-15",
        "2026-03-01"
    ],
    "City": [
        " kamra", "KAMRA ", "Kamra", "kamra",
        " Kamra", "KAMRA", "kamra ", "Kamra",
        " KAMRA", "kamra", "Kamra ", "KAMRA",
        " kamra ", "Kamra", "KAMRA", " kamra"
    ],
    "Temperature": [
        "32C", "28C", "25C", "33C", "29C", "34C",
        "24C", "30C", "35C", "28C", "32C", "26C",
        "31C", "29C", "33C", "32C"
    ],
    "Humidity": [
        45, 60, 80, None, 58, 42, 85, None,
        40, 65, 48, 78, None, 62, 46, 45
    ],
    "Condition": [
        "sunny", " CLOUDY", "Rainy ", "SUNNY",
        "cloudy ", " Sunny", "RAINY", "Cloudy",
        "SUNNY ", " cloudy", "sunny", " Rainy",
        "Sunny ", "CLOUDY", " sunny", "sunny"
    ]
}

df = pd.DataFrame(data)

df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

df["Temperature"] = df["Temperature"].str.replace(
    "C", "", regex=False
)
df["Temperature"] = pd.to_numeric(
    df["Temperature"], errors="coerce"
)
df["Date"] = pd.to_datetime(df["Date"])

df = df.drop_duplicates().copy()

humidity_median = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(humidity_median)

print("Rows after dropping duplicates:", len(df))
print("Humidity median:", humidity_median)


df_encoded = pd.get_dummies(
    df, columns=["Condition"], dtype=int
)
print(df_encoded.filter(like="Condition_"))

correlation = df["Temperature"].corr(df["Humidity"])
print("Correlation:", round(correlation, 3))

condition_counts = df["Condition"].value_counts()
print(condition_counts)

df = df.sort_values("Date")


fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(
    df["Date"], df["Temperature"],
    marker="o", color="steelblue"
)
axes[0, 0].set_title("Temperature Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", labelrotation=45)

axes[0, 1].scatter(
    df["Temperature"], df["Humidity"], color="orange"
)
axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity (%)")

axes[1, 0].pie(
    condition_counts.values,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    colors=["orange", "lightgray", "steelblue"]
)
axes[1, 0].set_title("Days by Condition")

axes[1, 1].hist(
    df["Temperature"], bins=5,
    color="seagreen", edgecolor="white"
)
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

fig.suptitle("Weather Overview", fontsize=16)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
print("Saved weather_dashboard.png")
plt.show()