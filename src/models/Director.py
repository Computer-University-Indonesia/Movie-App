from src.models.Model import GetData
from src.utils.filter import getDataFiltered
from src.utils.dataframe import formatDataFrame
df_director = GetData('director')


def getAllDirector():
  return df_director['director'].value_counts().index


def getDirectorFiltered(key, value):

  return getDataFiltered('director',getAllDirector, key, value)

def getDirectorWithAllAttributes():
  return formatDataFrame(df_director,'director','title')