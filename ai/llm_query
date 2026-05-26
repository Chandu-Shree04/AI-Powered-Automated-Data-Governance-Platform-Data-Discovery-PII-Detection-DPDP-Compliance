import ollama
from config import OLLAMA_MODEL

def ask_llm(question, metadata):

    prompt = f"""
    You are a data analyst assistant.

    Dataset Metadata:
    {metadata}

    User Question:
    {question}

    Provide insights.
    """

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response['message']['content']
