import pandas as pd

def load_data():
    url = "https://raw.githubusercontent.com/balriccc/scoring-credit/main/data/cs-training.csv"
    df = pd.read_csv(url, index_col=0)
    return df
