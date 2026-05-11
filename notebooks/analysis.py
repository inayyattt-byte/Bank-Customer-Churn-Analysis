import pandas as pd

print("\n--- BANK CUSTOMER CHURN ANALYSIS ---\n")


# Load dataset
df = pd.read_csv("../data/data.csv")
print("\n--- DATASET OVERVIEW ---\n")
# Show first 5 rows
print(df.head())

# Show dataset info
print(df.info())

#--------------------------------------------------
# Average balance by country

print("\n--- AVERAGE BALANCE BY COUNTRY ---\n")
print(df.groupby("Geography")["Balance"].mean())


import matplotlib.pyplot as plt

country_balance = df.groupby("Geography")["Balance"].mean()

country_balance.plot(kind="bar")

plt.title("Average Balance by Country")
plt.xlabel("Country")
plt.ylabel("Average Balance")

plt.savefig("../images/average_balance_by_country.png")

plt.show()

#---------------------------------------------------------------

# Churn rate by country

country_churn = df.groupby("Geography")["Exited"].mean()
print("\n--- CUSTOMER CHURN RATE BY COUNTRY ---\n")
print(country_churn)

country_churn.plot(kind="bar")

plt.title("Customer Churn Rate by Country")
plt.xlabel("Country")
plt.ylabel("Churn Rate")

plt.savefig("../images/churn_by_country.png")

plt.show()

#---------------------------------------------------------------

# Churn by activity status

activity_churn = df.groupby("IsActiveMember")["Exited"].mean()
print("\n--- CUSTOMER CHURN BY ACTIVITY STATUS ---\n")
print(activity_churn)

activity_churn.plot(kind="bar")

plt.title("Customer Churn by Activity Status")
plt.xlabel("Activity Status")
plt.ylabel("Churn Rate")

plt.savefig("../images/activity_churn.png")

plt.show()

#---------------------------------------------------------------

# Churn by gender
gender_churn = df.groupby("Gender")["Exited"].mean()
print("\n--- CUSTOMER CHURN BY GENDER ---\n")
print(gender_churn)

gender_churn.plot(kind="bar")

plt.title("Customer Churn by Gender")
plt.xlabel("Gender")
plt.ylabel("Churn Rate")

plt.savefig("../images/gender_churn.png")

plt.show()

#---------------------------------------------------------------

# Average churn by age

age_churn = df.groupby("Age")["Exited"].mean()
print("\n--- CUSTOMER CHURN BY AGE GROUP ---\n")
print(age_churn)


df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[18, 30, 45, 60, 100],
    labels=["18-30", "31-45", "46-60", "60+"]
)


age_group_churn = df.groupby("AgeGroup")["Exited"].mean()

print(age_group_churn)


age_group_churn.plot(kind="bar")

plt.title("Customer Churn by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Churn Rate")

plt.savefig("../images/age_group_churn.png")

plt.show()

#---------------------------------------------------------------

print("\n----------------------------")
print("ANALYSIS COMPLETE")
print("------------------------------\n")