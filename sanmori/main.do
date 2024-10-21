* ********************************** 1. Load Data *******************************************
* Load the dataset (assuming the file is in the same directory)
use "Data.dta", clear

* ********************************** 2. Keep Relevant Columns *******************************************
* Keep only the columns of interest
keep RID WEIGHT1_NEW Q1 Q1A_1 Q1A_2 Q1A_3 Q1A_4 Q1A_5 Q1A_6 Q1A_7 Q1A_8 Q1A_9 Q3D_1 Q3D_2 Q3D_4 Q3A_1 Q17 PPEMPLOY PPWORK TQCIT1 PPAGE PPETHM PPGENDER XACSNET Q1E Q1I TQTEL1 Q12L_1 Q4 Q10B Q8E Q14B Q13A

* ********************************** 3. Rename Columns *******************************************
* Rename columns for better readability
rename Q1 Health_Status
rename Q1A_1 Hypertension
rename Q1A_2 High_Cholesterol
rename Q1A_3 Heart_Conditions
rename Q1A_4 Stroke
rename Q1A_5 Cancer_Related
rename Q1A_6 Diabetes
rename Q1A_7 Asthma
rename Q1A_8 COPD
rename Q1A_9 Arthritis
rename Q3D_1 Hearing_Difficulty
rename Q3D_2 Blindness
rename Q3D_4 Difficulty_Walking
rename Q3A_1 Accessibility_Needs
rename Q17 Employment_Type
rename PPEMPLOY Employment_Status
rename PPWORK Employment_Type_Status
rename TQCIT1 USA_Citizenship
rename PPAGE Age
rename PPETHM Race_Ethnicity
rename PPGENDER Gender
rename XACSNET Internet_Access
rename Q1E Covid19
rename Q1I Covid19_Functional_Impairment
rename TQTEL1 Telehealth_Visit_History
rename Q12L_1 Missed_Visit_Transportation
rename Q4 Health_Care_Access
rename Q10B Insurance_Coverage_Stability
rename Q8E Marketplace_Plan_Type
rename Q14B Family_Income_Estimate
rename Q13A Medical_Debt_Status

* ********************************** 4. Handle Disease Data (Reshape) *******************************************
* Reshape the disease columns from wide to long format
reshape long Hypertension High_Cholesterol Heart_Conditions Stroke Cancer_Related Diabetes Asthma COPD Arthritis, i(RID WEIGHT1_NEW) j(Disease)

* Keep only rows where the disease status is "Yes"
drop if Hypertension != "Yes" & High_Cholesterol != "Yes" & Heart_Conditions != "Yes" & Stroke != "Yes" & Cancer_Related != "Yes" & Diabetes != "Yes" & Asthma != "Yes" & COPD != "Yes" & Arthritis != "Yes"

* Group diseases for each patient
bysort RID WEIGHT1_NEW: egen Disease_Group = concat(Hypertension High_Cholesterol Heart_Conditions Stroke Cancer_Related Diabetes Asthma COPD Arthritis)

* ********************************** 5. Handle Disability Data (Reshape) *******************************************
* Reshape the disability columns from wide to long format
reshape long Hearing_Difficulty Blindness Difficulty_Walking, i(RID WEIGHT1_NEW) j(Disability)

* Keep only rows where disability status is "Yes"
drop if Hearing_Difficulty != "Yes" & Blindness != "Yes" & Difficulty_Walking != "Yes"

* Group disabilities for each patient
bysort RID WEIGHT1_NEW: egen Disability_Group = concat(Hearing_Difficulty Blindness Difficulty_Walking)

* ********************************** 6. Handle Missing Data *******************************************
* Add "Undisclosed" category for USA Citizenship, Insurance Coverage Stability, and Family Income Estimate
replace USA_Citizenship = "Undisclosed" if USA_Citizenship == ""
replace Insurance_Coverage_Stability = "Undisclosed" if Insurance_Coverage_Stability == ""
replace Family_Income_Estimate = "Undisclosed" if Family_Income_Estimate == ""

* ********************************** 7. Merge Data *******************************************
* Merge the disease and disability datasets with the main data
merge 1:1 RID WEIGHT1_NEW using disease_combined_full
merge 1:1 RID WEIGHT1_NEW using disability_combined_full

* ********************************** 8. Filter Age and Save Data *******************************************
* Keep only rows where Age is greater than or equal to 50
drop if Age < 50

* Save the final data as a .dta file
save "final_data.dta", replace
