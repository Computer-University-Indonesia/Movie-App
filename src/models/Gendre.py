from src.models.Model import GetData 
from src.utils.filter import getDataFiltered

df_genre = GetData('genre')

def getAllGendre():
  return df_genre['listed_in'].value_counts().index
  

def getGendreFiltered(key, value):
  return getDataFiltered('listed_in', getAllGendre, key, value)['listed_in']
