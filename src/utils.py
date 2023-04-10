# src/utils.py
import pandas as pd

def read_csv(file_path):
    """
    Read a CSV file and return its contents as a pandas DataFrame.
    """
    return pd.read_csv(file_path)