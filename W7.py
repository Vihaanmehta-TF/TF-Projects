import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv('class_survey_v2_clean.csv')
survey['pet'] = survey['pet'].replace({'BIRD': 'Bird', 'FISH': 'Fish', 'HAMSTER': 'Hamster'})
survey['grade'].value_counts()
s=survey['favorite_subject'].value_counts
f=survey.groupby('grade')['minutes_gaming'].mean()
avg=(survey.groupby('favorite_subject')
    ['minutes_reading'].mean().round(1).sort_values(ascending=False)
)

survey['pet'].value_counts
survey.groupby('pet')['minutes_gaming'].mean().round(1).sort_values(ascending=False)
survey['pet'] = survey['pet'].str.title()
survey['pet'] = survey['pet'].fillna('No pet')
survey['pet'].value_counts()
survey.groupby('pet')['minutes_gaming'].mean().round(1)
survey.groupby('favorite_subject')['minutes_reading'].agg(['mean', 'count']).round(1).sort_values('mean', ascending=False)
plt.bar(avg.index, avg.values, color='#2A9D8F')
plt.title('Average Minutes Reading by Favorite Subject')
plt.xlabel('Favorite Subject')
plt.ylabel('Average Minutes Reading')
plt.savefig('reading_by_subject.png')
