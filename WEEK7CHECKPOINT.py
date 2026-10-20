#%%
import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv('class_survey_v2_clean.csv')
survey['grade'].value_counts()

# %%
survey.groupby('grade')['hours_sleep'].agg(['mean', 'count']).round(1).sort_values('mean', ascending=False)

# %%
