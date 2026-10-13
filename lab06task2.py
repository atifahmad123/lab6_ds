import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Cola", "Chips", "Milk", "Biscuits", "Juice",
                "Yogurt", "Tea", "Popcorn", "Cheese", "Coffee"],
    "Category": ["beverages ", "SNACKS", " Dairy", "Snacks",
                 "beverages", "DAIRY ", " Beverages", " snacks",
                 "dairy", "BEVERAGES"],
    "Price": ["Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120",
              "Rs. 1,800", "Rs. 200", "Rs. 650", "Rs. 150",
              "Rs. 800", "Rs. 1,100"],
    "Stock": [40, 120, 60, 100, 30, 50, 70, 80, 25, 45]
}

df = pd.DataFrame(data)


df["Category"] = df["Category"].str.strip().str.title()

df["Price"] = df["Price"].str.replace("Rs. ", "", regex=False)
df["Price"] = df["Price"].str.replace(",", "", regex=False)
df["Price"] = df["Price"].astype(float)

df["Category_Code"] = df["Category"].astype("category").cat.codes

print(df)

average_price = df.groupby("Category")["Price"].mean()
total_stock = df.groupby("Category")["Stock"].sum()


fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].bar(average_price.index, average_price.values,
            color=["steelblue", "orange", "red"])
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")

axes[1].pie(total_stock.values, labels=total_stock.index,
            autopct="%1.1f%%", colors=["steelblue", "orange", "red"])

axes[1].set_title("Stock Share by Category")

plt.tight_layout()
plt.savefig("inventory_plots.png")
print("Saved inventory_plots.png")
plt.show()