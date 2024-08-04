from openai import OpenAI
from io import BytesIO
from fastapi import HTTPException
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse
import os
import requests

load_dotenv()

client = OpenAI()

def generate_design(data):
    try:
        response = client.images.generate(
            model=os.getenv("IMAGE_MODEL"),
            prompt=data.context,
            size=os.getenv("IMAGE_SIZE"),
            quality="standard",
            n=1,
        )
        # Extract the URL from the response
        image_url = response.data[0].url
        
        # Fetch the image content
        image_response = requests.get(image_url)
        image_bytes = BytesIO(image_response.content)

        # Return the image as a StreamingResponse
        return StreamingResponse(image_bytes, media_type="image/jpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
