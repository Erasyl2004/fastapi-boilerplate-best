from fastapi import Depends
from app.audio.adapters import LangChain
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from typing import Any
from ..service import Service, get_service

from . import router

class GetSpeechToText(AppModel):
    id_of_speech: str

@router.post("/get_speech_to_text")
def get_speech_to_text(
    input: GetSpeechToText,
    svc: Service = Depends(get_service)
):
    speech = svc.repository.get_speech_by_id(input.id_of_speech)
    return eval(speech)