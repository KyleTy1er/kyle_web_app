# web_app/services/basilica_service.py

import basilica
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(API_KEY)


