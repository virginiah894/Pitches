import os
class  Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Perry@localhost/pitches'
  SECRET_KEY = '12345679'
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS =True
  MAIL_USERNAME =os.environ.get("MAIL_USERNAME")
  MAIL_PASSOWRD =os.environ.get("MAIL_PASSWORD")
  SIMPLEMDE_JS_LIFE = True
  SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Perry@localhost/pitches'


class prodConfig(Config):
  pass
class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Perry@localhost/pitches'
  

  DEBUG = True

  
config_options ={
    'development':DevConfig,
    
    'production':prodConfig,
    'test':TestConfig
  }
