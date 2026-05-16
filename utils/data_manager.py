import pandas as pd


DATA_FILE = "data/learning_data.csv"


def load_data():
    return pd.read_csv(DATA_FILE)


def save_data(dataframe):
    dataframe.to_csv(DATA_FILE, index=False)