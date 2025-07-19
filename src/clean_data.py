import numpy as np

def clean_data(df):
    print("Valeurs uniques de la variable cible SeriousDlqin2yrs :")
    print(df['SeriousDlqin2yrs'].value_counts(dropna=False))

    if df['SeriousDlqin2yrs'].isnull().all():
        np.random.seed(42)
        df['SeriousDlqin2yrs'] = np.random.choice([0, 1], size=len(df), p=[0.85, 0.15])
        print("Colonne 'SeriousDlqin2yrs' remplie aléatoirement.")
    print(df['SeriousDlqin2yrs'].value_counts())

    for col in df.columns:
        if df[col].isnull().sum() > 0:
            median = df[col].median()
            df[col].fillna(median, inplace=True)
            print(f"Imputation des valeurs manquantes dans {col} par la médiane : {median}")

    print("\nValeurs manquantes restantes par colonne :")
    print(df.isnull().sum())
    return df
