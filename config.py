class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/bes_ecom'
    CACHE_TYPE = 'SimpleCache'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False # to keep the message from populating everytime i run this thing
