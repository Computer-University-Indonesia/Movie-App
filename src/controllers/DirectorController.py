from flask import Blueprint
import src.models.Director as Director
import src.utils.response as response
DirectorApp = Blueprint('DirectorApp', __name__)


@DirectorApp.route('/directors')
def index():
  try:
    return response.success(Director.getAllDirector().to_list())
  except Exception as e:
    return response.error(e.args[0])
