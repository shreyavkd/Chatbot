from openai import OpenAI
import os
from dotenv import load_dotenv

#loading API key discretely
load_dotenv()

#initialising OpenAI client
client= OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

'''
function to produce answer based on user query
    input: user query
    output: response from gpt-4o-mini
'''
def answer_query(query):
    messages= [
                {"role": "system", 
                 "content": "You are a helpful financial assistant."
                 "If asked any non-financial questions, please decline politely."},
                {"role": "user", "content": query}
            ]

    try:
        response= client.chat.completions.create(model= "gpt-4o-mini", messages= messages)
        return response.choices[0].message["content"]
    
    except Exception as err:
        return (f"Error:\n{err}\n")

#initial message to user
if __name__ == "__main__":
    print("Welcome to the Finance Chatbot!")
    print("Please enter your finanial query. Type 'q' to quit.")

#running chatbot until user quits
while True:
    user_input= input("Q: ")

    if user_input.lower() == ("q"):
        exit()

    answer= answer_query(user_input)
    print(f"A: {answer}\n")

