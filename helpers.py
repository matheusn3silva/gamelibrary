import os
from jogoteca import app

def recovery_image(id):
    for archive_name in os.listdir(app.config['UPLOAD_PATH']):
        if f'cover{id}' in archive_name:
            return archive_name

    return 'standard_cover.jpg'


def cover_delete(id):
    image = recovery_image(id)
    if image != 'standard_cover.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], image))