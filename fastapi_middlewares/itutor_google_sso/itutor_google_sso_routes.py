from fastapi import Request, APIRouter
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from fastapi import Request
from fastapi.templating import Jinja2Templates
from typing import Optional
from config import settings

oauth = OAuth()
oauth.register(
    "google",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)
router = APIRouter()

admin_templates = Jinja2Templates(directory="templates/admin")

@router.get("/admin/login/google", include_in_schema=False)
async def google_sso(request: Request):
    # absolute url for callback
    # we will define it below
    redirect_uri = request.url_for("auth")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/admin/login", include_in_schema=False)
async def admin_login(request: Request, error_message: Optional[str] = None):
    # absolute url for callback
    # we will define it below
    auth_url = request.url_for("google_sso")
    return admin_templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "redirect_uri_google_sso": auth_url,
            "error_message": error_message,
        },
    )

@router.get("/auth", include_in_schema=False)
async def auth(request: Request):
    token = await oauth.google.authorize_access_token(request)
    # <=0.15
    # user = await oauth.google.parse_id_token(request, token)
    user = token.get("userinfo")
    if user:
        request.session["user"] = dict(user)
    return RedirectResponse(url="/admin/")


@router.get("/admin/logout", include_in_schema=False)
async def admin_logout(request: Request):
    request.session.pop("user", None)
    login_url = request.url_for("admin_login")
    return RedirectResponse(url=login_url)
