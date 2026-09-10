import pandas as pd

df = pd.read_csv("data.csv")

print("Data:")
print(df)

print("\nRows and Columns:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("n\summary:")
print(df.describe())

filtered = df[df["Marks"] >= 50]

print("\nFiltered Data:")
print(filtered)

cleaned = filtered.dropna()

cleaned.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")
