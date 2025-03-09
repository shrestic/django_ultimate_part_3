import os
from .common import *

DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["shrestic-prod-05edadebd44a.herokuapp.com"]
