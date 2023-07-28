from app.audio.adapters import gpt_api
from app.audio.source import prompt
def parse(json_file):
    final = ""
    templates = json_file
    for i in range (0,len(templates["monologues"])):
        if templates["monologues"][i]["speaker"] == 0:
            text = "speaker A: "
            for k in range (0,len(templates["monologues"][i]["elements"])):
                if 'value' in templates["monologues"][i]["elements"][k]:
                    text += templates["monologues"][i]["elements"][k]["value"]
            final += text + "\n"
        if templates["monologues"][i]["speaker"] == 1:
            text2 = "speaker B: "
            for k in range (0,len(templates["monologues"][i]["elements"])):
                if 'value' in templates["monologues"][i]["elements"][k]:
                    text2 += templates["monologues"][i]["elements"][k]["value"]
            final += text2 + "\n"
    return final

def mark_the_speech(text: str):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ] 
    response = gpt_api.get_evaluate_manager(messages,text,prompt.prompt_markship)
    return response