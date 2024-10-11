import pandas as pd

data = pd.read_stata('Data.dta')

# print(data.describe(include='all'))

columns = ['Q17', 'PPEMPLOY', 'PPWORK', 'TQCIT1', 'PPAGE', 'PPETHM',  'PPGENDER', 'XACSNET', 'Q1E', 'Q1I', 'TQTEL1', 'Q12L_1', 'Q4', 'Q10B', 'Q8E', 'Q14B', 'Q13A']

new_data = data[columns].copy()

new_data = new_data.rename(columns={'Q17': 'Employment Type', 
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
unique_values = new_data['Medical debt status'].unique()
print(unique_values)
