import pandas as pd
import numpy as np
from html_table_parser.parser import HTMLTableParser
from src.config.scraping import url_get_contents
from src.config.config import SCRAPING_URL
from src.config.cleaning import data_cleaning as cleaning

def GetData(type):
  print('Getting data from:', SCRAPING_URL)

  xhtml=url_get_contents(SCRAPING_URL).decode('utf-8')
  
  p = HTMLTableParser()

  p.feed(xhtml)
  df = pd.DataFrame(p.tables[0])
  df = df.replace(r'^\s*$', np.nan, regex=True)

  df.columns = df.iloc[0]
  return cleaning(df, type)
