from config import TOKEN
from fastapi_users.authentication import (
    CookieTransport,
    JWTStrategy,
    AuthenticationBackend,
)

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_name="Hello")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=TOKEN, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
