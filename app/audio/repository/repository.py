from pymongo.database import Database
from bson.objectid import ObjectId


class AudioRepository:
    def __init__(self, database: Database):
        self.database = database

    
    def create_speech(self, speech_to_text: str):
        payload = {
            "speech": speech_to_text
        }

        self.database["speech_to_text"].insert_one(payload)
        return str(payload['_id'])
    
    def get_speech_by_id(self, user_id: str) -> dict | None:
        speech = self.database["speech_to_text"].find_one(
            {
                "_id": ObjectId(user_id),
            }
        )
        return str(speech["speech"])