from src.models.Model import GetData
from src.utils.filter import getDataFiltered
from src.utils.dataframe import  formatDataFrame
import random
df_cast = GetData('cast')

def getAllCast():
  return df_cast['cast'].value_counts().index


def getCastFiltered(key, value):
  return getDataFiltered('cast', getAllCast, key, value)['cast']

def getAllCastWithAllAttributes():
  return formatDataFrame(df_cast,'cast','title')