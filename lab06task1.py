import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": [" atif", "ahmad ", "asif", " ali",
             "umar", "saad ", "hubab", " anfal "],
    "Marks": ["72", "85", "absent", "64",
              "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

df["Name"] = df["Name"].str.strip().str.title()
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df)

plt.figure(figsize=(8, 4))
plt.bar(df["Name"], df["Marks"], color="steelblue")
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("marks_bar.png")
print("Saved marks_bar.png")
plt.show()