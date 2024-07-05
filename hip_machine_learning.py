import pandas as pd
from sklearn.model_selection import train_test_split

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def data_for_ml(failas):
    # Load the dataset
    districts = pd.read_csv(failas)

    """Feature Engineering"""
    # Separating target and features
    target = districts.max_amount.copy()
    features = districts.drop('max_amount', axis=1)

    # Transforming categorical variables to binary variables
    dummies = pd.get_dummies(features['Type of mortgage'], drop_first=True).astype(int)
    dummies1 = pd.get_dummies(features['District']).astype(int)
    dummies2 = pd.get_dummies(features['date_quarter']).astype(int)
    dummies3 = pd.get_dummies(features['age_group']).astype(int)

    features = pd.concat([features.drop(['Type of mortgage', 'District', 'date_quarter', 'age_group'],
                                        axis=1), dummies, dummies1, dummies2, dummies3], axis=1)

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, train_size=0.3, random_state=101)

    return X_train, X_test, y_train, y_test


def main():
    # Loading and preprocessing data for machine learning
    X_train, X_test, y_train, y_test = data_for_ml('Data/districts.csv')
    print(X_train, X_test, y_train, y_test)


if __name__ == '__main__':
    main()
