# from typing import Any
from fastapi import Depends, UploadFile
from app.audio.adapters import speecher,parser
from app.utils import AppModel
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data 
from ..service import Service, get_service

from . import router

@router.post("/speech_to_text")
def speech_to_text(
    file: UploadFile,
    svc: Service = Depends(get_service),
):
    url = svc.s3_service.upload_file(file.file,file.filename)
    id = speecher.generate_text(url)
    text = parser.parse(speecher.get_text(id))
    id = svc.repository.create_speech(text)
    return id