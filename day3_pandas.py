import pandas as pd
import numpy as np

# 1. Create a small dataset
data = {
    "student": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"],
    "math": [80, 90, np.nan, 70, 60],
    "physics": [75, np.nan, 85, 65, 55],
    "signal_processing": [88, 92, 79, np.nan, 60]
}

df = pd.DataFrame(data)

print("\nOriginal dataframe:")
print(df)

# 2. Basic inspection
print("\nShape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nInfo:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

# 3. Missing values
print("\nMissing values per column:")
print(df.isna().sum())

# 4. Fill missing values with column means
numeric_cols = ["math", "physics", "signal_processing"]

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

print("\nAfter filling missing values:")
print(df)

# 5. Add average score column
df["average"] = df[numeric_cols].mean(axis=1)

print("\nWith average score:")
print(df)

# 6. Normalize numeric columns
for col in numeric_cols:
    df[col + "_norm"] = (df[col] - df[col].mean()) / df[col].std()

print("\nWith normalized columns:")
print(df)


df["passed"] = df["average"] >= 70
print("\nWith passed column:")
print(df)

# 7. Save processed file
df.to_csv("day3_processed_students.csv", index=False)

print("\nSaved: day3_processed_students.csv")