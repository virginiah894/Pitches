import os
class  Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Perry@localhost/pitches'
  UPLOADED_PHOTOS_DEST ='app/static/photos'

  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS =True
  MAIL_USERNAME =os.environ.get("MAIL_USERNAME")
  MAIL_PASSOWRD =os.environ.get("MAIL_PASSWORD")
class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Perry@localhost/pitches_tests'


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
