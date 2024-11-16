from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import pyperclip
import uvicorn
from dotenv import load_dotenv
from prompt import sys_prompt

import os
from groq import Groq
import instructor
from pydantic import BaseModel, Field
from typing import List, Optional
from dotenv import load_dotenv

class CodeModel(BaseModel):
    code: str

def get_output(prompt:str, ques:str):
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        client = instructor.from_groq(client, mode=instructor.Mode.TOOLS)

        output = client.chat.completions.create(
            #model="llama3-groq-8b-8192-tool-use-preview",
            model="llama-3.1-70b-versatile",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": ques},
            ],
            response_model=CodeModel,
        )
        return output

app = FastAPI()
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "Hello, World!"

@app.get("/send", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/form", response_class=HTMLResponse)
async def form_handler(data: str = Form(...)):
    try:
        pyperclip.copy(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to write to clipboard")
    return f"Received data: {data}"

@app.get("/clip", response_class=HTMLResponse)
async def clip_handler(request: Request):
    try:
        clipboard_content = pyperclip.paste()
        print(clipboard_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to get clipboard content")
    output = get_output(sys_prompt, clipboard_content)
    pyperclip.copy(output.code)
    print(output.code)
    #return templates.TemplateResponse(name="disp.html", request=request, context={"id": clipboard_content})
    return f"{clipboard_content}"

if __name__ == "__main__":
    
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=3100)