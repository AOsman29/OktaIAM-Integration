from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import okta_auth

app = FastAPI(title="Okta IAM Demo")

# CORS for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include Okta routes
app.include_router(okta_auth.router, prefix="/api/okta")

# Serve frontend
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
