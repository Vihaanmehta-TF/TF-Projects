#%%
import pandas as pd
import matplotlib.pyplot as plt
survey = pd.read_csv('class_survey_v2.csv')

#i want to see how many missing values are there

#print(survey.isna().sum()) #isna = is 'not applicable'
#pandas treats None as a missing value
#It also treats NaN, NA, and N/A as missing value

#Next we will fix data inconsistency
#%%
#print(survey['grade'].unique()) #how many unique values are there in the grade column
# %%
#grade_map = {'6': 6, '6th': 6, 'six': 6, '7': 7, '7th': 7} #this mapping fits our current data but let's add some more
grade_map = {'6': 6, '6th': 6, 'six': 6, '7': 7, '7th': 7, 'seven': 7} #in case more data gets added later and there is a 'seven'

#now we are going to change the values in the csv
#strings are a collection of characters - like words or sentences
survey['grade'] = (survey['grade'].astype(str).str.strip().map(grade_map))
#get the current grade, remove spaces from around it, and then map it to the grade_map we created above
#print(survey)

#Fixing the fav subject: MATH, math, P.E, etc etc

survey['favorite_subject'] = survey['favorite_subject'].str.strip().str.title()
# it prints as a title would - first letter capital and everything else small
#print(survey['favorite_subject'].unique())

#PE got messed up becuase we forced everything to be a title whereas PE should have been left as-is
survey['favorite_subject'] = survey['favorite_subject'].replace({'P.E.': 'PE', 'Pe': 'PE'})

#print(survey['favorite_subject'].unique())

#print(survey.duplicated().sum()) #how many duplicates are there
survey = survey.drop_duplicates()
#print(survey)

#check for impossibilities
print(survey['hours_sleep'].describe())
survey.loc[survey['hours_sleep'] > 24,'hours_sleep'] = pd.NA
#survey.loc[survey['hours_sleep'] > 24,'hours_sleep'] = NA ----this doesnt work without a pd.NA
#the above line locates the records where sleep > 24 hrs, and updates the sleep column to NA. pd.NA -> specifies
#the pandas format of NA. Try what happens with just NA

#%%
#WEEK 7
survey['grade'].value_counts()
survey['favorite_subject'].value_counts()

#Split, Apply, Combine
survey.groupby('grade')['minutes_gaming'].mean()