#%%
import pandas as pd
import matplotlib.pyplot as plt
snacks = pd.read_csv("snack_votes.csv")
ranked = snacks.sort_values("votes",ascending=False)
plt.figure(figsize=(9,5))
plt.bar(ranked["snack"], ranked["votes"], color="#F26419")
plt.title("Favorite snacks in our class")
plt.xlabel("Snack")
plt.ylabel("Number of Votes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("snack_chart.png")
winner = ranked.iloc[0]
print(f"{winner['snack']} won with {winner['votes']} votes")
print(f"Total votes cast: {snacks['votes'].sum()}")
# %%
