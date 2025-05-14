#prompt to openai

def build_prompt(question):
    system_message = ("You are a financial assistant chatbot. Answer user questions clearly and concisely."
                        "Keep explanations simple. Avoid jargon unless needed. If asked about a non-finance topic, politely decline.")
    return [
        {"role":"system", "content": system_message},
        {"role":"user", "content": question} 
    ]                   
    