from flask import Flask, request, jsonify, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_mail import Mail, Message
from datetime import datetime, timedelta
import jwt

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

# Configuración de Flask-Mail
mail = Mail()
def configure_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.office365.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'cwspablo@outlook.com' #correo real y pass
    app.config['MAIL_PASSWORD'] = '4geeks4geeks'
    mail.init_app(app)

def generate_reset_token(email):
    payload = {
        'exp': datetime.utcnow() + timedelta(hours=1),
        'iat': datetime.utcnow(),
        'sub': email
    }
    return jwt.encode(payload, 'SECRET_KEY', algorithm='HS256')

def decode_reset_token(token):
    try:
        payload = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200

@api.route('/users', methods=['GET'])
def handle_users():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))
    return jsonify(all_users), 200

@api.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()
    if not request_data or 'email' not in request_data or 'password' not in request_data:
        raise APIException('Invalid request body', status_code=400)

    new_user = User(email=request_data['email'])
    new_user.set_password(request_data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.serialize())

@api.route('/login', methods=['POST'])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()

    if user is None or not user.check_password(password):
        return jsonify({"msg" : "Invalid email or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"token": access_token, "user_id": user.id})

@api.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.filter.get(current_user_id)
    return jsonify({"id": user.id, "email": user.email}), 200

# Ruta para solicitar la recuperación de contraseña
@api.route('/forgot-password', methods=['POST'])
def forgot_password():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    
    if user:
        token = generate_reset_token(email)
        reset_link = f"http://127.0.0.1:3000/resetpassword/{token}"
        
        msg = Message("Password Reset Request",
                      sender="cwspablo@outlook.com", #cambiar por mi correo
                      recipients=[email])
        msg.body = f"To reset your password, visit the following link: {reset_link}"
        mail.send(msg)
        
        return jsonify({"msg": "Password reset link sent"}), 200
    
    return jsonify({"msg": "Email not found"}), 404

# Ruta para restablecer la contraseña
@api.route('/reset-password/<token>', methods=['PUT'])
@jwt_required()
def reset_password(token):
    current_user_id = get_jwt_identity()
    new_password = request.json.get('password')
    print(new_password)
    user = User.query.get(current_user_id)
    if user:
        user.set_password(new_password)
        db.session.commit()
        return jsonify({"msg": "Password has been reset"}), 200
    
    return jsonify({"msg": "User not found"}), 404
