from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import datetime
import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = "./data"

@app.options("/api/test")
async def preflight():
    return {"message": "Preflight OK"}

@app.post("/api/test")
async def test(request: Request):
    data = await request.json()
    print()
    print(data)
    print()
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = os.path.join(DATA_DIR, f"{timestamp}.json")
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return {"message": "JSON salvo com sucesso!", "file": file_path}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
