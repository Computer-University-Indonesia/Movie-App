from flask import Blueprint, request
import src.models.Cast as Cast
import src.utils.response as response
CastApp = Blueprint('CastApp', __name__)

@CastApp.route('/casts')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    casts = Cast.getAllCast()
    if (key != None and value != None):
      casts = Cast.getCastFiltered(key, value)
    return response.success(casts.to_list())
    # return response.success(Cast.getAllCast().to_list())
  except Exception as e:
    return response.error(e.args[0])
