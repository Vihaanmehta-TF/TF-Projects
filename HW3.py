#%%
import pandas as pd
import matplotlib.pyplot as plt

survey = pd.read_csv("class_survey.csv")
plt.figure(figsize=(9,5))
plt.bar(survey["pet"], survey["minutes_gaming"], color="#C1146B")
plt.title("Minutes gaming per each person's pet")
plt.xlabel("pet")
plt.ylabel("Minutes gaming")
plt.tight_layout()
plt.savefig("chart_one.png", dpi=150)
plt.figure(figsize=(9,5))
plt.scatter(survey["pet"], survey["minutes_gaming"], color="#C1146B")
plt.savefig("chart_two.png", dpi=150)
print(f"Finding one: most people had no pets")
print(f"Finding two: the person with the most minutes gaming had no pets")
# %%
