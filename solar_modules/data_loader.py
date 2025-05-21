import pandas as pd

class DataLoader:
    def __init__(self, filepath, parse_dates=["Timestamp"]):
        self.filepath = filepath
        self.parse_dates = parse_dates
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.filepath, parse_dates=self.parse_dates)
        return self.df
