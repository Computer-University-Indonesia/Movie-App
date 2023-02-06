from src.models.Model import GetData
from src.utils.filter import getDataFiltered

df_cast = GetData('cast')

def getAllCast():
  return df_cast['cast'].value_counts().index


def getCastFiltered(key, value):
  return getDataFiltered('cast', getAllCast, key, value)['cast']
