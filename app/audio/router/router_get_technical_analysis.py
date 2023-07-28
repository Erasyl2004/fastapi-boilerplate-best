from fastapi import Depends
from app.audio.adapters import LangChain
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from typing import Any
from ..service import Service, get_service

from . import router


class GetTechnicalAnalysisResponse(AppModel):
    technical_analysis: Any

class GetTechnicalAnalysisRequest(AppModel):
    id_of_speech: str

@router.post("/technical_analysis" , response_model=GetTechnicalAnalysisResponse)
def get_technical_analysis(
    input: GetTechnicalAnalysisRequest,
    svc: Service = Depends(get_service)
):
    speech = svc.repository.get_speech_by_id(input.id_of_speech)
    analysis = LangChain.get_technical_analysis(speech)
    return GetTechnicalAnalysisResponse(technical_analysis=analysis)
