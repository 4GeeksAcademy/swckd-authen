<<<<<<< HEAD
"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
from flask_swagger import swagger
from api.utils import APIException, generate_sitemap
from api.models import db
from api.routes import api
from api.admin import setup_admin
from api.commands import setup_commands

# from models import Person

ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
static_file_dir = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), '../public/')
app = Flask(__name__)
app.url_map.strict_slashes = False

# database condiguration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
=======
import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from flask_migrate import Migrate
#from flask_swagger import swagger
from api.utils import APIException, generate_sitemap
from api.models import db
from api.routes import api, configure_mail  # Importar la función de configuración de mail
from api.admin import setup_admin
from api.commands import setup_commands
from flask_jwt_extended import JWTManager

ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../public/')
app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Configuración de la base de datos
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db, compare_type=True)
db.init_app(app)

<<<<<<< HEAD
# add the admin
setup_admin(app)

# add the admin
setup_commands(app)

# Add all endpoints form the API with a "api" prefix
app.register_blueprint(api, url_prefix='/api')

# Handle/serialize errors like a JSON object


=======
# Configurar mail
configure_mail(app)

# Añadir el administrador
setup_admin(app)

# Añadir los comandos
setup_commands(app)

# Añadir todos los endpoints del API con el prefijo "api"
app.register_blueprint(api, url_prefix='/api')

# Manejar/serializar errores como un objeto JSON
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

<<<<<<< HEAD
# generate sitemap with all your endpoints


=======
# Generar sitemap con todos los endpoints
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
@app.route('/')
def sitemap():
    if ENV == "development":
        return generate_sitemap(app)
    return send_from_directory(static_file_dir, 'index.html')

<<<<<<< HEAD
# any other endpoint will try to serve it like a static file


=======
# Cualquier otro endpoint intentará servirlo como un archivo estático
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = 'index.html'
    response = send_from_directory(static_file_dir, path)
<<<<<<< HEAD
    response.cache_control.max_age = 0  # avoid cache memory
    return response


# this only runs if `$ python src/main.py` is executed
=======
    response.cache_control.max_age = 0  # evitar caché de memoria
    return response

# Ejecutar solo si se ejecuta `$ python src/main.py`
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)
