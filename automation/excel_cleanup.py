import pandas as pd

df = pd.read_excel("RawData.xlsx")
df = df.drop_duplicates()
df = df.fillna("N/A")
df.to_excel("Refined_Data.xlsx", index=False)

print("Data cleaned successfully!")
