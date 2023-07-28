import openai
import env

openai.api_key = env.openai_api_key

def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

def get_response(messages):
    response= openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']

def get_evaluate_manager(messages,information: str,prompt: str):
    messages = update(messages, "user", f'{prompt}\n{information}')
    model_response = get_response(messages)
    messages = update(messages, "assistant" , model_response)
    return model_response