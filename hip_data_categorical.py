import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Load the dataset
hipoteka = pd.read_csv('Data/hipoteka_clean.csv', parse_dates=['st_ireg_ketv'])
print(hipoteka.head())

#  Converting dates to quarters
hipoteka['date_quarter'] = hipoteka['st_ireg_ketv'].dt.to_period('Q')

#  Converting categorical data to datatype "category"
col = ['skol_amziaus_grupe', 'st_tipas', 'st_sav_aps_pav', 'maksimalus', 'paprastas', 'jungtinis', 'svetimas',
       'bendras', 'salyginis', 'pareikstinis']
for c in col:
    hipoteka[c] = hipoteka[c].astype('category')

print(hipoteka.info())

#  Converting age category from string to interval[int64]
age_conv = {'iki_18': 10, 'nuo_18_iki_25': 22, 'nuo_25_iki_35': 30, 'nuo_35_iki_45': 40, 'nuo_45_iki_55': 50,
            'nuo_55_iki_65': 60, 'nuo_65_iki_85': 75, 'nuo_85': 90}
hipoteka['age'] = hipoteka['skol_amziaus_grupe'].map(age_conv)

age_bins = [0, 18, 25, 35, 45, 55, 65, 85, 100]
age_cats = pd.cut(hipoteka.age, age_bins, right=False)
hipoteka['age_group'] = age_cats
print(hipoteka.age_group.value_counts())

#  Removing unused columns
hipoteka = hipoteka.drop(['skol_amziaus_grupe', 'age', 'st_ireg_ketv'], axis=1)
print(hipoteka.info())

print(hipoteka.head())
hipoteka.to_csv('Data/hipoteka_cat.csv', index=False)
