# FastAPI Middlewares

This package provide useful middlewares for our FastAPI microservices

## Installation

```bash
pip install git+https://github.com/bcpitutor/fastapi_middlewares
```

## Middlewares:

## Google SSO

Middleware to define which routes need to be validated with @itutor.com google sso, it also provides a way to define which users are allowed to access the protected routes.

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
-  `allowed_routes`: List with allowed routes routes, if a path is present here will not be validated if is protected, it supports asterisk. I.E `/admin/*`
-  `protected_routes`: List with protected routes, it supports asterisk. I.E `/admin/*`
-  `allowed_users`: If present, only users in this list will be allowed to access the protected routes. Otherwhise all users with @itutor.com domain will be allowed.
-  `scope_kwargs`: `Dict[str,str]`, scope requested to the client.