import os
from dotenv import load_dotenv

load_dotenv()

# Constant's
DB_USER = os.getenv('DB_USER')
DB_USER_PW = os.getenv('DB_USER_PW')

# Flask settings
SECRET_KEY = os.getenv('SECRET_KEY_FLASK')

# Flask SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_USER_PW}' \
                          '@localhost/db_flask_site'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask WTF settings
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY')

