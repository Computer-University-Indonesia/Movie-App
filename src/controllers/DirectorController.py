from flask import Blueprint,request
import src.models.Director as Director
import src.utils.response as response
DirectorApp = Blueprint('DirectorApp', __name__)


@DirectorApp.route('/directors')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    directors = Director.getAllDirector()
    if (key != None and value != None):
      directors = Director.getDirectorFiltered(key, value)
    return response.success(directors.to_list())
  except Exception as e:
    return response.error(e.args[0])
