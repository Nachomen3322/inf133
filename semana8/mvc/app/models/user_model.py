from database import db

# Se importa el objeto
# el db.model es una clase base para todos los modelos de SQALchemy
# Define la clase User que hereda dbModel
# User representa la tabla users en la bd


class User(db.Model):
    __table__name = "users"
    # Define las columnas de la tabla users
    id = db.Column(db.Integer, primary_key=True)
    # Es una columna de tipo coduno, no es nuleable
    first_name = db.Column(db.String(50), nullable=False)
    # No puede ser nullable
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)

    # Inicializa la clase User

    def __init__(self, first_name, last_name, email, password, date):
        # No necesita hacer la llave que tenga etc
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.date = date

    # Guarda us
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Query,  la forma en la que consulta la info, todo esta aca, solo se encarga de usuarios y nada mas.
    @staticmethod
    def get_all():
        # ya no hay que hacer lo otro
        return User.query.all()

    # cambia modelo y listas, en el formulario aplicar
