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

# Deleting data of credits taken by companies
print(hipoteka.imones.unique())
index_company = hipoteka[hipoteka['imones'] == 1].index
hipoteka.drop(index_company, inplace=True)

#  Deleting columns with unused data
hipoteka.drop(['st_nr', 'imones', 'skol_reg_data', 'st_isreg_ketv', 'pri_terminas_metai', 'formavimo_data',
               'st_sav_kodas_dm', 'st_aps_kodas', 'skol_amnt_grupe', 'skol_sal_grupe', 'iraso_priezastis'], axis=1, inplace=True)

# Detecting NaN values
print(hipoteka.info())
print(f'\n NAN values: \n {hipoteka.isna().sum()}')

# Deleting rows with NAN values
hipoteka = hipoteka.dropna()
print(hipoteka.info())

# Exploring values of each column
print('\nValue counts')
for col in hipoteka.columns:
    print(hipoteka[col].value_counts())

# Deleting data related to pledging (keeping just mortgages)
index_pledges = hipoteka[(hipoteka['st_tipas'] == 'Sutartinis_ikeitimas') |
                         (hipoteka['st_tipas'] == 'Priverstinis_ikeitimas')].index
hipoteka.drop(index_pledges, inplace=True)

#  Max mortgage amount - from str to integer
hipoteka['max_amount'] = hipoteka['pri_dydis_rez']
hipoteka['max_amount'] = hipoteka['max_amount'].replace('iki 10 tūk.', 10000)
hipoteka['max_amount'] = hipoteka['max_amount'].replace('nuo 10 tūk. iki 50 tūk.', 50000)
hipoteka['max_amount'] = hipoteka['max_amount'].replace('nuo 50 tūk. iki 100 tūk.', 100000)
hipoteka['max_amount'] = hipoteka['max_amount'].replace('nuo 100 tūk. iki 500 tūk.', 500000)
hipoteka['max_amount'] = hipoteka['max_amount'].replace('nuo 500 tūk. Iki 1 mln.', 1000000)
hipoteka['max_amount'] = hipoteka['max_amount'].replace('nuo 1 mln. Iki 5 mln.', 5000000)
hipoteka['max_amount'] = hipoteka['max_amount'].replace('nuo 5 mln. Iki 10 mln.', 10000000)
hipoteka['max_amount'] = hipoteka['max_amount'].replace('nuo 10 mln. Iki 50 mln.', 50000000)
hipoteka['max_amount'] = hipoteka['max_amount'].replace('nuo 50 mln. Iki 100 mln.', 100000000)

hipoteka.drop('pri_dydis_rez', axis=1, inplace=True)

#  Detecting outliers
plt.figure(figsize=(12, 12))
sns.boxplot(x=hipoteka['skol_amziaus_grupe'], y=hipoteka['max_amount'])
plt.show()

print(hipoteka.max_amount.value_counts())

#  Removing outliers
max_amount_out = hipoteka[hipoteka['max_amount'] >= 1000000].index
hipoteka.drop(max_amount_out, inplace=True)
print(hipoteka.max_amount.value_counts())

plt.figure(figsize=(12, 6))
sns.boxplot(x=hipoteka['max_amount'])
plt.show()

#  Exploring data about municipalities, districts
print(hipoteka.st_sav_aps_pav.value_counts())

#  Creating 2 separate dataframes for realizing EDA in 2 scopes: for 5 largest municipalities and 10 districts.
largest_mun = ['Vilniaus m. sav.', 'Kauno m. sav.', 'Klaipėdos m. sav.', 'Šiaulių m. sav.', 'Panevėžio m. sav.']
hipoteka_mun_5 = hipoteka.loc[hipoteka['st_sav_aps_pav'].isin(largest_mun)]
print(hipoteka_mun_5.st_sav_aps_pav.value_counts())

hipoteka.replace(to_replace=['Vilniaus m. sav.', 'Kauno m. sav.', 'Klaipėdos m. sav.', 'Šiaulių m. sav.',
                             'Panevėžio m. sav.'],
                             value=['Vilniaus apskr.', 'Kauno apskr.', 'Klaipėdos apskr.', 'Šiaulių apskr.',
                                    'Panevėžio apskr.'], inplace=True)
print(hipoteka.st_sav_aps_pav.value_counts())
print(hipoteka.info())
print(hipoteka.head())
