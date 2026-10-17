
# import pandas as pd

# df = pd.read_excel("SWYNEX_Titanic_Data_Cleaned.xlsx")

# # Remove extra spaces from column names
# df.columns = df.columns.str.strip()

# print("COLUMN NAMES:")
# print(df.columns.tolist())

# print("\nAVERAGE AGE:")
# print(df["Age"].mean())

# print("\nSURVIVAL COUNT:")
# print(df["Survived"].value_counts())

# print("\nSURVIVAL PERCENTAGE:")
# print(df["Survived"].value_counts(normalize=True) * 100)
# # Survival Analysis by Gender
# print("\nSURVIVAL BY GENDER:")
# print(pd.crosstab(df["Sex"], df["Survived"]))

# # Survival Rate by Gender
# print("\nSURVIVAL RATE BY GENDER:")
# print(df.groupby("Sex")["Survived"].mean() * 100)

# # Survival by Passenger Class
# print("\nSURVIVAL BY PASSENGER CLASS:")
# print(pd.crosstab(df["Pclass"], df["Survived"]))

# # Average Fare
# print("\nAVERAGE FARE:")
# print(df["Fare"].mean())

import pandas as pd

# Read the cleaned dataset
df = pd.read_excel("SWYNEX_Titanic_Data_Cleaned.xlsx")
df.columns = df.columns.str.strip()
print(df.columns.tolist())

# 1. Show dataset information
print("Dataset Shape:")
print(df.shape)

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Find average age
print("\nAverage Age:")
print(df["Age"].mean())

# 4. Count passengers who survived
print("\nSurvival Count:")
print(df["Survived"].value_counts())

# 5. Calculate survival percentage
print("\nSurvival Percentage:")
print(df["Survived"].value_counts(normalize=True) * 100)

# 6. Check survival by gender
print("\nSurvival by Gender:")
print(pd.crosstab(df["Sex"], df["Survived"]))

# 7. Check survival by passenger class
print("\nSurvival by Passenger Class:")
print(pd.crosstab(df["Pclass"], df["Survived"]))

# 8. Find average ticket fare
print("\nAverage Fare:")
print(df["Fare"].mean())
import matplotlib.pyplot as plt
import seaborn as sns

# Chart 1: Survival Count
sns.countplot(data=df, x="Survived")
plt.title("Titanic Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.savefig("survival_count.png")
plt.show()

# Chart 2: Survival by Gender
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Gender")
plt.savefig("survival_by_gender.png")
plt.show()

# Chart 3: Survival by Passenger Class
sns.countplot(data=df, x="Pclass", hue="Survived")
plt.title("Survival by Passenger Class")
plt.savefig("survival_by_class.png")
plt.show()
# 9. Five Useful Insights

print("\n--- Five Useful Insights ---")

# Insight 1: Total passengers
print("1. Total passengers:", len(df))

# Insight 2: Number of survivors
print("2. Passengers who survived:", (df["Survived"] == 1).sum())

# Insight 3: Survival by gender
print("3. Survival by gender:")
print(df.groupby("Sex")["Survived"].mean() * 100)

# Insight 4: Survival by passenger class
print("4. Survival by passenger class:")
print(df.groupby("Pclass")["Survived"].mean() * 100)

# Insight 5: Average ticket fare
print("5. Average ticket fare:", df["Fare"].mean())