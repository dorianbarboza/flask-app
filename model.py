from main import DatabaseInstanceAlchemy

class Person(DatabaseInstanceAlchemy.Model):

    #__tablename__ = 'Person'

    id = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Integer, primary_key = True)
    firstName = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(120), unique = False)
    lastName = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(120), unique = False)
    email = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(120), unique = False)

    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email
            }

class Usuario(DatabaseInstanceAlchemy.Model):

    #__tablename__ = 'Usuario'

    ID_Usuario = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Integer, primary_key = True)
    username = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(10), unique = False)
    password = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(10), unique = False)

    def __init__(self, ID_Usuario, username, password):
        self.ID_Usuario = ID_Usuario
        self.username = username
        self.password = password

    def __repr__(self):
        return '<ID_Usuario> {}'.format(self.ID_Usuario)

    def serialize(self):
        return {
            'ID_Usuario': self.ID_Usuario,
            'username': self.username,
            'password': self.password
            }

class Artista(DatabaseInstanceAlchemy.Model):

    #__tablename__ = 'Artista'

    ID_Artista = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Integer, primary_key = True)
    Seudonimo = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Nombre = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Apellido = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    FechaNacimiento = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Date, unique = False)
    Ciudad = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Pais = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    UrlImg = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(100), unique = False)

    def __init__(self, Seudonimo, Nombre, Apellido, FechaNacimiento, Ciudad, Pais, UrlImg):
        self.Seudonimo = Seudonimo
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.FechaNacimiento = FechaNacimiento
        self.Ciudad = Ciudad
        self.Pais = Pais
        self.UrlImg = UrlImg

    def __repr__(self):
        return '<ID_Artista> {}'.format(self.ID_Artista)

    def serialze(self):
        return {
            'ID_Artista': self.ID_Artista,
            'Seudonimo': self.Seudonimo,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'FechaNacimiento': self.FechaNacimiento,
            'Ciudad': self.Ciudad,
            'Pais': self.Pais,
            'UrlImg': self.UrlImg
            }

class Album(DatabaseInstanceAlchemy.Model):

    #__tablename__ = 'Album'

    ID_Album = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Integer, primary_key = True)
    NombreAlbum = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Publicacion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Date, unique = False)
    CiudadGrabacion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    PaisGrabacion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Duracion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Time, unique = False)
    UrlImgAlbum = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(100), unique = False)
    # FK ID_Artista Artista

    def __init__(self, NombreAlbum, Publicacion, CiudadGrabacion, PaisGrabacion, Duracion, UrlImgAlbum):
        self.NombreAlbum = NombreAlbum
        self.Publicacion = Publicacion
        self.CiudadGrabacion = CiudadGrabacion
        self.PaisGrabacion = PaisGrabacion
        self.Duracion = Duracion
        self.UrlImgAlbum = UrlImgAlbum

    def __repr__(self):
        return '<ID_Album> {}'.format(self.ID_Album)

    def serialize(self):
        return {
            'ID_Album': self.ID_Album,
            'Nombre': self.NombreAlbum,
            'Publicacion': self.Publicacion,
            'CiudadGrabacion': self.CiudadGrabacion,
            'PaisGrabacion': self.PaisGrabacion,
            'Duracion': self.Duracion,
            'UrlImg': self.UrlImg
            }

class Cancion(DatabaseInstanceAlchemy.Model):

    #__tablename__ = 'Cancion'

    ID_Cancion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Integer, primary_key = True)
    NombreCancion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    DuracionCancion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Time, unique = False)
    UrlSong = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(100), unique = False)
    # FK ID_Album Album

    def __init__(self, NombreCancion, DuracionCancion, UrlSong):
        self.NombreCancion = NombreCancion
        self.DuracionCancion = DuracionCancion
        self.UrlSong = UrlSong

    def __repr__(self):
        return '<ID_Cancion> {}'.format(self.ID_Cancion)

    def serialize(self):
        return {
            'ID_Cancion': self.ID_Cancion,
            'NombreCancion': self.NombreCancion,
            'DuracionCancion': self.DuracionCancion,
            'UrlSong': self.UrlSong
            }

DatabaseInstanceAlchemy.create_all()
