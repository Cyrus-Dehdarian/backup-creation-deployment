import os
import time
import base64
import subprocess
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, HTTPException, status, BackgroundTasks, WebSocket


#Making the requests acceptable from out side
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


@app.post('/PullBackup')
def creating_backup():
    return {"Value": "This is a response from 192.168.50.43"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)