from flask import Blueprint
import src.models.Type as Type
import src.utils.response as response
TypeApp = Blueprint('TypeApp', __name__)


@TypeApp.route('/types')
def index():
  try:
    return response.success(Type.getAllType().to_list())
  except Exception as e:
    return response.error(e.args[0])
