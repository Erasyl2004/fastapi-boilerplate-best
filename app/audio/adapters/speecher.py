from rev_ai.models import CustomVocabulary
from rev_ai.models import CustomerUrlData
from rev_ai import apiclient
import env
from time import sleep


def generate_text(source_url: str):
        custom_vocabularies = [CustomVocabulary(["Kaspi Bank", "Kaspi Red"])]
        client = apiclient.RevAiAPIClient(env.rev_ai_api_key)
        url_job = client.submit_job_url(source_config=CustomerUrlData(url=source_url), language="en", custom_vocabularies=custom_vocabularies)
        return url_job.id


def get_text(job_id: str):
        client = apiclient.RevAiAPIClient(env.rev_ai_api_key)
        while True:
            if str(client.get_job_details(job_id).status) == 'JobStatus.TRANSCRIBED':
                transcript_json = client.get_transcript_json(job_id)
                return transcript_json
            sleep(5)