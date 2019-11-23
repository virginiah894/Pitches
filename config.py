import os
class  Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Perry@localhost/pitches'


class prodConfig(Config):
  pass
class DevConfig(Config):
  DEBUG = True
  
config_options ={
    'development':DevConfig,
    
    'production':prodConfig
  }
