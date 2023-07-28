
from app.config import database
from .repository.repository import AudioRepository
from .adapters.s3_service import S3Service

class Service:
    def __init__(self):
        self.repository = AudioRepository(database)
        self.s3_service = S3Service()


def get_service():
    svc = Service()
    return svc