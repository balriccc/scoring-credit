from sklearn.preprocessing import MinMaxScaler

def preprocess(df):
    df['TotalDelinquencies'] = (df['NumberOfTime30-59DaysPastDueNotWorse'] +
                                df['NumberOfTime60-89DaysPastDueNotWorse'] +
                                df['NumberOfTimes90DaysLate'])
    scaler = MinMaxScaler()
    cols_to_scale = ['RevolvingUtilizationOfUnsecuredLines', 'DebtRatio', 'MonthlyIncome', 'age', 'TotalDelinquencies']
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    return df
