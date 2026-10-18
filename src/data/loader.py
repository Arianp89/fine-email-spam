import pathlib

import pandas as pd
import logging
from pathlib import Path

def load_data():
  try:
    path = pathlib.Path(__file__).resolve().parents[2] / "data" / "raw" / "spam.csv"
    df = pd.read_csv(path , encoding="latin-1")
  except Exception as e:
   logging.error(e)
   return  False
  return df







