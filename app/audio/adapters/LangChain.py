import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from app.audio.adapters import gpt_api
from app.audio.source import inform_about_kaspi
from app.audio.source import prompt
import os
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(temperature=0, openai_api_key=os.getenv("openai_api_key"))

def update_vector_store():
    df = pd.DataFrame(inform_about_kaspi.documents)
    df.head()
    loader = DataFrameLoader(df, page_content_column='question')
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(openai_api_key="")
    db = FAISS.from_documents(texts, embeddings)
    db.as_retriever()
    db.save_local('./vectordb')


def get_technical_analysis(speech: str):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    question = gpt_api.get_evaluate_manager(messages,speech,prompt.prompt_question)
    question = eval(question)
    print(question)

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("openai_api_key"))
    db = FAISS.load_local('./vectordb',embeddings)
    tools = [
        Tool(
            name="kaspi search",
            func=db.similarity_search,
            description="useful for when you search by question",
        )
    ]
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION 
    )
    answer = ""
    for i in range(0,len(question["question"])):
        answer += "question: " + question["question"][i]["question"] + "\n"
        answer += "answer: " + agent.run(question["question"][i]["question"]) + "\n"
    print(answer)
    messages =[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f'{prompt.prompt_question}\n{speech}'},
        {"role": "assistant", "content": f'{question}'},
    ]
    response = gpt_api.get_evaluate_manager(messages,answer,prompt.prompt_technical_analysis)
    return eval(response)


def get_analysis_by_reglament(speech: str):
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    data = eval(gpt_api.get_evaluate_manager(messages,speech,prompt.prompt_evaluate))    
    # analysis = "This is the analysis carried out by the AI!!!\n"
    # for i in range (0,len(data[1]["corrections"])):
    #     analysis += f'<strong>{i + 1}) mistake:</strong> <em>{data[1]["corrections"][i]["mistake"]}</em>\n' 
    #     analysis += f'<strong>fix:</strong> <em>{data[1]["corrections"][i]["fix"]}</em>\n\n'
    # analysis += f'<strong>Opinion:</strong> <em>{data[0]["opinion"]}</em>\n\n'
    return data


def data_processing(json_analysis):
    analysis = "This is technical analysis carried out by the AI!!!\n"
    for i in range (0,len(json_analysis["response"])):
        analysis += f'<strong>{i + 1}) analyze:</strong> <em>{json_analysis["response"][i]["analyze"]}</em>\n' 
    return analysis