from flask import Blueprint, request
import src.models.Type as Type
import src.utils.response as response
TypeApp = Blueprint('TypeApp', __name__)


@TypeApp.route('/types')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    types = Type.getAllType().to_list()
    if (key != None and value != None):
      types_filtered = Type.getTypeFiltered(key, value)
      types_renamed = types_filtered.rename(columns={0:'count'})
      types=types_renamed.to_dict(orient='records')
    return response.success(types)
  except Exception as e:
    return response.error(e.args[0])

@TypeApp.route('/types/grafik')
def grafik():
  try:
    types = Type.getTypeWithAllAttributes()
    return response.success(types.to_dict(orient='records'))
  except Exception as e:
    return response.error(e.args[0])