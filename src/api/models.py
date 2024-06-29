from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD

db = SQLAlchemy()
=======
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
<<<<<<< HEAD
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
=======
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)
    user_uuid= db.Column(db.String(250), nullable=True)
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
<<<<<<< HEAD
            # do not serialize the password, its a security breach
        }
=======
            "password": self.password,
            "user_uuid": self.user_uuid
        }

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
>>>>>>> daeec6084f2f76cf862888ab4517a4719b87d2bc
