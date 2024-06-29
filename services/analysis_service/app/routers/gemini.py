from fastapi import APIRouter, HTTPException, Query
import google.generativeai as genai
import os

router = APIRouter()

api_key = os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("API_KEY environment variable is not set")

genai.configure(api_key=api_key)

@router.get('/generate', tags=["generate"])
async def generate(prompt: str = Query(...)):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return {"success": response.text}
    except genai.ApiError as e:
        raise HTTPException(status_code=500, detail=f"API Error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")