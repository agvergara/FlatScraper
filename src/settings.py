import os
from os.path import abspath, dirname

from dotenv import load_dotenv

ROOT_PATH = dirname(dirname(abspath(__file__)))

ENV = os.environ.get('ENV', 'PRODUCTION')

load_dotenv(f"{ROOT_PATH}/.env.{ENV.lower}")

CHROMIUM_PATH = os.environ.get("CHROMIUM_PATH", f"{ROOT_PATH}/chrome-linux")
CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH", f"{ROOT_PATH}/chromedriver") 
