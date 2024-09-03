from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri='redis://localhost:6380/0'
)

cache = Cache()
