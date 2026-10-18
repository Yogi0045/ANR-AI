from typing import List
from services.ai_services import extract_entries

from fastapi import FastAPI, APIRouter
from models.schema import Voice, MessageRequest
from dotenv import load_dotenv


app = FastAPI() #object for fastapi
router = APIRouter() #object for router

@router.get('/')
def home():
    message = {
       "message": "ANR AI is runnnig"
    }
    return message

@router.get("/about")
def about():
    info = {
        "about_us" : "This is an AI Assistant created to help my client to convert her voice into text or excel scheet"
    }
    return info


@router.post("/voice-to-text")
def voice_to_text(text:Voice):
    message = {
        "entry" : " voice_to_text has been recieved",
        "entry_text" : text.text
    }

    return message


@router.post("/shop-entry")
def shop_entry(user_input:MessageRequest):
    result = extract_entries(user_input.text)
    return result
