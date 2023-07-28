from fastapi import Depends
from app.audio.adapters import LangChain
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from typing import Any
from ..service import Service, get_service

from . import router


class GetReglamentAnalysisResponse(AppModel):
    reglament_analysis: Any

class GetReglamentAnalysisRequest(AppModel):
    id_of_speech: str

@router.post("/reglament_analysis" , response_model=GetReglamentAnalysisResponse)
def get_analysis_by_reglament(
    input: GetReglamentAnalysisRequest,
    svc: Service = Depends(get_service)
):
    speech = svc.repository.get_speech_by_id(input.id_of_speech)
    analysis = LangChain.get_analysis_by_reglament(speech)
    return GetReglamentAnalysisResponse(reglament_analysis=analysis)
