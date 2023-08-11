from fastapi import Depends
from app.audio.adapters import LangChain
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from typing import Any
from app.audio.adapters import parser
from ..service import Service, get_service
from fastapi import Response
from . import router

class UpdateSpeechToTextRequest(AppModel):
    id_of_speech: str    
    speech: str

@router.post("/update_speech_to_text")
def update_speech_to_text(
    input: UpdateSpeechToTextRequest,
    svc: Service = Depends(get_service)
):
    mark = parser.mark_the_speech(input.speech)
    speech = "roles:\n" + mark + "\ntext:\n" + input.speech
    svc.repository.update_speech(input.id_of_speech,speech)
    return Response(status_code=200)
