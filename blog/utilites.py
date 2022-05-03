import os
import secrets
from PIL import Image

from blog import app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_name = random_hex + file_ext
    picture_path = os.path.join(
        app.root_path,
        'static/profile_pict',
        picture_name
    )

    available_size = (250, 250)
    image = Image.open(form_picture)
    image.thumbnail(available_size)

    image.save(picture_path)
    return picture_name
