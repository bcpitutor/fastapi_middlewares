from fastapi_middlewares.itutor_google_sso import (
    install_google_sso, 
    iTutorGoogleSSORoutesMiddleware, 
    LOGIN_FUNCTION
)
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()

install_google_sso(
    app=app,
    client_id="mi-client-id",
    client_secret="mi-client-secret",
    login_base_path="/admin/login"
)

app.add_middleware(
    iTutorGoogleSSORoutesMiddleware,
    allowed_routes = ["/admin/login*"],
    protected_routes = ["/admin*"],
    login_url = app.url_path_for(LOGIN_FUNCTION)
)

# SessionMiddleware should be added after iTutorGoogleSSORoutesMiddleware
# or it is not going to work.

app.add_middleware(SessionMiddleware, secret_key="mySecretKey")

