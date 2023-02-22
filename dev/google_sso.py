from fastapi_middlewares.itutor_google_sso import (
    install_google_sso
)
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
import local_config as settings

app = FastAPI()

install_google_sso(
    app=app,
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    login_base_path=f"/admin/google_sso",
    redirect_after_login = "/admin/algo",
    protected_routes = ["/admin*"],
)

# SessionMiddleware should be added after iTutorGoogleSSORoutesMiddleware
# or it is not going to work.
app.add_middleware(SessionMiddleware, secret_key="mySecretKey")
