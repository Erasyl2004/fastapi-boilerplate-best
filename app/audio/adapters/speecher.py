from rev_ai.models import CustomVocabulary
from rev_ai.models import CustomerUrlData
from rev_ai import apiclient
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()

def generate_text(source_url: str):
        custom_vocabularies = [CustomVocabulary(["Kaspi", "Kaspi Bank", "Kaspi Bonus", "Kaspi Kartomat", "Kaspi Gold", "Kaspi Deposit"])]
        client = apiclient.RevAiAPIClient(os.getenv("rev_ai_api_key"))
        url_job = client.submit_job_url(source_config=CustomerUrlData(url=source_url), language="en", custom_vocabularies=custom_vocabularies)
        return url_job.id


def get_text(job_id: str):
        client = apiclient.RevAiAPIClient(os.getenv("rev_ai_api_key"))
        while True:
            if str(client.get_job_details(job_id).status) == 'JobStatus.TRANSCRIBED':
                transcript_json = client.get_transcript_json(job_id)
                return transcript_json
            sleep(5)