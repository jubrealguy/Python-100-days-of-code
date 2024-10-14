import pandas as pd

data = pd.read_stata('Data.dta')

columns = ['RID', 'WEIGHT1_NEW', 'Q1', 'Q1A_1', 'Q1A_2', 'Q1A_3', 'Q1A_4', 'Q1A_5', 'Q1A_6', 'Q1A_7', 'Q1A_8', 'Q1A_9', 'Q3D_1', 'Q3D_2', 'Q3D_4', 'Q3A_1', 'Q17', 'PPEMPLOY', 'PPWORK', 'TQCIT1', 'PPAGE', 'PPETHM',  'PPGENDER', 'XACSNET', 'Q1E', 'Q1I', 'TQTEL1', 'Q12L_1', 'Q4', 'Q10B', 'Q8E', 'Q14B', 'Q13A']

new_data = data[columns].copy()

new_data = new_data.rename(columns={'Q1' : 'Health Status', 'Q1A_1' : 'Hypertension',
                                    'Q1A_2' : 'High cholesterol', 'Q1A_4' : 'Stroke', 'Q1A_5' : 'Cancer Related', 'Q1A_6' : 'Diabetis', 'Q1A_7' : 'Asthma', 'Q1A_8' : 'COPD', 'Q1A_9' : 'Arthritis',
                                    'Q1A_3' : 'Heart Conditions', 'Q3D_1' : 'Hearing Difficulty', 'Q3D_2' : 'Blindness', 'Q3D_4' : 'Difficulty Walking', 'Q3A_1' : 'Accessibility Needs',
                                    'Q17': 'Employment Type', 
                                    'PPEMPLOY': 'Employment Status', 
                                    'PPWORK' : 'Employment Type & Status', 
                                    'TQCIT1' : 'USA Citizenship', 
                                    'PPAGE' : 'AGE',
                                    'PPETHM' : 'RACE / ETHNICITY',
                                    'PPGENDER': 'GENDER',
                                    'XACSNET' : 'INTERNET ACCESS',
                                    'Q1E' : 'COVID-19',
                                    'Q1I' : 'COVID-19 FUNCTIONAL IMPAIRMENT',
                                    'TQTEL1' : 'TELEHEALTH VISIT HISTORY',
                                    'Q12L_1' : 'MISSED VISIT TRANSPORTATION',
                                    'Q4' : 'HEALTH CARE ACCESS',
                                    'Q10B' : 'INSURANCE COVERAGE STABILITY',
                                    'Q8E' : 'MARKETPLACE PLAN TYPE',
                                    'Q14B' : 'FAMILY INCOME ESTIMATE',
                                    'Q13A' : 'MEDICAL DEBT STATUS'})

new_data.columns = new_data.columns.str.capitalize()

print(new_data.info())
unique_values = new_data['Health status'].unique()
print(unique_values)

# data = pd.read_stata('Data.dta')

# for column in data.columns:
#     value_counts = data[column].value_counts()
    
#     if (value_counts == 915).any():
#         print(f"Column '{column}' has a unique value with a count of 350")
#         break
# else:
#     print("No column has a unique value with a count of 350")