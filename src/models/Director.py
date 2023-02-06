from src.models.Model import GetData
from src.utils.filter import getDataFiltered

df_director = GetData('director')


def getAllDirector():
  return df_director['director'].value_counts().index


def getDirectorFiltered(key, value):

  return getDataFiltered('director',getAllDirector, key, value)['director']
