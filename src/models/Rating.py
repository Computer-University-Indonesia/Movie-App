from src.models.Model import GetData
from src.utils.filter import getDataFiltered
from src.utils.dataframe import formatDataFrame
df_rating = GetData('rating')

def getAllRating():
  return df_rating['rating'].value_counts().index


def getRatingFiltered(key, value):
    return getDataFiltered('rating', getAllRating, key, value)['rating']

def getRatingWithAllAttributes():
    return formatDataFrame(df_rating, 'rating', 'title')
