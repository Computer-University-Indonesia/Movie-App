from src.models.Model import GetData
from src.utils.filter import getDataFiltered

df_rating = GetData('rating')

def getAllRating():
  return df_rating['rating'].value_counts().index


def getRatingFiltered(key, value):
    return getDataFiltered('rating', getAllRating, key, value)['rating']
