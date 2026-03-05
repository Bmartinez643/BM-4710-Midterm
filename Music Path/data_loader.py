import pandas as pd

def load_dataset(filename):

    df = pd.read_csv(filename)

    df = df[['Artist', 'Title', 'Top Genre', 'Year', 'Beats Per Minute (BPM)']]

    df = df.dropna()

    return df 