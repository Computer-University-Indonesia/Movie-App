from src.models.Model import GetData
from src.utils.filter import getDataFiltered

df_type = GetData('type')


def getAllType():
  return df_type['type'].value_counts().index


def getTypeFiltered(key, value):
  return getDataFiltered('type', getAllType, key, value)['type']

