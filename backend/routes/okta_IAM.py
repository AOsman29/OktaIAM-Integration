from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, JSONResponse
import os
import requests
from urllib.parse import urlencode

router = APIRouter()

OKTA_CLIENT_ID = os.getenv("OKTA_CLIENT_ID")
OKTA_CLIENT_SECRET = os.getenv("OKTA_CLIENT_SECRET")
OKTA_ISSUER_URL = os.getenv("OKTA_ISSUER_URL")
OKTA_REDIRECT_URI = os.getenv("OKTA_REDIRECT_URI")

@router.get("/login")
def login_redirect():
    params = {
        "client_id": OKTA_CLIENT_ID,
        "response_type": "code",
        "scope": "openid profile email",
        "redirect_uri": OKTA_REDIRECT_URI,
        "state": "demo123",
        "nonce": "secure_nonce"
    }
    auth_url = f"{OKTA_ISSUER_URL}/v1/authorize?{urlencode(params)}"
    return RedirectResponse(auth_url)

@router.get("/callback")
def okta_callback(request: Request, code: str = None):
    if not code:
        return JSONResponse({"error": "Missing code"}, status_code=400)

    token_url = f"{OKTA_ISSUER_URL}/v1/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": OKTA_REDIRECT_URI,
        "client_id": OKTA_CLIENT_ID,
        "client_secret": OKTA_CLIENT_SECRET,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    token_response = requests.post(token_url, data=data, headers=headers)
    if token_response.status_code != 200:
        return JSONResponse({"error": "Token exchange failed", "details": token_response.text})

    tokens = token_response.json()
    return RedirectResponse(url="/secure/dashboard.html")
