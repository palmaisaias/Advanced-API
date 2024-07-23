#moved this to a file like was created in class because I could not for the life of me solve a circular import so I had to rework a lot of my code :)

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "3 per second"])