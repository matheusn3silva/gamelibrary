import os

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        user = 'root',
        password = 'admin',
        server = 'localhost',
        database = 'jogoteca'
    )


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads' # RETURN FOLDER UPLOADS IN JOGOTECA