import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv('class_survey_v2.csv')
survey = survey.drop_duplicates()
#print(survey['favorite_subject'].unique())
survey['grade'] = survey['grade'].replace({'7th': '7', 'six': '6', '6th': '6'})
survey['favorite_subject'] = survey['favorite_subject'].replace({'P.E.': 'PE', 'pe': 'PE', 'science': 'Science', 'art': 'Art', 'Art ': 'Art', 'Math ': 'Math', 'MATH': 'Math', 'math': 'Math', 'english': 'English','English ': 'English', 'history': 'History', 'History ': 'History'})
survey['pet'] = survey['pet'].replace({'BIRD': 'Bird', 'FISH': 'Fish', 'HAMSTER': 'Hamster'})
survey.loc[survey['hours_sleep'] > 24,'hours_sleep'] = pd.NA
survey['hours_sleep'] =  survey['hours_sleep'].replace({'': 'Not given'})
survey.to_csv('class_survey_v2_clean.csv')
print("The dataset before had 43 lines but the clean dataset has 42 lines because of the one line that got dropped because its number of hours slept in a day was 99 which is impossible. For the missing hours of sleep values I left them empty because if there is no information provided I don't need to put any information in. The grade column was messy because it had things like 7th and six and not just 6 and 7. My code fixed this by replacing each alternate form with the correct form. I corrected 7th into 7 and six and 6th into 6.")
