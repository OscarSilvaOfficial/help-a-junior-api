import os
from dotenv import load_dotenv, find_dotenv

verison="0.3.3"
load_dotenv(find_dotenv())

PORT = os.getenv('PORT')
ADDR = os.getenv('ADDR') 