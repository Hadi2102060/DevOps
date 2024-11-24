from fastapi import FastAPI, Request
from pymongo.mongo_client import MongoClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Middleware to allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
client = MongoClient("mongodb://localhost:27017/")
db = client.demoDatabase
collection = db.emails



# Base route
@app.get('/')
async def demoApp():
    return "yasin_arafat"



# Endpoint to add email
@app.post('/add/mail')
async def addMail(request: Request):
    body = await request.json()  
    email = body.get("email")
    if email:
        print(f"Email received: {email}")
        collection.insert_one({"email": email})
        return {"response": email}
    else:
        return {"error": "Email not provided in request body"}, 400



# Endpoint to get emails
@app.get('/get/email')
async def getMail():
    # {} fetch all the email:
    # {"_id": 1, "email": 1}, fetch only id andthe email
    emails = collection.find({}, {"_id": 1, "email": 1})
    email_list = [email["email"] for email in emails]
    return {"email": email_list}
