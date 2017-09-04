import os

#grab folder where script lives
basedir = os.path.abspath(os.path.dirname(__file__))
JSON_AS_ASCII = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
# This is the path to the upload directory
UPLOAD_FOLDER = 'uploads/'

DATABASE = 'allcards.db'
WTF_CSRF_ENABLED = True
SECRET_KEY = """<your-secret-key-goes-here>"""

'''1159e07zxczc1f0cccf c529a8100914af 4022480dd9ae11 da9b17f91f40fb 4b12f6cb896602
a23b8a2b4808f4  53d25a8f7999f6 3a04e99fbqwdqwe  qweqewqwpo99009aslkasjlksl82198c298 3f957afec1c2df
b1a19348c4www4d56 4b2ca21c1190ff  f13154e90e5ff3 e91799ad25b286
575543582fe00e d9461eab8d465f 94034360f5adc0 8aa8a20b173176 b38eb32cb7f73e
28dea6d87f7796 86ee615344b710 c720679eb1alsdkalsdkd8d9 dae3ed2f629a62 3c271abdd3443f
991ed8963wcccc9e2d 1zcxzxcz8b0241cee1378 a98938a77dfe31 ee406cc17d11c0 2d3e9a0aa1aa13
e4f474e79369b5 2aaa32891c27b6 30e5f3c0c1zxczacx9f2e 06d9cc9631ebe1 ee12907a7af2e7
fe33e091d4f8d9 e4289833bcc1b3 3619249e677bea 48asaaaae8cdab76ac91 b81fa50b0f7329'''

#COMMENT OUT BELOW LINES IN PRODUCTION SERVER

#DATABASE_PATH = os.path.join(basedir, DATABASE)

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH