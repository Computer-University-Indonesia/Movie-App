from flask import Blueprint, request
import src.models.Type as Type
import src.utils.response as response
TypeApp = Blueprint('TypeApp', __name__)


@TypeApp.route('/types')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    types = Type.getAllType()
    if (key != None and value != None):
      types = Type.getTypeFiltered(key, value)
    return response.success(types.to_list())
  except Exception as e:
    return response.error(e.args[0])
