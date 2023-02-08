from flask import Blueprint, request
import src.models.Gendre as Gendre
import src.utils.response as response
GenreApp = Blueprint('GenreApp', __name__, url_prefix='/gendres')


@GenreApp.get('/')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    gendres = Gendre.getAllGendre().to_list()
    if(key != None and value != None) : 
      gendres_filtered = Gendre.getGendreFiltered(key, value)
      gendres_renamed = gendres_filtered.rename(columns={0:'count','listed_in':'genre'})
      gendres = gendres_renamed.to_dict(orient='records')
    return response.success(gendres)
  except  Exception as e:
    return response.error( e.args[0])

@GenreApp.get('/grafik')
def grafik():
  try:
    gendres = Gendre.getGendreWithAllAttributes()
    return response.success(gendres.to_dict(orient='records'))
  except Exception as e:
    return response.error( e.args[0])