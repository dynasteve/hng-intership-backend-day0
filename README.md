# 🐱 HNG Intership Stage 0 — Dynamic Profile Endpoint

## Overview
A simple FastAPI app that returns profile info along with a random cat fact fetched from the Cat Facts API.

## Endpoints
**GET** `/me`

### Example Response
```json
{
  "status": "success",
  "user": {
    "email": "your_email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-16T14:12:34.567Z",
  "fact": "Cats sleep 70% of their lives."
}
Setup Instructions
Clone the repo

Create and activate a virtual environment

Install dependencies:


Copy code
pip install -r requirements.txt
Create a .env file:

ini
Copy code
USER_EMAIL=you@example.com
USER_NAME=Your Name
USER_STACK=Python/FastAPI
Run the app:

bash
Copy code
uvicorn main:app --reload
Visit: http://127.0.0.1:8000/me

Deployment
Deployed on [Railway/Fly.io/etc.]
Live URL: [https://yourapp-domain/me]

Technologies
FastAPI

httpx

python-dotenv

yaml
Copy code

---

### 🪄 **PHASE 8: Test + Submit**

Before submitting:
✅ Verify your deployed `/me` endpoint works  
✅ Test from multiple networks  
✅ Ensure `Content-Type: application/json`  
✅ Timestamp updates dynamically  
✅ Cat fact changes on reload  

Then go to Slack:
/stage-zero-backend

yaml
Copy code
Submit:
- Live `/me` endpoint URL  
- GitHub repo  
- Full name  
- Email  
- Stack (Python/FastAPI)

---
