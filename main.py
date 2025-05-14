import openai
from build_prompt import build_prompt

import os
openai.api_key = os.getenv("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")

'''
function to produce answer based on user query
    input: user query
    output: response from gpt-4o-mini
'''
def answer_query(query):
    messages = build_prompt(query)

    try:
        response = openai.ChatCompletion.create(model= "gpt-4o-mini", messages= messages)
        return response.choices[0].message["content"]

#initial message to user
if __name__ == "__main__":
    print("Welcome to the Finance Chatbot!")
    print("Please enter your finanial query.")

#running chatbot until user quits
while True:
    user_input= input("Q: ")
    answer= answer_query(user_input)
    print(f"A: {answer}\n")

