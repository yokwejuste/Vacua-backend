import os

import firebase_admin
from firebase_admin import credentials, firestore

from vacua.settings import BASE_DIR, env

cred = credentials.Certificate(os.path.join(BASE_DIR, env('GOOGLE_CREDENTIALS')))
firebase_admin.initialize_app(cred)

db = firestore.client()
