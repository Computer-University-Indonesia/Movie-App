from flask import Blueprint, request
import src.models.Cast as Cast
import src.utils.response as response
CastApp = Blueprint('CastApp', __name__)

@CastApp.route('/casts')
def index():
  try:
    key = request.args.get('key')
    value = request.args.get('value')
    casts = Cast.getAllCast().to_list()
    if (key != None and value != None):
      casts_filtered = Cast.getCastFiltered(key, value)
      casts_renamed = casts_filtered.rename(columns={0: 'count'})
      casts = casts_renamed.to_dict(orient='records')
    return response.success(casts)
    # return response.success(Cast.getAllCast().to_list())
  except Exception as e:
    return response.error(e.args[0])

@CastApp.route('/casts/grafik')
def grafik():
  try:
    
    return response.success(Cast.getAllCastWithAllAttributes().to_dict(orient='records'))
    
  except Exception as e:
    return response.error(e.args[0])