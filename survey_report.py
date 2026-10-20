#%%
import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv("class_survey.csv")
print(len(survey))
gamers = survey[survey["minutes_gaming"] >60 ]
print(len(gamers))
print(len(survey))
#columns
survey["pet"]
survey[["pet", "hours_sleep"]]
#rows
survey["minutes_gaming"] >60
#boolean table true or false statement
gamers = survey[survey["minutes_gaming"] > 60]
survey[survey["pet"] == "dog"]
survey[survey["pet"].isin(["dog", "cat"])]

gamers[gamers["hours_sleep"] < 8.0]
survey[(survey["minutes_gaming"] > 60) & (survey["hours_sleep"] < 8)]


survey["hours_gaming"] = survey["minutes_gaming"] / 60
survey.head()

survey["screen_vs_book"] = survey["minutes_gaming"] - survey["minutes_reading"]
survey.sort_values(
    ["grade",  "minutes_reading"], ascending=[True, False])
survey["hours_sleep"].describe()
plt.savefig("survey_report.png")
# %%
