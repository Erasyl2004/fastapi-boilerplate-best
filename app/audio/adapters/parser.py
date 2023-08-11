from app.audio.adapters import gpt_api
from app.audio.source import prompt
import json
def parse(json_file):
    final = []
    templates = json_file
    for i in range (0,len(templates["monologues"])):
        if templates["monologues"][i]["speaker"] == 0:
            text = ""
            for k in range (0,len(templates["monologues"][i]["elements"])):
                if 'value' in templates["monologues"][i]["elements"][k]:
                    text += templates["monologues"][i]["elements"][k]["value"]
            final.append({"speaker0": text})
        if templates["monologues"][i]["speaker"] == 1:
            text2 = ""
            for k in range (0,len(templates["monologues"][i]["elements"])):
                if 'value' in templates["monologues"][i]["elements"][k]:
                    text2 += templates["monologues"][i]["elements"][k]["value"]
            final.append({"speaker1": text2})
    return json.dumps(final)

def mark_the_speech(text: str):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ] 
    response = gpt_api.get_evaluate_manager(messages,text,prompt.prompt_markship)
    return response