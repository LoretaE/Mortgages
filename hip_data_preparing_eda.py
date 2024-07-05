import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def data_for_eda(failas):
    # Load the dataset
    hipoteka = pd.read_csv(failas)

    #  Converting dates to quarters
    hipoteka['date_quarter'] = (hipoteka['st_ireg_ketv'].str.split('-').str[0] + 'Q' +
                                 hipoteka['st_ireg_ketv'].str.split('-').str[1])
    hipoteka['date_quarter'] = pd.to_datetime(hipoteka['date_quarter']).dt.to_period('Q')

    #  Converting categorical data to datatype "category"
    col = ['skol_amziaus_grupe', 'st_tipas', 'st_sav_aps_pav', 'maksimalus', 'paprastas', 'jungtinis', 'svetimas',
           'bendras', 'salyginis', 'pareikstinis']
    for c in col:
        hipoteka[c] = hipoteka[c].astype('category')

    #  Converting age category from string to interval[int64]
    age_conv = {'nuo_18_iki_25': 22, 'nuo_25_iki_35': 30, 'nuo_35_iki_45': 40, 'nuo_45_iki_55': 50,
                'nuo_55_iki_65': 60, 'nuo_65_iki_85': 75}
    hipoteka['age'] = hipoteka['skol_amziaus_grupe'].map(age_conv)

    age_bins = [18, 25, 35, 45, 55, 65, 85]
    age_cats = pd.cut(hipoteka.age, age_bins, right=False)
    hipoteka['age_group'] = age_cats

    #  Removing unused columns
    hipoteka = hipoteka.drop(['skol_amziaus_grupe', 'age', 'st_ireg_ketv'], axis=1)

    #  Renaming columns and category names
    hipoteka.rename(columns={'st_tipas': 'Type of mortgage', 'maksimalus': 'Max mortgage',
                             'st_sav_aps_pav': 'District', 'paprastas': 'Ordinary mortgage',
                             'jungtinis': 'Joint mortgage', 'svetimas': 'Mortgage on someone else property',
                             'bendras': 'Shared mortgage',  'salyginis': 'Conditional mortgage',
                             'pareikstinis': 'Bearer mortgage'}, inplace=True)

    hip_type = {'Sutartine_hipoteka': 'Contractual mortgage', 'Priverstine_hipoteka': 'Compulsory mortgage'}
    hipoteka['Type of mortgage'] = hipoteka['Type of mortgage'].map(hip_type)

    return hipoteka


def districts_10(hipoteka):
    #  Dataframe for realizing EDA for 10 districts.
    mun_conv = {'Vilniaus m. sav.': 'Vilnius', 'Vilniaus apskr.': 'Vilnius', 'Kauno m. sav.': 'Kaunas',
                'Kauno apskr.': 'Kaunas', 'Klaipėdos m. sav.': 'Klaipėda', 'Klaipėdos apskr.': 'Klaipėda',
                'Šiaulių m. sav.': 'Šiauliai', 'Šiaulių apskr.': 'Šiauliai', 'Panevėžio m. sav.': 'Panevėžys',
                'Panevėžio apskr.': 'Panevėžys', 'Alytaus apskr.': 'Alytus', 'Marijampolės apskr.': 'Marijampolė',
                'Tauragės apskr.': 'Tauragė', 'Telšių apskr.': 'Telšiai', 'Utenos apskr.': 'Utena'}
    districts = hipoteka.copy()
    districts['District'] = districts['District'].map(mun_conv)
    districts.to_csv('Data\districts.csv', index=False)
    return districts


def eda(districts):

    # Visualising data - mortgages and features (total and in districts)

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=districts, x='age_group', y='max_amount', hue='Type of mortgage')
    plt.title(f'Mortgage Distribution in Districts by Age')
    plt.xlabel('Age group')
    plt.ylabel('Max mortgage amount')
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=districts, x='District', y='max_amount', hue='Type of mortgage')
    plt.title(f'Mortgage Distribution in Districts')
    plt.xlabel('District')
    plt.ylabel('Max mortgage amount')
    plt.show()

    g = sns.FacetGrid(data=districts, col='District', col_wrap=2, height=4)
    g.map(sns.boxplot, 'age_group', 'max_amount')
    g.set_axis_labels('Age group', 'Max mortgage amount')
    plt.show()

    plt.figure(figsize=(12, 6))
    districts.sort_values(['date_quarter'], inplace=True)
    sns.countplot(data=districts, x='date_quarter', hue='Type of mortgage')
    plt.title('Mortgages Trend')
    plt.xlabel('Date (Quarters)')
    plt.ylabel('Frequency')
    plt.show()

    g = sns.FacetGrid(data=districts, col='District', col_wrap=2, height=4)
    g.map(sns.countplot, 'date_quarter', order=['2021Q1', '2021Q2', '2021Q3', '2021Q4', '2022Q1', '2022Q2',
                                                '2022Q3', '2022Q4', '2023Q1', '2023Q2', '2023Q3'])
    g.set_axis_labels('Date (quarter)', 'Frequency')
    g.set_xticklabels(labels=['2021Q1', '2021Q2', '2021Q3', '2021Q4', '2022Q1', '2022Q2', '2022Q3', '2022Q4', '2023Q1',
                              '2023Q2', '2023Q3'], rotation=90)
    plt.tight_layout()
    plt.show()


def main():
    #  Loading and preparing data for EDA (converting to categories, time periods)
    hipoteka = data_for_eda('Data/hipoteka_clean.csv')
    print(hipoteka.info())

    #  Preparing  data frame for EDA (10 districts)
    districts = districts_10(hipoteka)

    # Performing EDA on the filtered data frame
    eda(districts)


if __name__ == '__main__':
    main()
