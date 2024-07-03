import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

hipoteka = pd.read_csv('Data/Stsr_AD_hip_ik_skolininkai_nuo_2021.csv', delimiter='|')

# Exploring data (types, missing values, statistical info)
# print(hipoteka.head())
# print(hipoteka.describe())
# print(hipoteka.info())

# Deleting data of credits taken by companies (rows)
print(hipoteka.imones.unique())
index_company = hipoteka[hipoteka['imones'] == 1].index
hipoteka.drop(index_company, inplace=True)

#  Deleting columns with unused data and checking data
hipoteka.drop(['st_nr', 'imones', 'skol_reg_data', 'st_isreg_ketv', 'pri_terminas_metai', 'formavimo_data',
               'st_sav_kodas_dm', 'st_aps_kodas', 'skol_amnt_grupe', 'skol_sal_grupe'], axis=1, inplace=True)
print(hipoteka.describe())
print(hipoteka.info())

# Exploring data in the columns with NaN values
print(f'\n NAN values: \n {hipoteka.isna().sum()}')

# Deleting rows with NAN values
hipoteka = hipoteka.dropna()
print(hipoteka.info())

# Exploring values of each column
print('\n Value counts')
for col in hipoteka.columns:
    print(hipoteka[col].value_counts())



#  Exploring data about municipalities, districts
print(hipoteka.st_sav_aps_pav.value_counts())

#  2 separate dataframes created for realizing EDA in 2 scopes: for 5 largest municipalities and 10 districts.

largest_mun = ['Vilniaus m. sav.', 'Kauno m. sav.', 'Klaipėdos m. sav.', 'Šiaulių m. sav.', 'Panevėžio m. sav.']
hipoteka_mun_5 = hipoteka.loc[hipoteka['st_sav_aps_pav'].isin(largest_mun)]
print(hipoteka_mun_5.st_sav_aps_pav.value_counts())

hipoteka.replace(to_replace=['Vilniaus m. sav.', 'Kauno m. sav.', 'Klaipėdos m. sav.', 'Šiaulių m. sav.',
                             'Panevėžio m. sav.'],
                             value=['Vilniaus apskr.', 'Kauno apskr.', 'Klaipėdos apskr.', 'Šiaulių apskr.',
                                    'Panevėžio apskr.'], inplace=True)
print(hipoteka.st_sav_aps_pav.value_counts())
print(hipoteka.info())

