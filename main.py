from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Unofficial Threads API (harus sudah di-clone atau diinstal secara lokal sebagai modul)
from threads import Threads

app = FastAPI()

# CORS agar bisa diakses dari JS Bookmarklet
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy akun Threads untuk akses publik (disarankan ganti dengan akunmu yg valid)
threads = Threads()
threads.login("your_username", "your_password")  # Ganti dengan kredensial kamu

@app.get("/")
def home():
    return {"message": "Threads UID API is running"}

@app.get("/api/followers")
def get_followers(username: str = Query(...)):
    try:
        user_id = threads.get_user_id(username)
        followers = threads.get_user_followers(user_id)

        results = []
        for f in followers:
            results.append({
                "username": f.username,
                "uid": f.pk,
                "name": f.full_name
            })

        return {"followers": results}

    except Exception as e:
        return {"error": str(e)}
