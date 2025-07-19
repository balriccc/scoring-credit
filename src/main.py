from load_data import load_data
from clean_data import clean_data
from preprocess import preprocess
from visualize import visualize

def run_all():
    df = load_data()
    df = clean_data(df)
    df = preprocess(df)
    visualize(df)

if __name__ == "__main__":
    run_all()
