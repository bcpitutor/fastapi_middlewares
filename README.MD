# FastAPI Middlewares

This package provide useful middlewares for our FastAPI microservices

## Installation

```bash
pip install git+https://github.com/bcpitutor/fastapi_middlewares
```

## Middlewares:

### iTutorGoogleSSORoutesMiddleware

Middleware to define which routes need to be validated with @itutor.com google sso

Usage: 

```python
from fastapi_middlewares.itutor_google_sso import (
    install_google_sso
)
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

install_google_sso(
    app=app,
    client_id="mi-client-id",
    client_secret="mi-client-secret",
    login_base_path="/google-sso",
    redirect_after_login = "/asd",
    protected_routes = ["/admin*"],
)

# SessionMiddleware should be added after iTutorGoogleSSORoutesMiddleware
# or it is not going to work.

app.add_middleware(SessionMiddleware, secret_key="mySecretKey")
```
### Description:

#### Function `install_google_sso`:

Installs google sso routes for login and logout

Params:
-  `client_id`: `string`, Google Oauth client_id.
-  `client_secret`: `string`, Google Oauth client_secret.
-  `login_base_path`: `string`, base url for the login form.
-  `redirect_after_login`: `string`, path to redirect after logged in with google sso.
-  `allowed_routes`: List with allowed routes routes, if a path is present here will not be validated if is protected, it supports asterisk. I.E `/admin/*`
-  `protected_routes`: List with protected routes, it supports asterisk. I.E `/admin/*`
-  `scope_kwargs`: `Dict[str,str]`, scope requested to the client.

This middleware also has two useful constants to get the login and logout url:

```python 
from fastapi_middlewares.itutor_google_sso import LOGIN_FUNCTION, LOGOUT_FUNCTION

# Then you can use this constants to get the URLs:

login_path = request.url_path_for(LOGIN_FUNCTION)
logout_path = request.url_path_for(LOGOUT_FUNCTION)

```
