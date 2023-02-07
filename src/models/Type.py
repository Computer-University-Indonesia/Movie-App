from src.models.Model import GetData
from src.utils.filter import getDataFiltered
from src.utils.dataframe import formatDataFrame
df_type = GetData('type')


def getAllType():
  return df_type['type'].value_counts().index


def getTypeFiltered(key, value):
  return getDataFiltered('type', getAllType, key, value)['type']

def getTypeWithAllAttributes():
  return formatDataFrame(df_type, 'type','title')