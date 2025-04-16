
import pandas as pd

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, dataframe: pd.DataFrame):
        dataframe.to_csv(self.filename, index=False)
