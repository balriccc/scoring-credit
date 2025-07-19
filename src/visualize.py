import matplotlib.pyplot as plt
import seaborn as sns

def visualize(df):
    print("Statistiques descriptives :")
    print(df.describe())

    plt.figure(figsize=(6,4))
    sns.countplot(x='SeriousDlqin2yrs', data=df)
    plt.title("Répartition des défauts de paiement (0 = non, 1 = oui)")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.histplot(df['age'], bins=30, kde=True)
    plt.title("Distribution de l'âge des clients")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.boxplot(x='SeriousDlqin2yrs', y='MonthlyIncome', data=df)
    plt.title("Revenu mensuel selon défaut de paiement")
    plt.show()

    plt.figure(figsize=(12,10))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Matrice de corrélation")
    plt.show()

    plt.figure(figsize=(8,6))
    sns.scatterplot(x='RevolvingUtilizationOfUnsecuredLines', y='DebtRatio', hue='SeriousDlqin2yrs', data=df, alpha=0.6)
    plt.title("Taux d'utilisation du crédit vs Ratio d'endettement")
    plt.show()
