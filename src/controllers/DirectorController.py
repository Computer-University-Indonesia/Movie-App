from flask import Blueprint,request
import src.models.Director as Director
import src.utils.response as response
DirectorApp = Blueprint('DirectorApp', __name__)


@DirectorApp.route('/directors')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    directors = Director.getAllDirector().to_list()
    if (key != None and value != None):
      directors_filtered = Director.getDirectorFiltered(key, value)
      directors_renamed = directors_filtered.rename(columns={0: 'count'})
      directors = directors_renamed.to_dict(orient='records')
    return response.success(directors)
  except Exception as e:
    return response.error(e.args[0])

@DirectorApp.route('/directors/grafik')
def grafik():
  try:
    directors = Director.getDirectorWithAllAttributes()
    return response.success(directors.to_dict(orient='records'))
  except Exception as e:
    return response.error(e.args[0])