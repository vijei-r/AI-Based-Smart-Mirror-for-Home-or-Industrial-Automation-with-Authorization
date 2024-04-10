import firebase_admin
from firebase_admin import credentials,db
cred = credentials.Certificate("your json file path")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'your db_url'})
ref=db.reference('test')


