from flask import Flask

from src.controllers.GenresController import GenreApp
from src.controllers.CastController import CastApp
from src.controllers.TypeController import TypeApp
from src.controllers.DirectorController import DirectorApp
from src.controllers.RatingController import RatingApp
from src.controllers.CountryController import CountryApp
from src.config.config import BASE_URL, PORT, DEBUG
main_app = Flask(__name__)

main_app.register_blueprint(GenreApp)
main_app.register_blueprint(CastApp)
main_app.register_blueprint(TypeApp)
main_app.register_blueprint(DirectorApp)
main_app.register_blueprint(RatingApp)
main_app.register_blueprint(CountryApp)

print("Server is running on url: "+ BASE_URL +":", PORT)
if(__name__ == "__main__"):
  main_app.run()

