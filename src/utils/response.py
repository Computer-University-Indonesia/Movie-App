from flask import jsonify
def success(data):
  response = jsonify( {
    'status_code': 200,
    'message': 'success',
    'data': data
  })
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response
   
def error(message):
    response = jsonify({
      'status_code': 400,
      'message': message,
      'data': None
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
