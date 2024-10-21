import pandas as pd

data = pd.read_stata('Data.dta')

# ********************************  NEW DATA *******************************************

# Based on the codebook, these columns of interest are used to form a new dataset
columns = ['RID', 'WEIGHT1_NEW', 'Q1', 'Q1A_1', 'Q1A_2', 'Q1A_3', 'Q1A_4', 'Q1A_5', 'Q1A_6', 'Q1A_7', 'Q1A_8', 'Q1A_9', 'Q3D_1', 'Q3D_2', 'Q3D_4', 'Q3A_1', 'Q17', 'PPEMPLOY', 'PPWORK', 'TQCIT1', 'PPAGE', 'PPETHM',  'PPGENDER', 'XACSNET', 'Q1E', 'Q1I', 'TQTEL1', 'Q12L_1', 'Q4', 'Q10B', 'Q8E', 'Q14B', 'Q13A']

new_data = data[columns].copy()

# All columns were renamed for readability and comprehension purposes
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


# Columns were capitalised, Only the first letter is a capital letter
new_data.columns = new_data.columns.str.capitalize()



# **********************************  DISEASE DATA  *********************************************

# A new database was created, which focused on the diseases each patient has. The purpose of this was to combine all diseases of each patient and make them one entry (Disease)
disease_data = new_data[['Rid', 'Weight1_new',"Hypertension", "High cholesterol", "Heart conditions", "Stroke", "Cancer related", "Diabetis", "Asthma", "Copd", "Arthritis"]]

# Melt the data to get the diseases in a single column
disease_melted = disease_data.melt(id_vars=['Rid', 'Weight1_new'], var_name='Disease', value_name='Status')

# Filter the data to only include rows where the disease status is "Yes"
disease_melted = disease_melted[disease_melted['Status'] == 'Yes']

# Group by Rid and Weight1_new, and combine the diseases into a single entry
disease_combined = disease_melted.groupby(['Rid', 'Weight1_new'])['Disease'].apply(lambda x: ', '.join(x)).reset_index()

# Merge with the original DataFrame to ensure we include all 'RID' values
disease_combined_full = pd.merge(disease_data[['Rid', 'Weight1_new']], disease_combined, on=['Rid', 'Weight1_new'], how='left')

# Replace NaN values (where no diseases were found) with the string "None"
disease_combined_full['Disease'] = disease_combined_full['Disease'].fillna('None')



# **********************************  DISABILITY DATA *********************************************

# Followed the same process for the diseased data

disability_data = new_data[['Rid', 'Weight1_new', 'Hearing difficulty', 'Blindness', 'Difficulty walking']]

disability_melted = disability_data.melt(id_vars=['Rid', 'Weight1_new'], var_name='Disability', value_name='Status')

disability_melted = disability_melted[disability_melted['Status'] == 'Yes']

disability_combined = disability_melted.groupby(['Rid', 'Weight1_new'])['Disability'].apply(lambda x: ', '.join(x)).reset_index()

disability_combined_full = pd.merge(disability_data[['Rid', 'Weight1_new']], disability_combined, on=['Rid', 'Weight1_new'], how='left')

disability_combined_full['Disability'] = disability_combined_full['Disability'].fillna('None')



# ********************************** DATA WITHOUT DISEASES AND DISABILITIES  **************************************

# Dropping columns we have already worked on in the disease and disabilty dataset
newest_data = new_data.drop(["Hypertension", "High cholesterol", "Heart conditions", "Stroke", "Cancer related", "Diabetis", "Asthma", "Copd", "Arthritis", 'Hearing difficulty', 'Blindness', 'Difficulty walking', 'Covid-19 functional impairment', 'Marketplace plan type'], axis=1)


# ********************************** Handling missing datas in the newest data ***********************************

# List of columns to modify
columns_to_modify = ['Usa citizenship', 'Insurance coverage stability', 'Family income estimate']

# Looping through the columns and adding a "undisclosed" category and filling up the missing values
for col in columns_to_modify:
    newest_data[col] = newest_data[col].cat.add_categories('Undisclosed').fillna('Undisclosed')



# ********************************** Merging all three datas into a finall data ***********************************

# Merge newest_data and disease_combined_full on 'Rid'
merged_data = pd.merge(newest_data, disease_combined_full, on=['Rid', 'Weight1_new'], how='inner')  # You can change 'how' to 'left', 'right', or 'outer' as needed

# Merge the result with disability_combined_full on 'Rid', 'Weight1_new'
final_merged_data = pd.merge(merged_data, disability_combined_full, on=['Rid', 'Weight1_new'], how='inner')


final_data = final_merged_data[final_merged_data["Age"] >= 50]


# Converting the data type of the Age from category to integer so t can be worked upon easily
final_data['Age'] = final_data['Age'].cat.codes

print(final_data.info())

final_data.to_stata('final_data.dta', write_index=False)
final_data.to_csv('final_data.csv')