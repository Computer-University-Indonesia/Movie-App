from src.models.Model import GetData 

df_genre = GetData('genre')
  
def getAllGendre():
  # get  all gendre from df_genre and sort by most popular gendre and remove duplicates gendre
  return df_genre['listed_in'].value_counts().index
  # gendres = df_genre['listed_in'].value_counts
  
