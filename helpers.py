import os
from jogoteca import app

def recovery_image(id):
    for archive_name in os.listdir(app.config['UPLOAD_PATH']):
        print("Arquivo na pasta:", archive_name)
        if f'cover{id}.jpg' == archive_name:
            return archive_name

    return 'standard_cover.jpg'