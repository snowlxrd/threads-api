from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS biar bisa diakses dari bookmarklet
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello from Threads UID API"}

@app.get("/api/followers")
def get_followers(username: str):
    # Dummy response dulu
    followers = [{"username": f"{username}_follower{i}", "uid": 1000000 + i} for i in range(1, 11)]
    return {"followers": followers}
