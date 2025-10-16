from datetime import datetime, timezone
import os
from fastapi import FastAPI, HTTPException
import httpx
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

app = FastAPI()

@app.get("/me")
async def get_profile():
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get("https://catfact.ninja/fact")
            response.raise_for_status()
            data = response.json()
            cat_fact = data.get("fact", "Cats have 4 legs")

    except httpx.RequestError:
        cat_fact = "Failed to fetch fact right now"

    current_time = datetime.now(timezone.utc).isoformat()
    
    payload = {
        "status": "success",
        "user":{
            "email": os.getenv("USER_EMAIL", "tosisiyesteve@gmail.com"),
            "name": os.getenv("USER_NAME", "Stephen Tosisiye Akande"),
            "stack": os.getenv("USER_STACK", "Python/FastAPI")
        },
        "timestamp": current_time,
        "fact": cat_fact
    }

    return JSONResponse(content=payload, media_type="application/json")